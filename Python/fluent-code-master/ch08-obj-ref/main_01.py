print('----------------------------------------------------------\n'
      '          8.3 The default copy is shallow.                \n'
      '----------------------------------------------------------\n')

'''
--------------------------------------------------------------------------
      common library
--------------------------------------------------------------------------
'''
#import os, sys
#sys.path.append(os.path.dirname(__file__))

import copy
from copy import deepcopy
#from bus import *
#from haunted_bus import *
#from twilight_bus import *
#from TwilightBus_Modify import *

'''
-------------------------------------------------------------------------
      Class Declaration
-------------------------------------------------------------------------
'''

# BEGIN BUS_CLASS
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
# END BUS_CLASS

# BEGIN HAUNTED_BUS_CLASS
class HauntedBus:
    '''A bus model haunted by ghost passengers'''

    def __init__(self, passengers=[]):  # <1>
        self.passengers = passengers  # <2>

    def pick(self, name):
        self.passengers.append(name)  # <3>

    def drop(self, name):
        self.passengers.remove(name)
# END HAUNTED_BUS_CLASS

# BEGIN TWILIGHT_BUS_CLASS
class TwilightBus:
    '''A bus model that makes passengers vanish'''

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # <1>
        else:
            self.passengers = passengers  #<2>

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>
# END TWILIGHT_BUS_CLASS

# BEGIN TWILIGHT_BUS_CLASS
class TwilightBus_Modify:
    '''A bus model that makes passengers vanish'''

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # <1>
        else:
            self.passengers = list(passengers)  #<2>

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>
# END TWILIGHT_BUS_CLASS

'''
copy.copy (x)
Returns a shallow copy of x.

copy.deepcopy (x [, memo]) ��
Returns a deep copy of x.

exception copy.error
Raises a module specific error.
'''
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1: {0}'.format(l1))
print('l2: {0}'.format(l2))
print()
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1: {0}'.format(l1))
print('l2: {0}'.format(l2))
print()

print('----------------------------------------------------------\n'
      '    8.3.1 Deep and Shallow copies of any object           \n'
      '----------------------------------------------------------\n')
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print('id(bus1) = {0}, id(bus2) = {1}, id(bus3) = {2}'.format(id(bus1), id(bus2), id(bus3)))
print()
bus1_drop = bus1.drop('Bill')
print('bus2.passengers = {0}'.format(bus2.passengers))
print('id(bus1.passengers) = {0}, id(bus2.passengers) = {1}, id(bus3.passengers) = {2}'.format(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)))
print('bus3.passengers = {0}'.format(bus3.passengers))
print()

'''
Circular reference that b referring to a is further added to a.
deepcopy still copies properly.
'''
a = [10, 20]
print('a = {0}'.format(a))
b = [a, 30]
print('[a, 30] = {0}'.format(b))
print()
a.append(b)
print('a = {0}'.format(a))
print()
c = deepcopy(a)
print('c = {0}'.format(c))
print()

print('----------------------------------------------------------\n'
      '         8.4 Function arguments as a reference            \n'
      '----------------------------------------------------------\n')
def f(a, b):
      a += b
      return a

x = 1
y = 2
print('f({0}, {1}) = {2}'.format(x, y, f(x, y)))
print()
print('x, y = {0}'.format((x, y)))
print()

a = [1, 2]
b = [3, 4]
print('f(a, b) = {0}'.format(f(a, b)))
print()
print('a, b = {0}'.format((a, b)))
print()

t = (10, 20)
u = (30, 40)
print('f(t, u) = {0}'.format(f(t, u)))
print()
print('t, u = {0}'.format((t, u)))
print()

print('-----------------------------------------------------------------\n'
      ' 8.4.1 Care should be taken                                      \n'
      '     when using variable types for default values of arguments.  \n'
      '-----------------------------------------------------------------\n')
bus1 = HauntedBus(['Alice', 'Bill'])
print('bus1.passengers = {0}'.format(bus1.passengers))
print()

bus1.pick('Charlie')
bus1.drop('Alice')
print('bus1.passengers = {0}'.format(bus1.passengers))
print()

bus2 = HauntedBus()
bus2.pick('Carrie')
print('bus2.passengers = {0}'.format(bus2.passengers))
print()

bus3 = HauntedBus()
print('bus3.passengers = {0}'.format(bus3.passengers))
print()

bus3.pick('Dave')
print('bus2.passengers = {0}'.format(bus2.passengers))
print()

print('bus2.passengers is bus3.passengers = {0}'.format(bus2.passengers is bus3.passengers))
print()

print('bus1.passengers = {0}'.format(bus1.passengers))
print()

print('dir(HauntedBus.__init__) = \n{0}'.format(dir(HauntedBus.__init__)))
print()

print('HauntedBus.__init__.__defaults__ = {0}'.format(HauntedBus.__init__.__defaults__))
print()

print('HauntedBus.__init__.__defaults__[0] is bus2.passengers = {0}'.format(HauntedBus.__init__.__defaults__[0] is bus2.passengers))
print()

print('-----------------------------------------------------------------\n'
      '    8.4.2 Make programs that use variable arguments robust.      \n'
      '-----------------------------------------------------------------\n')
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print('basketball_team = {0}'.format(basketball_team))
print()

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus_Modify(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print('basketball_team = {0}'.format(basketball_team))
print()

