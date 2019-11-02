# Python API �w��

�{�񋟗��ꍱ���ᗈ���@���� Python API �p TensorFlow Lite ��C�ȋy����B

���� : �{����I�� Tensorflow nightly �Ŗ{�I��C �s `pip install tf-nightly` �������Ŗ{�B
���ŕ����Q�l[�g TensorFlow 1.12 �y�V�O�Ŗ{�I�͌^�h](#pre_tensorflow_1.12)�B

[TOC]

  
## �T�q

�R��ȍݖ��ߍs���p TensorFlow Lite ��C�A�p Python �r�{�p API �I�����ȍ�͌^���� (model development pipeline) �I��C�ʏ��X���֏��G�ȍX���I���𐳍ݓI�͌^���ۈ�

## API

`tf.lite.TFLiteConverter`�F�p���� TensorFlow �͌^ TensorFlow Lite �I API�B 
`tf.lite.Interpreter`�F�p���p Python ����I API�B

�s���I�͌^���n�i���C`TFLiteConverter` �񋟗����p���I���@�B
`TFLiteConverter.from_session()` �p�� GraphDefs�B
`TFLiteConverter.from_saved_model()` �p�� SavedModels�B
`TFLiteConverter.from_keras_model_file()` �p�� `tf.Keras` �����B
[��{����](#basic) �W�����_�͌^�I�p�@�B[����](#complex) �W���X�I�͌^�p�@�B

## ��{���� <a name="basic"></a>

�ȉ����������@���c��{���_�͌^���e���n�����i���� TensorFlow Lite FlatBuffers�B

### �g�p tf.Session �o GraphDef <a name="basic_graphdef_sess"></a>

�ȉ�����W�����@���� `tf.Session` �ۈ꘢ TensorFlow GraphDef �� TensorFlow Lite FlatBuffer�B

```python
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
var = tf.get_variable("weights", dtype=tf.float32, shape=(1, 64, 64, 3))
val = img + var
out = tf.identity(val, name="out")

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)
```

### �g�p�����o GraphDef <a name="basic_graphdef_file"></a>

�ȉ�����W������ GraphDef �푶�������C�����꘢ TensorFlow GraphDef �� TensorFlow Lite FlatBuffer�B�x�������@ .pb �a .pbtxt�B

���ᒆ�p���I��������F[Mobilenet_1.0_224](https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_1.0_224_frozen.tgz)�B
�������x���p [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py) �I GraphDef�B

```python
import tensorflow as tf

graph_def_file = "/path/to/Downloads/mobilenet_v1_1.0_224/frozen_graph.pb"
input_arrays = ["input"]
output_arrays = ["MobilenetV1/Predictions/Softmax"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

### �o SavedModel <a name="basic_savedmodel"></a>

�ȉ�����W�����@���� SavedModel �� TensorFlow Lite FlatBuffer�B

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

���X�I SavedModel, �� `TFLiteConverter.from_saved_model()` �����Q���F
`input_arrays`�C`input_shapes`�C`output_arrays`�C`tag_set`�C`signature_key`�B
�s `help(tf.lite.TFLiteConverter)` �ŎQ����B

### �o tf.keras ���� <a name="basic_keras_file"></a>

�ȉ�����W���@���� `tf.keras` �͌^�� TensorFlow Lite FlatBuffer�B������v�����[`h5py`](http://docs.h5py.org/en/latest/build.html)

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("keras_model.h5")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

`tf.keras` �����K��ܖ͌^�a�d�B�꘢�S�ʓI��͌^���ݓ��I����@�������F

```python
import numpy as np
import tensorflow as tf

# Generate tf.keras model.
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, input_shape=(3,)))
model.add(tf.keras.layers.RepeatVector(3))
model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(3)))
model.compile(loss=tf.keras.losses.MSE,
              optimizer=tf.keras.optimizers.RMSprop(lr=0.0001),
              metrics=[tf.keras.metrics.categorical_accuracy],
              sample_weight_mode='temporal')

x = np.random.random((1, 3))
y = np.random.random((1, 3, 3))
model.train_on_batch(x, y)
model.predict(x)

# Save tf.keras model in HDF5 format.
keras_file = "keras_model.h5"
tf.keras.models.save_model(model, keras_file)

# Convert to TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_keras_model_file(keras_file)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

## ���� <a name="complex"></a>

�������ҕs���I�͌^�C�ݗp `convert()` �V�O�u�����B
��@�u�C����ʓs���v�g�p `tf.lite.constants.<CONSTANT_NAME>`�C�ȉ����ᒆ�g�p����� `QUANTIZED_UINT8`�B
�ȍ� Python �[���s `help(tf.lite.TFLiteConverter)` ��L�����I�����B

�s�ǎ��ᒆ����������܏�ʓI GraphDefs�C���I�ȗp����������i���B

### �o�ʉ� GraphDef <a name="complex_quant"></a>

�ȉ�����W�����@���c�ʉ��͌^�� TensorFlow Lite FlatBuffer�B

```python
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
const = tf.constant([1., 2., 3.]) + tf.constant([1., 4., 4.])
val = img + const
out = tf.fake_quant_with_min_max_args(val, min=0., max=1., name="output")

with tf.Session() as sess:
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  converter.inference_type = tf.lite.constants.QUANTIZED_UINT8
  input_arrays = converter.get_input_arrays()
  converter.quantized_input_stats = {input_arrays[0] : (0., 1.)}  # mean, std_dev
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)
```

## TensorFlow Lite Python ���� <a name="interpreter"></a>

### ���͌^�����p���� <a name="interpreter_file"></a>

�ȉ�����W������ TensorFlow Lite FlatBuffer �����@�C�@���g�p TensorFlow Lite Python ����B
���㉉�����@�������������s�����B�ȍ� Python �[���s `help(tf.lite.Interpreter)` �����I�����B

```python
import numpy as np
import tensorflow as tf

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="converted_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model on random input data.
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
```

### ���͌^�����p���� <a name="interpreter_data"></a>

�ȉ�����W�����@�����V�O���D�I TensorFlow Lite Flatbuffer �͌^�C�p TensorFlow Lite Python ����B
���㎦���꘢���� TensorFlow �͌^�n�I�[���[�ė�B

```python
import numpy as np
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
const = tf.constant([1., 2., 3.]) + tf.constant([1., 4., 4.])
val = img + const
out = tf.identity(val, name="out")

with tf.Session() as sess:
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  tflite_model = converter.convert()

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
```

## ������

### ���� <a name="latest_package"></a>

���s�ŐV�Ŗ{�I TensorFlow Lite Converter Python API�C�Ȉ�������� nightly �Ŗ{�F
[pip](https://www.tensorflow.org/install/pip)�i��䦁j�C
[Docker](https://www.tensorflow.org/install/docker)�C
[�����㌚ pip ��](https://www.tensorflow.org/install/source)�B

###  TensorFlow 1.12 �y�V�O�Ŗ{�I�͌^ <a name="pre_tensorflow_1.12"></a>

�Q�l���\�� TensorFlow 1.12 �V�O�I�Ŗ{�� TensorFlow �͌^�� TensorFlow Lite
�s `help()` �� API �I��B 

TensorFlow �Ŗ{ | Python API
------------------ | ---------------------------------
1.12               | `tf.contrib.lite.TFLiteConverter`
1.9-1.11           | `tf.contrib.lite.TocoConverter`
1.7-1.8            | `tf.contrib.lite.toco_convert`