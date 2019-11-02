# TensorFlow Lite converter
TensorFlow Lite converter���p����TensorFlow�͌^�����I[FlatBuffer](https://google.github.io/flatbuffers/)�i���C�ȕ�TensorFlow Lite����p�B

���ӁF���ʕ��TensorFlow 1.x�Iconverter API�����C[TensorFlow 2.0�IAPI�_����](https://www.tensorflow.org/lite/convert/)

## FlatBuffers
FlatBuffers���꘢�����I���ו��䏘�񉻁B������[protocol buffers](https://developers.google.com/protocol-buffers)�C��ݘ�FlatBuffers�ݐ����V�O�s���v�����v�\�s���/���C������Ƙ��ۍs�������z�BFlatBuffers�I���p���protocol buffers���꘢���ʁB

## ���͌^�|������
TensorFlow Lite converter�Ș�TensorFlow�͌^������TensorFlow Lite [FlatBuffers](https://google.github.io/flatbuffers/)����(.tflite)�B

converter�x���ȉ����i���F
- [SavedModels](https://www.tensorflow.org/guide/saved_model#using_savedmodel_with_estimators)
- �ʌŒ�퐔(Frozen)�I`GraphDef`:�R[freeze_graph.py](https://www.tensorflow.org/code/tensorflow/python/tools/freeze_graph.py)�����I�͌^
- `tf.keras` HDF5�͌^
- �C���� `tf.Session`��I�͌^�i��Python API�j

�R�@�C��TensorFlow Lite FlatBuffer�����������q�[�CTensorFlow Lite �����g�p�͌^�ݏ�s���f(inference)�B����@�������F
![TFLite converter workflow](https://github.com/tensorflow/tensorflow/raw/master/tensorflow/lite/g3doc/images/convert/workflow.svg?sanitize=true)

## 

TensorFlow Lite Converter �Ȓʈȉ������g�p�F
- [Python](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/convert/python_api.md)�i**�����**�j�F�g�pPython API�ȍX���n���͌^�͌^��(model development pipeline)�I�ꕔ���C��L�����ݑ���������[���e��](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/tf_ops_compatibility.md)
- [���ߍs](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/convert/cmdline_examples.md)
