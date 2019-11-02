# �͌^�햽�ߎQ�l

�{��@���g�p TensorFlow 2.0 ���ߍs�H��I[TensorFlow Lite �͌^��](index.md)�B��I���@���g�p [Python API](python_api.md)�B

## �q

TensorFlow Lite �햽�ߍs�H�� `tflite_convert` ���x����͌^�B�g�p `TFLiteConverter` [Python API](python_api.md) �x���C���y�ʉ��������Q���I(��@�FSavedModels ���C���ҍ� Keras �͌^�㎩���).

## �g�p

���񖽗ߎQ���p�����a�o�����B

*   `--output_file`. �^: string. �w��o�����I�H�a�B
*   --saved_model_dir. �^: string. �w��ܗL TensorFlow 1.x ���� 2.0 �g�p SavedModel ���������I�H�a�ځB
*   --keras_model_file. Type: string. �w��ܗL TensorFlow 1.x ���� 2.0 �g�p tf.keras model ���� HDF5 �����I�H�a�ځB

��@�F

```
tflite_convert \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```

## ������

### �����㌚

�z�v�s�ŐV�Ŗ{�I TensorFlow Lite �͌^��Ȓ� [pip](https://www.tensorflow.org/install/pip) ���� TensorFlow 2.0 �ň���[���� TensorFlow ��](https://www.tensorflow.org/install/source)�R�@�g�p `bazel` ������ TensorFlow �B���ʐ��꘢������ TensorFlow �I��q�B

```
bazel run //third_party/tensorflow/lite/python:tflite_convert -- \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```
