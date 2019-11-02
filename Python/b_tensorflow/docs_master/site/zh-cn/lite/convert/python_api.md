# �͌^��iConverter�j�I Python API �w��

���ʒ񋟗��꘢���� TensorFlow 2.0 ���@���g�p 
[TensorFlow Lite ��iTensorFlow Lite converter�j](index.md) Python API �I����B

[TOC]

## Python API

�� TensorFlow 2.0 ���C�p�������n�I TensorFlow �͌^�i�� TensorFlow Lite �I Python API �� `tf.lite.TFLiteConverter`�B�� `TFLiteConverter` ���L�ȉ��I���@�iclassmethod�j�F

*   `TFLiteConverter.from_saved_model()`�F�p��
    [SavedModel �i���͌^](https://www.tensorflow.org/guide/saved_model)�B
*   `TFLiteConverter.from_keras_model()`�F�p��
    [`tf.keras` �͌^](https://www.tensorflow.org/guide/keras/overview)�B
*   `TFLiteConverter.from_concrete_functions()`�F�p��
    [concrete functions](concrete_function.md)�B

����: �� TensorFlow Lite 2.0 ���L�꘢�s���Ŗ{�I
`TFLiteConverter` API�C  API ����ܗ�
[`from_concrete_function`](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/lite/TFLiteConverter#from_concrete_function)�B
�{�����p���I�I�V�Ŗ{ API �Ȓ� pip ����
[`tf-nightly-2.0-preview`](#2.0-nightly)�B

�{���W���� API �I [����p�@](#examples)�C�s�� TensorFlow �Ŗ{�I API ��\�� [1.X �Ŗ{�� 2.0 �Ŗ{ API �I��](#differences)�C�a
[���� TensorFlow](#versioning) �������a�g�p�B

## ���� <a name="examples"></a>

###  SavedModel �i���͌^ <a name="saved_model"></a>

�ȉ�����W�����@�����꘢
[SavedModel](https://www.tensorflow.org/guide/saved_model) 
TensorFlow Lite ���I [`FlatBuffer`](https://google.github.io/flatbuffers/)�i���B

```python
import tensorflow as tf

# �����꘢�I�͌^�B
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# �ۑ��͌^�B
export_dir = "/tmp/test_saved_model"
input_data = tf.constant(1., shape=[1, 1])
to_save = root.f.get_concrete_function(input_data)
tf.saved_model.save(root, export_dir, to_save)

# �͌^�B
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert()
```

�� API �s�x���w������ʓI�x�B �@�ʓI�͌^���v�w������ʓI�x�C�g�p
[`from_concrete_functions`](#concrete_function) �������B ����F

```python
model = tf.saved_model.load(export_dir)
concrete_func = model.signatures[
  tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
concrete_func.inputs[0].set_shape([1, 256, 256, 3])
converter = TFLiteConverter.from_concrete_functions([concrete_func])
```

###  Keras �͌^ <a name="keras"></a>

�ȉ�����W�����@�����꘢
[tf.keras �͌^](https://www.tensorflow.org/guide/keras/overview) 
TensorFlow Lite ���I [`FlatBuffer`](https://google.github.io/flatbuffers/) �i���B

```python
import tensorflow as tf

# ���꘢�I Keras �͌^�B
x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]

model = tf.keras.models.Sequential(
    [tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=50)

# �͌^�B
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

###  concrete function <a name="concrete_function"></a>

�ȉ�����W�����@���� TensorFlow ���I
[concrete function](concrete_function.md) TensorFlow Lite ���I
[`FlatBuffer`](https://google.github.io/flatbuffers/) �i���B

```python
import tensorflow as tf

# �����꘢�͌^�B
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# ���� concrete function�B
input_data = tf.constant(1., shape=[1, 1])
concrete_func = root.f.get_concrete_function(input_data)

# �͌^�B
#
# `from_concrete_function` �I���Q����꘢�꘢ concrete function �I��\�C�R��
# �i�x�����p�ڎ�꘢concrete function�B
# ������concrete function�I���\���ݒ��B
converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_func])
tflite_model = converter.convert()
```

### �[���[ MobileNet  <a name="mobilenet"></a>

�ȉ�����W�����@�������꘢��O�D�I 
`tf.keras` MobileNet �͌^ TensorFlow Lite �x���I�^��s���f �iinference�j�B ������������
TensorFlow �a TensorFlow Lite �͌^���s�I�ʏ����B�@�ʐ����������͌^�C�g�p `model_path` ����� `model_content`�B

```python
import numpy as np
import tensorflow as tf

# �� MobileNet tf.keras �͌^�B
model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(224, 224, 3))

# �͌^�B
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# �� TFLite �͌^�󕪔z�ʁitensor�j�B
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# ����a�o�ʁB
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# �g�p����������� TensorFlow Lite �͌^�B
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# ���� `get_tensor()` ��ԉ��ʓI���B
# �g�p `tensor()` ��w���ʓI�w�B
tflite_results = interpreter.get_tensor(output_details[0]['index'])

# �g�p����������� TensorFlow �͌^�B
tf_results = model(tf.constant(input_data))

# ��ʁB
for tf_result, tflite_result in zip(tf_results, tflite_results):
  np.testing.assert_almost_equal(tf_result, tflite_result, decimal=5)
```

##  1.X �Ŗ{�� 2.0 �Ŗ{ API �I�� <a name="differences"></a>

�{���� 1.X �� 2.0 �Ŗ{ Python API �I���B
�@�ʖ^�����L�C���
[GitHub issue](https://github.com/tensorflow/tensorflow/issues)�B

### `TFLite��` �x���I�i���^

`TFLite��` �� 2.0 �Ŗ{���x���R 1.X �Ŗ{�a 2.0 �Ŗ{�����I SavedModels �a Keras �͌^�B�A���C���s�Ďx���R
1.X �Ŗ{�I `GraphDefs`�B �҉ʗp `tf.compat.v1.lite.TFLiteConverter` ���c�I
`GraphDefs` �� TensorFlow Lite �Ŗ{�B

### �ʉ����m�iQuantization-aware training�j

�ȉ��^
[�ʉ����m�iQuantization-aware training�j](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/quantize)
�L�I�����a���@�� TensorFlow 2.0 ����`TFLiteConverter` ����ڏ��B

*   `inference_type`
*   `inference_input_type`
*   `quantized_input_stats`
*   `default_ranges_stats`
*   `reorder_across_fake_quant`
*   `change_concat_input_ranges`
*   `post_training_quantize` - �� 1.X API ����P�p
*   `get_input_arrays()`

�x���ʉ����m�I�d�ʊ�irewriter�j�����s�x���R TensorFlow 2.0 �����I�͌^�B���O�CTensorFlow Lite �I�ʉ� API
�߈x�� Keras ���ʉ����m API �I�v�H�d�V�a���B �ݐV�I�ʉ� API �����O�C���������s��o�� 2.0 �I API ���B�҉Ȏg�p
`tf.compat.v1.lite.TFLiteConverter` ���R�d�ʊ픟�������I�͌^�B

### �� `TFLiteConverter` �������I��

���� `target_ops` �ߐ� `TargetSpec` ���I�������얢�����y�˓I�[��d���� `supported_ops`�B

���O�C�ȉ�������ڏ�:

*   `drop_control_dependency` (default: `True`) - TFLite �s�x���T�����icontrol flow�j�C���ȍ��������P `True`�B
*   _Graph visualization_ - �� TensorFlow 2.0 ���C��䦎g�p
    [visualize.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py)  TensorFlow Lite �igraph�j�I���B
    �s���� GraphViz, ���x���қߍs post training �ʉ��I�igraph�j���B�ȉ��^���I��������ڏ��F
    *   `output_format`
    *   `dump_graphviz_dir`
    *   `dump_graphviz_video`

### �ʗp API �I��

#### ���@

�ȉ��� 1.X ����P�p�I���@�s��� 2.0 ���o�F

*   `lite.toco_convert`
*   `lite.TocoConverter`

#### `lite.constants`

�� 2.0 ���C���� TensorFlow �a TensorFlow Lite �V�I�d�ڏ��� `lite.constants` API�B�ȉ��I��\�W����
`lite.constant` ���I�^�� TensorFlow ���I�^�F

*   `lite.constants.FLOAT`: `tf.float32`
*   `lite.constants.INT8`: `tf.int8`
*   `lite.constants.INT32`: `tf.int32`
*   `lite.constants.INT64`: `tf.int64`
*   `lite.constants.STRING`: `tf.string`
*   `lite.constants.QUANTIZED_UINT8`: `tf.uint8`

���O�C`lite.constants.TFLITE` �a `lite.constants.GRAPHVIZ_DOT` ��ڏ��i�R�� `TFLiteConverter` ���I flage `output_format`��ڏ��j�B

#### `lite.OpHint`

�R�� API `OpHint` �^ 2.0 �I API �s���e�C�̕s�p�B �� API�p��� LSTM �I�͌^�B �� 2.0 ��
LSTMs �I�x�����ݔ�T���B���L�^ `lite.experimental` �L�I API �s������ڏ��B

## ���� TensorFlow <a name="versioning"></a>

### ���� TensorFlow 2.0 nightly <a name="2.0-nightly"></a>

�p�ȉ����߈��� TensorFlow 2.0 nightly�F

```
pip install tf-nightly-2.0-preview
```

### �ݛ߈����I 1.X ���g�p TensorFlow 2.0 <a name="use-2.0-from-1.X"></a>

�ʈȉ���Вi���ŋ߈����I 1.X ���g�p TensorFlow 2.0�B

```python
import tensorflow.compat.v2 as tf

tf.enable_v2_behavior()
```

### ��������� <a name="latest_package"></a>

�g�p�ŐV�Ŗ{�I TensorFlow Lite �� Python API�C
�ʈȉ��������� nightly build�F
[pip](https://www.tensorflow.org/install/pip) (��䦕���) ��
[Docker](https://www.tensorflow.org/install/docker), ��
[�����㌚ pip ��](https://www.tensorflow.org/install/source).
