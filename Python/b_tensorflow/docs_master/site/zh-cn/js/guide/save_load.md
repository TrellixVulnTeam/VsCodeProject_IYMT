# �ۑ���� tf.Model

TensorFlow.js�񋟗��ۑ��a���͌^�I���\�C���͌^�Ȑ��g�p[`Layers`](https://js.tensorflow.org/api/0.14.2/#Models)API���I�����LTensorFlow�͌^���I�B�\�����ȓI�͌^�C��\���l�I�͌^�B�g�pLayers API�I�꘢��v�D���g�p�����I�͌^�����񉻓I�C�A���䏫�ݖ{�������T�I���e�B

�{���������@���� TensorFlow.js ���ۑ��a���͌^(��JSON����)�B�䓯�ȓ�Tensorflow Python�͌^�B

�ȉ�������������͌^�F

- [��Keras�͌^](../tutorials/conversion/import_keras.md)
- [��Graphdef�͌^](../tutorials/conversion/import_saved_model.md)


## �ۑ� tf.Model

[`tf.Model`](https://js.tensorflow.org/api/0.14.2/#class:Model) �a [`tf.Sequential`](https://js.tensorflow.org/api/0.14.2/#class:Model)
���񋟗����� [`model.save`](https://js.tensorflow.org/api/0.14.2/#tf.Model.save) ��ۑ��꘢�͌^�I
_��(topology)_ �a _�d(weights)_ �B

-  ��(Topology): ���꘢�`�q�͌^�I�����i��@���g�p�I��������j�B����ܑ��݊O���I�͌^�d�I���p�B

-  �d(Weights): �����ȗL���i������͌^�d�I�񐧕����B���ʏ푶�ݗ^�񑊓��I�������B

��Ŋŕۑ��͌^�I�㐥�Y�q�I

```js
const saveResult = await model.save('localstorage://my-model-1');
```

�ꍱ���v���ӓI�n��:

- `save`  ���@�їp�� scheme �������I URL �������Q���i������ scheme�j�B���`�q����z�ۑ��͌^�I�n���I�^�B �ݖ{�ᒆ��g�p localstorage:// scheme ���͌^�ۑ����{�n���B
- �� scheme �V�@�� **�H�a(path)**�B �ݏ�ʓI��q���C�H�a��'my-model-1'�B
- `save` ���@���I�B
- `model.save` �I�ԉ񐥈꘢ JSON �ہC����܈ꍱ�\�L�p�I�M���C��@�͌^�I��a�d�I�召�B
- �p���ۑ��͌^�I���s��e�ߍ��ȉ��͌^�I���B�� node.js ���ۑ��͌^��s��j�V�͌^�݊풆����B


���ʉ䏫��ȉ��s�����āB

### �{�n�� (����)

**Scheme:** `localstorage://`

```js
await model.save('localstorage://my-model');
```
�ȍ݊�I[�{�n��](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)���Ȗ��� `my-model` ���ۑ��͌^�B���\�݊���V�@�ێ��s�C�������󐬁C�p����{�g�Ȑ����{�n���B ����Ȓ��ݖ{�n�I�������B

### IndexedDB (����)

**Scheme:** `indexeddb://`

```js
await model.save('indexeddb://my-model');
```

��͌^�ۑ�����I[IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)�����B
�^�{�n����C���ݍ��V�@���R���݁C���������瑶�I�ۓI�召�L��I�����B

### ������ (����)

**Scheme:** `downloads://`

```js
await model.save('downloads://my-model');
```
��퉺�͌^�������p�I�����C�󐶐��������F
 1. �꘢�� `[my-model].json` �I JSON �����C����ܗ��͌^�I��a���ʏ��v��I�d�����I���p�B
 2. �꘢�񐧕����C������ܖ� `[my-model].weights.bin` �I�d�B

�ȍX `[my-model]` �I���̈ȓ��꘢�s���I���̓I�����B

�R��`.json`�g�p���H�a�w�� `.bin`�C���Ș��������v������ݓ��꘢�������B

> ����: �^����v���p�ݓ������������V�O���\���B



### HTTP(S) Request

**Scheme:** `http://` or `https://`

```js
await model.save('http://model-server.domain/upload')
```

�����꘢Web���C�ȏ��͌^�ۑ���������B �T��������C�ȕ֕ۛ��\�����B
�͌^����[POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) �������w��I HTTP ����B
POST ���I body �����`multipart/form-data`�I�i���B���R�ȉ���������

 1. �꘢�� `model.json` �I JSON �����C������ܑ�a���ʕ`�q�I�d�����I���p�B
 2. �꘢�񐧕����C������ܖ� `[my-model].weights.bin` �I�d�B

���ӁC�������I���̎��v�^��q��I�ێ����S�����i�����̓��u���������C�ٖ@�X���j�B ��[ api ����](https://js.tensorflow.org/api/latest/#tf.io.browserHTTPRequest)��܈꘢ Python ��Вi�C�������@���g�p [flask](http://flask.pocoo.org/) web �y�˗������� `save` �I���B

�ʏ�C�K�� HTTP ����X���Q�������i��@�C�p���g�C���Ҕ@�ʗv�w��ۑ��͌^�I�����j�B�Ȓʑ� `tf.io.browserHTTPRequest` �������I URL�������Q���������� `save` �����I���ݍ����ʓI���x�T���B��API�ݍT�� HTTP �����ʒ񋟗��X��I�����B

��@�F

```js
await model.save(tf.io.browserHTTPRequest(
    'http://model-server.domain/upload',
    {method: 'PUT', headers: {'header_key_1': 'header_value_1'}}));
```


### �{�������n (����Node.js)

**Scheme:** `file://`

```js
await model.save('file:///path/to/my-model');
```

���sNode.js�@�䓖�R�Ȓ��ڕ����n�󊎕ۑ��͌^�B�����ߏ���ۑ���������`scheme`�V�@�w��I`path`���B

 1. �꘢�� `model.json` �I JSON �����C������ܑ�a���ʕ`�q�I�d�����I���p�B
1.  �꘢�񐧕����C������ܖ�`model.weights.bin`. �I�d�B

���ӁC�������I���̏��n�^��ʎw��I���S�����i���̓��u���������j�B


## �� tf.Model

��꘢�g�p��q���@�V��ۑ��I�͌^�C��Ȏg�p `tf.loadLayersModel` API�������B

��ňꉺ���͌^�I�㐥�Y�q�I

```js
const model = await tf.loadLayersModel('localstorage://my-model-1');
```

�ꍱ�������:
- ����`model.save()`,  `loadLayersModel`�����g�p�� **scheme**�I��URL�I�������Q���B���`�q���䘸�����͌^�I�ڌ^�B
- scheme �R**path**�w��B�ݏ�q��q���H�a`my-model-1`�B
- URL�������Ȕ�ֈ꘢����IOHandler�ڌ��I�ہB
- `tf.loadLayersModel()`�������I�B
- `tf.loadLayersModel`�ԉ�I�� `tf.Model`

���ʉ䏫��p�I�s�����āB


### �{�n�� (����)

**Scheme:** `localstorage://`

```js
const model = await tf.loadLayersModel('localstorage://my-model');
```

������I[�{�n��](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).
���꘢��`my-model`�͌^�B

### IndexedDB (����)

**Scheme:** `indexeddb://`

```js
const model = await tf.loadLayersModel('indexeddb://my-model');
```
������I[IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).
���꘢�͌^�B


### HTTP(S)

**Scheme:** `http://` or `https://`

```js
const model = await tf.loadLayersModel('http://model-server.domain/download/model.json');
```
����HTTP�[�_���͌^�B��`json` �����@�C���������I`json` �������p�I`.bin`�����B

> ���ӁF���H��˘�[`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)���@�B�@�ʓI���v�L�񋟌����Ifetch���@�C�Ȓ񋟑S�Ǖ��@����[`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)�������ڌ��v�������g�p����(`node-fetch`)[https://www.npmjs.com/package/node-fetch]�I�B


### �{�������n (����Node.js)

**Scheme:** `file://`

```js
const model = await tf.loadLayersModel('file://path/to/my-model/model.json');
```

���s��Node.js��C��Ȓ��ڕ����n�󊎘��ߗ����͌^�B���ӁC�ݏ�ʓI�����p���C����pmodel.json�����{�g�i���ݕۑ��C��w��꘢�����j�B���I`.bin`�������v�a`json` �����ݓ��꘢�������B

## �g�p IOHandlers ���͌^

�@�ʏ�q���Ėv�L���I�����C�Ȏg�p`IOHandler`�s����I���s�BTensorflow.js�I`IOHandler`�񋟗�[`tf.io.browserFiles`](https://js.tensorflow.org/api/latest/#io.browserFiles) �C�s��p�݊풆�㕶���B�ȍ� [����](https://js.tensorflow.org/api/latest/#io.browserFiles)���ōX���M���B

# �g�p����I IOHandlers �ۑ������͌^

�@�ʏ�q���Ėv�L���I�ۑ��a���͌^�I�����C�Ȓʍs`IOHandler`�ȍs����I���񉻍s�B

`IOHandler`���꘢�ܗL`save` �a `load`���@�I�ہB

`save`�����ڎ�꘢�^[ModelArtifacts](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L165)�ڌ��C�z�I�Q���󊎉�ԉ�꘢���[SaveResult](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L107)�I�ہB

`load`�����v�L�ڎ�Q������ԉ�꘢���[ModelArtifacts](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L165)�I�ہB�a`save`�I�����ہB


��[BrowserHTTPRequest](https://github.com/tensorflow/tfjs-core/blob/master/src/io/browser_http.ts)��@���sIOHandler�I��q�B
