"""Transformdict: a mapping that transforms keys on lookup

This module and ``test_transformdict.py`` were extracted from a
patch contributed to Python by Antoine Pitrou implementing his
PEP 455 -- Adding a key-transforming dictionary to collections.

As of Nov. 14, 2014, the patch was not yet merged to Python 3.5
(which is in pre-alpha). The patch is ``transformdict3.patch``,
part of issue #18986: Add a case-insensitive case-preserving dict.

http://bugs.python.org/issue18986
"""

from collections.abc import MutableMapping


_sentinel = object()


class TransformDict(MutableMapping):
    '''Dictionary that calls a transformation function when looking
    up keys, but preserves the original keys.

    >>> d = TransformDict(str.lower)
    >>> d['Foo'] = 5
    >>> d['foo'] == d['FOO'] == d['Foo'] == 5
    True
    >>> set(d.keys())
    {'Foo'}
    '''

    __slots__ = ('_transform', '_original', '_data')

    def __init__(self, transform, init_dict=None, **kwargs):
        '''Create a new TransformDict with the given *transform* function.
        *init_dict* and *kwargs* are optional initializers, as in the
        dict constructor.
        '''
        if not callable(transform):
            msg = 'expected a callable, got %r'
            raise TypeError(msg % transform.__class__)
        self._transform = transform
        # transformed => original
        self._original = {}
        self._data = {}
        if init_dict:
            self.update(init_dict)
        if kwargs:
            self.update(kwargs)

    def getitem(self, key):
        'D.getitem(key) -> (stored key, value)'
        transformed = self._transform(key)
        original = self._original[transformed]
        value = self._data[transformed]
        return original, value

    @property
    def transform_func(self):
        "This TransformDict's transformation function"
        return self._transform

    # Minimum set of methods required for MutableMapping

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._original.values())

    def __getitem__(self, key):
        return self._data[self._transform(key)]

    def __setitem__(self, key, value):
        transformed = self._transform(key)
        self._data[transformed] = value
        self._original.setdefault(transformed, key)

    def __delitem__(self, key):
        transformed = self._transform(key)
        del self._data[transformed]
        del self._original[transformed]

    # Methods overridden to mitigate the performance overhead.

    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        self._data.clear()
        self._original.clear()

    def __contains__(self, key):
        return self._transform(key) in self._data

    def get(self, key, default=None):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        return self._data.get(self._transform(key), default)

    def pop(self, key, default=_sentinel):
        '''D.pop(k[,d]) -> v, remove key and return corresponding value.
           If key is not found, d is returned if given, otherwise
           KeyError is raised.
        '''
        transformed = self._transform(key)
        if default is _sentinel:
            del self._original[transformed]
            return self._data.pop(transformed)
        else:
            self._original.pop(transformed, None)
            return self._data.pop(transformed, default)

    def popitem(self):
        '''D.popitem() -> (k, v), remove and return some (key, value) pair
           as a 2-tuple; but raise KeyError if D is empty.
        '''
        transformed, value = self._data.popitem()
        return self._original.pop(transformed), value

    # Other methods

    def copy(self):
        'D.copy() -> a shallow copy of D'
        other = self.__class__(self._transform)
        other._original = self._original.copy()
        other._data = self._data.copy()
        return other

    __copy__ = copy

    def __getstate__(self):
        return (self._transform, self._data, self._original)

    def __setstate__(self, state):
        self._transform, self._data, self._original = state

    def __repr__(self):
        try:
            equiv = dict(self)
        except TypeError:
            # Some keys are unhashable, fall back on .items()
            equiv = list(self.items())
        return '%s(%r, %s)' % (self.__class__.__name__,
                               self._transform, repr(equiv))

print ('---< class types.MappingProxyType(mapping) >---')
from types import MappingProxyType
d = {1: 'A'}
print('d = {0}'.format(d))
d_proxy = MappingProxyType(d)
print ('d_proxy = {0}'.format(d_proxy))
print ('type(d_proxy) = {0}'.format(type(d_proxy)))
print()
print('d_proxy[1] = {0}'.format(d_proxy[1]))
print()

try:
    print('---< d_proxy[2] = "B" >---')
    d_proxy[2] = 'B'
except Exception as e:
    print(e)
finally:
    pass

d[2] = 'B'
print('---< Add {2: "B"} to d')
print ('d_proxy = {0}'.format(d_proxy))
print()
print('d_proxy[2] = {0}'.format(d_proxy[2]))
print()

l = ['spam', 'spam', 'eggs', 'spam']
print ('l = {0}'.format(l))
print('type(l) = {0}'.format(type(l)))
print()
m = set(l)
print('m = {0}'.format(set(l)))
print('type(m) = {0}'.format(type(m)))
print()
print('---< transform m to list. >---')
n = list(m)
print('n = {0}'.format(n))
print('type(n) = {0}'.format(type(n)))
print()

print('---< literal >---')
s ={1}
print('s = {0}, type(s) = {1}'.format(s, type(s)))
print()
print('s.pop() = {0}'.format(s.pop()))
print()
print('s = {0}'.format(s))
print()

from dis import dis
A = dis('{0}')
print('A = \n{0}'.format(A))
print()
B = dis('set({1})')
print('B = \n{0}'.format(B))
print()

print('frozenset(range(10)) = {0}'.format(frozenset(range(10))))
print()

print('---< Set comprehension notation >---')
from unicodedata import name
C = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print('C = {0}'.format(C))
print()





