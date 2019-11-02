# �p�� Keras �p�g�p�I TensorFlow.js layers API

TensorFlow.js �ILayers API��Keras�͌^�B�l�� JavaScript �a Python �V�I���C��w�͎g[Layers API](https://js.tensorflow.org/api/latest/) �^Keras ���B��L�g�pPythonKeras�͌^�I�p�ȍX���n���ڈړ� JavaScript���ITensorFlow.js Layers�B��@�C�ȉ� Keras �� JavaScript�F

```python
# Python:
import keras
import numpy as np

# ������͌^.
model = keras.Sequential()
model.add(keras.layers.Dense(units=1, input_shape=[1]))
model.compile(optimizer='sgd', loss='mean_squared_error')

# �����ꍱ�p���I����.
xs = np.array([[1], [2], [3], [4]])
ys = np.array([[1], [3], [5], [7]])

# �p fit() �͌^.
model.fit(xs, ys, epochs=1000)

# �p predict() ����.
print(model.predict(np.array([[5]])))
```

```js
// JavaScript:
import * as tf from '@tensorlowjs/tfjs';

// ������͌^.
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

// �����ꍱ�p���I����.
const xs = tf.tensor2d([[1], [2], [3], [4]], [4, 1]);
const ys = tf.tensor2d([[1], [3], [5], [7]], [4, 1]);

// �p fit() �͌^.
await model.fit(xs, ys, {epochs: 1000});

// �p predict() ����.
model.predict(tf.tensor2d([[5]], [1, 1])).print();
```

�A���C���]�ݖ{������������ꍱ���B��U���𗹍����y���w�@�I��{�����C���I������Python �ړ�JavaScript�i�������ځj��ꑊ���I�́B

## �������� JavaScript �ۍ�z�u

���ʎ��ᒆ�I�ȉ� Python �a JavaScript ��F���s�����꘢[�S��](https://keras.io/layers/core/#dense)�B

```python
# Python:
keras.layers.Dense(units=1, inputShape=[1])
```

```js
// JavaScript:
tf.layers.dense({units: 1, inputShape: [1]});
```

JavaScript������Python �������v�L�����I���Q���B���]��ƍ� JavaScript ����������ʒu�Q���C���a�g�p��L��ʎ��Q���I�������i�@[LSTM](https://keras.io/layers/recurrent/#lstm)�ޑ��� �B�A����g�pJavaScript �z�u�ۓI�����B���ے񋟗^Python���Q�������I�ʒu�s���a�����B

Model �I�ꍱ���@�i��@�C[`Model.compile()`](https://keras.io/models/model/#model-class-api)�j�珫 JavaScript �z�u�ۍ���B�A���C�Z Model.fit()�AModel.evaluate() �a Model.predict() ���L�s���B�������@���� x�ifeature �����j�a y�ilabel �� target �ځj��������Gx �a y ���^�@�z�u�ە��I�ʒu�Q���C�������Q���B��@�F


## Model.fit()���I

`Model.fit()` ���p��Tensorflow.js���s�͌^�I��v���@�B�����@�������s�I�i�����b�������j�B�����C�䗘�p��JavaScript���I�g�h�����B���ȍ݊풆�s�C�g�p�������A�s��j�ǎ�UI���B�aJavaScript�������\���s�I�������C��@`async`[��](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)�B���v����`async`���꘢��python���s���ݓI���B��[`fit()`](https://keras.io/models/model/#model-class-api)���@��keras���ԉ�꘢�j��, ��JavaScript��`fit()`���@�I�ԉ�꘢��܎j�I[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)������[await(����)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)�C��ȗ^then()���@��N�g�p�B


## TensorFlow.js ���v�L NumPy

Python Keras �p��g�p[NumPy](http://www.numpy.org/)���s��{�I���a���I����C��@�ݏ�ʓI���ᒆ���� 2D �ʁB

```python
# Python:
xs = np.array([[1], [2], [3], [4]])
```

�� TensorFlow.js ���C��{�I�����I���쐥�g�p��{�g�����I�B��@�F

```js
// JavaScript:
const xs = tf.tensor2d([[1], [2], [3], [4]], [4, 1]);
```

 tf.* ������񋟐��a���㐔�Ioperations�i����j�C�@�阩�@�B�L�X���M���C�Q [TensorFlow.js�j�S����](https://js.tensorflow.org/api/latest/)�B

## �g�pfactory(�H��)���@�C���s��������

Python ���I��s�i������ʓI��q�j���꘢�������p�F

```python
# Python:
model = keras.Sequential()
```

�@�ʊi JavaScript�C�����������p���@�������F

```js
// JavaScript:
const model = new tf.Sequential();  // �s�I �v�I �I �I ��I 
```

�R���C��r��s�g�p�gnew�h�������C�� 1)�gnew�h����g��X���c�G2)�gnew�h�������� JavaScript �I�gbad part�h�F�꘢���ݓI蜁C�@��[*JavaScript: the Good Parts*](http://archive.oreilly.com/pub/a/javascript/excerpts/javascript-good-parts/bad-parts.html).���I���B�v�� TensorFlow.js �����͌^�a Layer �C�ȗp��� lowerCamelCase�i���������j�I�H�ʕ��@�C��@�F

```js
// JavaScript:
const model = tf.sequential();

const layer = tf.layers.batchNormalization({axis: 1});
```

## ���������������C���s�� snake_case

�� JavaScript ���C�^ Python ����C�X��I���g�p����아�����́i��@�C[Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html#naming-camel-case-defined)�j�C�� Python �� snake_case �k��i��@�C�� Keras ���j�B�����C��r��g�p����������I�������C��ȉ����e�F

* DataFormat�C��@�CchannelsFirst ���s�� channels_first
* Initializer�C��@�CglorotNormal ���s�� glorot_normal
* Loss and metrics�C��@�CmeanSquaredError ���s�� mean_squared_error�CcategoricalCrossentropy ���s�� categorical_crossentropy�B

��@�C�@��Ꮚ���F

```js
// JavaScript:
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});
```

���͌^���񉻘a�����񉻁C���S�B���S�BTensorFlow.js �I���������ې��� JSON �ے��I snake_case �C��@�C�� Python Keras ���͌^�B


## �g�p apply() �s Layer �ہC���s�������씟���p

�� Keras ���CLayer �ے藹`__call__`���@�B�����C�p�Ȓʏ��ۍ씟���p���p Layer �I�C��@:

```python
# Python:
my_input = keras.Input(shape=[2, 4])
flatten = keras.layers.Flatten()

print(flatten(my_input).shape)
```

�� Python �@���� TensorFlow.js ���� apply() ���@�F

```js
// JavaScript:
const myInput = tf.input{shape: [2, 4]});
const flatten = tf.layers.flatten();

console.log(flatten.apply(myInput).shape);
```

## Layer.apply() �x����� Tensor�i�ʁj�I���ߎ��iEager�j�s

�ڑO�C�� Keras ���C`__call__`���@���\�iPython�jTensorFlow �I `tf.Tensor` �ۍs����i�� TensorFlow ���@�[�j�C���ې��������I�󊎕s��ܓI���B�A����ꒆ�I���ᒆ�����I���e�B�A���C�� TensorFlow.js ���CLayer �I  `apply()` ���@�ȍݕ����a���ߖ͎����s�B�@�ʗp SymbolicTensor �p `apply()`�i���� tf.Tensor�j�p�C�ԉ� SymbolicTensor�B�ʏ퐶�ݖ͌^�����B�A���@�ʗp�I��� Tensor�i�ʁj�p  `apply()`�C���ԉ�꘢��̓I Tensor�i�ʁj�B��@�F

```js
// JavaScript:
const flatten = tf.layers.flatten();

flatten.apply(tf.ones([2, 3, 4])).print();
```

�������l�z���iPython�jTensorFlow �I[Eager Execution](https://www.tensorflow.org/guide/eager)�B���ݖ͌^���񋟗��X��I���ݐ��a���C�󊎐��_㤑ŗ���B

## Optimizers�i����j�� train.* ���C���s�� optimizers.*

�� Keras ���COptimizer�i����j�ۓI�������ʘ� keras.optimizers.* �����󉺁B�� TensorFlow.js Layer ���COptimizer�i����j�I�H�ʕ��@�ʘ� tf.train.* �����󉺁B��@�F

```python
# Python:
my_sgd = keras.optimizers.sgd(lr=0.2)
```

```js
// JavaScript:
const mySGD = tf.train.sgd({lr: 0.2});
```

## loadLayersModel() �� URL ���C���s�� HDF5 ����

�� Keras ���C�͌^�ʏ�[�ۑ�](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model) HDF5�i.h5�j�����C�R�@�Ȏg�p `keras.models.load_model()`���@�� �B���@�їp .h5 �����I�H�a�BTensorFlow.js ���I load_model() �I��[`tf.loadLayersModel()`](https://js.tensorflow.org/api/latest/#loadLayersModel)�B�R�� HDF5 �����i�����s�F�D�C���� tf.loadLayersModel() �їp TensorFlow.js ����I�i���Btf.lloadLayersModel() �� model.json �����쑴���Q���B�Ȏg�p tensorflowjs �I pip � Keras HDF5 ���� model.json�B

```js
// JavaScript:
const model = await tf.loadLayersModel('https://foo.bar/model.json');
```

�v���ӓI��`tf.loadLayersModel()`�ԉ�I��[`tf.Model`](https://js.tensorflow.org/api/latest/#class:Model)�I[��`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)�B

�ʏ�Ctf.Model�� TensorFlow.js���ۑ��a�����g�p`tf.Model.save`�a`tf.loadLayersModel`���@�B�䏫�� API ����Keras[the save and load_model API](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)�B�A���틫�^ Keras ����v�[�x�w�y�ˍs�I�@�[�����S�s���C�����p�����v���a�����I�H�R�����B�����CTensorFlow.js �a Keras ���I save/load API �V���݈ꍱ�L��I���B�L�X���M���C�Q�䘰 [�ۑ��a��tf.Model](./save_load.md)�I�����B

## �p`fitDataset()`�͌^�g�p`tf.data.Dataset`��

��python�Ŗ{�Itensorflow keras���C �꘢�͌^�Ȏg�p[Dataset](https://www.tensorflow.org/guide/datasets)�ۍs�B�͌^�I`fit()`���@���ڐڎ�I�ہB�꘢Tensorflow.js���@�Ȏg�p������Dataset�ۓIJavascript�s�C[TensorFlow.js�Itf.data API����](https://js.tensorflow.org/api/latest/#Data)�B�R���C�^python�s���C �Dataset�I���ʈ꘢�I���@�������I�����@�̔V[fitDataset](https://js.tensorflow.org/api/0.15.1/#tf.Model.fitDataset)�B[fit()](https://js.tensorflow.org/api/latest/#tf.Model.fitDataset) ���Tensor(��)�I�͌^�B

## Layer()�ۘaModel(�͌^)�ۓI�����Ǘ�

TensorFlow.js�݊풆�IWebGL��s�C�����a�͌^�ۓI�d�RWebGL���x���B�R��WebGL��s�x�����u�I���W�B�ݐ����a�I�����CLayer()�aModel(�͌^)�ۗp�ݓ����Ǘ�Tensor(��)�����B�A�������p�������ȕ�����p�IWebGL�����B���݉��������a�����͌^��I��v�k�L�p�B�z�v�����꘢Layer()�aModel(�͌^)�ہC�g�p`dispose()` ���@�B
