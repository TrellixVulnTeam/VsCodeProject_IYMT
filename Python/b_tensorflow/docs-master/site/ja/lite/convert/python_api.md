# �R���o�[�^ Python API �K�C�h

���̃y�[�W�ł́ATensorFlow 2.0 �� Python API �ɂ�� [TensorFlow Lite �R���o�[�^](index.md) �̎g�p���������܂��B

[TOC]

## Python API

TensorFlow 2.0 �ɂ����āATensorFlow ���f���� TensorFlow Lite �ɕϊ����� Python API �� `tf.lite.TFLiteConverter` �ł��B
 `TFLiteConverter` �ɂ́A���̃��f���t�H�[�}�b�g�Ɋ�Â��ă��f����ϊ�����ȉ��̃N���X���\�b�h������܂��F

*   `TFLiteConverter.from_saved_model()`: 
    [SavedModel �f�B���N�g��](https://www.tensorflow.org/guide/saved_model) ��ϊ����܂��B
*   `TFLiteConverter.from_keras_model()`: 
    [`tf.keras` ���f��](https://www.tensorflow.org/guide/keras/overview) ��ϊ����܂��B
*   `TFLiteConverter.from_concrete_functions()`: 
    [��ۊ֐�](concrete_function.md) ��ϊ����܂��B

Node: TensorFlow Lite 2.0 alpha �ɂ́A [`from_concrete_function`](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/lite/TFLiteConverter#from_concrete_function) �������܂ނ悤�ȁA�قȂ�o�[�W������ `TFLiteConverter` API ������܂��B
���̃h�L�������g�ŋL�q����Ă��� API �́A[`tf-nightly-2.0-preview`](#installing_the_tensorflow_20_nightly_) �� PIP �ŃC���X�g�[�����邱�ƂŎg����悤�ɂȂ�܂��B


���̃h�L�������g�ł� API �� [�g�p��](��examples) �A [1.X �� 2.0 �̊Ԃ� API �̕ύX�_�̏ڍׂȃ��X�g](#differences) �A �قȂ�o�[�W������ TensorFlow �Ŏ��s���� [���@](#versioning) ���܂݂܂��B

## �� <a name="examples"></a>

### SavedModel ��ϊ����� <a name="saved_model"></a>

�ȉ��̗�� [SavedModel](https://www.tensorflow.org/guide/saved_model) �� TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) �ɕϊ�������@�������Ă��܂��B

```python
import tensorflow as tf

# ��{�I�Ȋ֐����\�z
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# ���f����ۑ�
export_dir = "/tmp/test_saved_model"
input_data = tf.constant(1., shape=[1, 1])
to_save = root.f.get_concrete_function(input_data)
tf.saved_model.save(root, export_dir, to_save)

# ���f����ϊ�
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert()
```

### Keras ���f����ϊ����� <a name="keras"></a>

�ȉ��̗�� [`tf.keras` ���f��](https://www.tensorflow.org/guide/keras/overview) �� TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) �ɕϊ�������@�������Ă��܂�.


```python
import tensorflow as tf

# �V���v���� Keras ���f�����\�z
x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]

model = tf.keras.models.Sequential(
    [tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=50)

# ���f����ϊ�
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

### ��ۊ֐���ϊ����� <a name="concrete_function"></a>

�ȉ��̗�� TensorFlow ��[��ۊ֐�](concrete_function.md)�� TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) �ɕϊ�������@�������Ă��܂��B


```python
import tensorflow as tf

# ��{�I�Ȋ֐����\�z
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# ��ۊ֐��𐶐�
input_data = tf.constant(1., shape=[1, 1])
concrete_func = root.f.get_concrete_function(input_data)

# ���f����ϊ�
#
# `from_concrete_function` �͋�ۊ֐��̃��X�g�������Ɏ��܂����A
# ���݂̂Ƃ����1�̊֐��݂̂��T�|�[�g���Ă��܂��B �����֐��̕ϊ��͊J�����ł�
converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_func])
tflite_model = converter.convert()
```

### End-to-end �� MobileNet �̕ϊ� <a name="mobilenet"></a>

�ȉ��̗�́A�P���ς݂� `tf.keras` MobileNet ���f���� TensorFlow Lite �ɕϊ����Ď��s������@�������Ă��܂��B
�܂��A ���� TensorFlow ���f���� TensorFlow Lite ���f���̌��ʂ������_���f�[�^�Ŕ�r���Ă��܂��B
���f�����t�@�C�����烍�[�h���邽�߂ɁA `model_content` �̑���� ` model_path` ���g�p���܂��B


```python
import numpy as np
import tensorflow as tf

# MobileNet tf.keras ���f�������[�h
model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(224, 224, 3))

# ���f����ϊ�
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# TFLite ���f����ϊ����A�e���\���������Ă�
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# ���o�̓e���\�����擾
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# TensorFlow Lite ���f���������_���ȓ��̓f�[�^�Ńe�X�g
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
# `get_tensor()` �̓e���\���̃R�s�[��Ԃ�
# �e���\���̃|�C���^���擾�������ꍇ�� `tensor()` ���g�� 
tflite_results = interpreter.get_tensor(output_details[0]['index'])

# ���� TensorFlow ���f���������_���ȓ��̓f�[�^�Ńe�X�g
tf_results = model(tf.constant(input_data))

# ���ʂ��r
for tf_result, tflite_result in zip(tf_results, tflite_results):
  np.testing.assert_almost_equal(tf_result, tflite_result, decimal=5)
```

## 1.X ���� 2.0 �ւ� Python API �̕ύX�_�܂Ƃ� <a name="differences"></a>

�ȍ~�̏͂ł́APython API �� 1.X ���� 2.0 �ւ̕ύX�_�ɂ��Ă܂Ƃ߂Ă��܂����A
�����Ȃɂ����O���������ꍇ�� GitHub �� [issue](https://github.com/tensorflow/tensorflow/issues) ���o���Ă��������B

### `TFLiteConverter` �̃T�|�[�g���Ă���t�H�[�}�b�g

2.0�� `TFLiteConverter` �� 1.X �� 2.0 �Ő������ꂽ SavedModel �� Keras
���f���t�@�C�����T�|�[�g���܂����A1.X �Ő������ꂽ frozen `GraphDefs` �̓T�|�[�g���܂���B frozen `GraphDefs` ��
TensorFlow Lite �ɕϊ��������ꍇ�� `tf.compat.v1.lite.TFLiteConverter` ���g���K�v������܂��B

### Quantization-aware training

[quantization-aware training](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/quantize) �Ɋ֘A����ȉ��̑����ƃ��\�b�h�́A TensorFlow 2.0 �� `TFLiteConverter` ����폜����܂���:


*   `inference_type`
*   `inference_input_type`
*   `quantized_input_stats`
*   `default_ranges_stats`
*   `reorder_across_fake_quant`
*   `change_concat_input_ranges`
*   `post_training_quantize` - 1.X API �Ŕ񐄏�
*   `get_input_arrays()`

quantization-aware training ���T�|�[�g���Ă����v�Z�O���t�̏��������֐��́ATensorFlow
2.0�ɂ�郂�f�����T�|�[�g���܂���B �܂��ATensorFlow Lite �� quantization API �́AKeras API ��ʂ���
quantization-aware training ���T�|�[�g��������ō�蒼���ƍ����������߂Ă���Œ��ł��B �V���� quantization API
�����[���`�����܂ł́A�����̑����� 2.0 API ����폜����܂��B ���������֐��ɂ���ă��f����ϊ��������ꍇ��
`tf.compat.v1.lite.TFLiteConverter` ���g���Ă��������B

### `TFLiteConverter` �̑����ɑ΂���ύX�_

`target_ops` ������ `TargetSpec` �̑����ƂȂ�A�����ǉ������\��̍œK���t���[�����[�N�ɍ��킹�� `supported_ops` �Ƀ��l�[������܂����B
�܂��A�ȉ��̑������폜����Ă��܂�:

*   `drop_control_dependency` (default: `True`) - ���݂̂Ƃ���R���g���[���t���[�� TFLite �ŃT�|�[�g����Ă��Ȃ��̂ŁA��� `True` �ł��B
*   _Graph visualization_ - TensorFlow 2.0 �ɂ����āA TensorFlow Lite �O���t�̉����Ő��������̂� [visualize.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py) ���g�����Ƃł��B GraphViz �ƈႢ�A post training quantization ���{���ꂽ��̃O���t�������ł��܂��B �܂��A�O���t�̉����Ɋւ���ȉ��̑����͍폜�����\��ł�:
    *   `output_format`
    *   `dump_graphviz_dir`
    *   `dump_graphviz_video`

### ��ʓI�� API �ɑ΂���ύX�_

#### �ϊ����@

1.X �Ŋ��ɔ񐄏��ƂȂ��Ă����ȉ��̃��\�b�h�́A 2.0 �ł͍폜����Ă��܂�:

*   `lite.toco_convert`
*   `lite.TocoConverter`

#### `lite.constants`

`lite.constants` API �́A TensorFlow �� TensorFlow Lite �̊Ԃ̏d�������炷���߂� 2.0 �ō폜����܂����B
`lite.constant` �̌^�� TensorFlow �̌^�̑Ή��͈ȉ��̂Ƃ���ł��B

*   `lite.constants.FLOAT`: `tf.float32`
*   `lite.constants.INT8`: `tf.int8`
*   `lite.constants.INT32`: `tf.int32`
*   `lite.constants.INT64`: `tf.int64`
*   `lite.constants.STRING`: `tf.string`
*   `lite.constants.QUANTIZED_UINT8`: `tf.uint8`

�܂��A`lite.constants.TFLITE` �� `lite.constants.GRAPHVIZ_DOT` �́A `TFLiteConverter` �� `output_format` �̔p�~�ɔ����폜����܂����B

#### `lite.OpHint`

`OpHint` API �́A2.0 API �Ƃ̌݊������Ȃ����߁A���� 2.0 �ł͗��p�ł��܂���B
���� API �� LSTM �x�[�X�̃��f���̕ϊ����\�ɂ�����̂ł����A2.0 �ɂ����� LSTM �̃T�|�[�g�͌��ؒ��̂��߁A�֘A���� `lite.experimental` API �͂��ׂč폜����Ă��܂��B

## TensorFlow �̃C���X�g�[�� <a name="versioning"></a>

### TensorFlow 2.0 nightly �̃C���X�g�[�� <a name="2.0-nightly"></a>

TensorFlow 2.0 nightly �͈ȉ��̃R�}���h�ŃC���X�g�[���ł��܂�:

```
pip install tf-nightly-2.0-preview
```

### �C���X�g�[���ς� TensorFlow 1.X ���� 2.0 ���g�� <a name="use-2.0-from-1.X"></a>

TensorFlow 2.0 �́A�ŋ߂� 1.X ����ȉ��̂悤�ɂ��ė��p�ł��܂��B

```python
import tensorflow.compat.v2 as tf

tf.enable_v2_behavior()
```

### �\�[�X�R�[�h����̃r���h <a name="latest_package"></a>

TensorFlow Lite �R���o�[�^ Python API �̍ŐV�o�[�W���������s����ɂ́A [pip](https://www.tensorflow.org/install/pip) (����) �܂��� [Docker](https://www.tensorflow.org/install/docker) ���g�p���ăi�C�g���[�r���h���C���X�g�[�����邩�A[�\�[�X���� pip �p�b�P�[�W���r���h](https://www.tensorflow.org/install/source) ���Ă��������B
