# ��Keras�͌^��Tensorflow.js

Keras�͌^�i�ʏ��Python API���j�\��ۑ���[���i���V��](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model). �����͌^�i���Ȕ�Tensorflow.js�I(Layer)�i���C���i���Ȕ���󒼐ڗp��Tensorflow.js�I���f������I�B

�@�ITensorFlow.js(Layer)�i�����꘢���model.json�����a��񐧊i���I���Џd�����I�ځB model.json������ܖ͌^��i�����g��(architecture)�h���g�`(graph)�h�F����(Layer)�y���ڕ����I�`�q�j�a�d�����I���B

## �v��

���v��Python�I�����C�\���v�Ɨ��I�g�p[pipenv](https://github.com/pypa/pipenv)����[virtualenv](https://virtualenv.pypa.io)�B��g�p `pip install tensorflowjs`������

��Keras�͌^��Tensorflow.js���v���B���C���ߗLKeras�͌^��TF.js(Layer)�i���C�R�@������Tensorflow.js�B

## Step 1. ���ߗLKeras�͌^��TF.js(Layer)�i��

Keras�͌^�ʏ�� `model.save(filepath)`�s�ۑ��C���꘢���ܗL�͌^��ȋy�d�IHDF5(.h5)�����B�@���v�꘢������TF.js�i���C�ȍs�ȉ���B���I`path/to/my_model.h5`Keras .h5�����n���C��`path/to/tfjs_target_dir`���o�ITF.js�ځB

```sh
# bash

tensorflowjs_converter --input_format keras \
                       path/to/my_model.h5 \
                       path/to/tfjs_target_dir
```

## �����: �g�p Python API ���ڏo TF.js (Layer)�i��

�@�ʗL�꘢Python�IKeras�͌^�C�ȗp�ȉ����@���ڏo�꘢Tensoflow.js(Layers)�i��:


```py
# Python

import tensorflowjs as tfjs

def train(...):
    model = keras.models.Sequential()   # for example
    ...
    model.compile(...)
    model.fit(...)
    tfjs.converters.save_keras_model(model, tfjs_target_dir)
```

## Step 2: ���͌^��Tensorflow.js

�g�p�꘢web�����1�������I�@�I�͌^�����񋟕��B���ӁC�\���v���I����z�u[��׌�������(CORS)](https://enable-cors.org/), �Ȉ�� JavaScript ����敶���B

�R�@�ʒ�model.json�����IURL���͌^����TensorFlow.js���F


```js
// JavaScript

import * as tf from '@tensorflow/tfjs';

const model = await tf.loadLayersModel('https://foo.bar/tfjs_artifacts/model.json');
```

�݁C�͌^�ߏy�D�s����(inference)�C��(evaluation)���d�V(re-training)�B��@�C�͌^�������@�ȗ����s(predict)�F


```js
// JavaScript

const example = tf.fromPixels(webcamElement);  // for example
const prediction = model.predict(example);
```

�k��[Tensorflow.js��](https://github.com/tensorflow/tfjs-examples)�їp���@�C�g�p�ߍ� Google �]����a��ǓI�͌^�B

���ӁC�g�p`model.json`���������p�����͌^�B`loadModel(...)` �� `model.json`�C�󊎒ʊO�IHTTP(S)���Ȏ�`model.json`�d�������p�I���Џd�����B �����@��폫�������S����(�\�푶�݌�㤏㑴�������풆)�B���� `model.json`�a�d���s�����T�^�I�������召�����B�������͌^�\�ݐ��@�I�i�����n�X���B


## �ߎx���I����

TensorFlow.js�I(Layers)�ڑO�x����yKeras�IKeras�͌^�B �g�p�s�x���I����(ops)��(layers)�I�͌^ - ��@ ����CLambda�C���莸(loss)������w(metrics)�ٖ@�����C�����˘��ٖ@����ϒnJavaScript�IPython��B
