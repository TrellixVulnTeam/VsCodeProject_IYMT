# �R���o�[�^�̃R�}���h���C�����t�@�����X

���̃y�[�W�ł́ATensorFlow 2.0 �ŃR�}���h���C������ [TensorFlow Lite �R���o�[�^](index.md) ���g�p������@��������܂��B �������A���D�܂����̂� [Python API](python_api.md) ���g�p������@�ł��B

[TOC]

## �T�v�̊T�v

TensorFlow Lite �R���o�[�^�ɂ͊�{�I�ȃ��f�����T�|�[�g����R�}���h���C���c�[�� `tflite_convert` ������܂����A�ʎq���₻�̑��̃p�����[�^ (SavedModel �̃V�O�l�`���� Keras ���f���̃J�X�^���I�u�W�F�N�g�Ȃ�) ���܂ޏꍇ�ɂ́A `TFLiteConverter`[Python API](python_api.md) ���g�p���Ă��������B

## �g����

�ȉ��̃t���O�œ��̓t�@�C���Əo�̓t�@�C�����w�肵�܂��B

*   `--output_file` ������^�B �o�̓t�@�C���̃p�X���w�肷��B
*   `--saved_model_dir` ������^�B TensorFlow 1.x �������� 2.0 �ō\�z���� SavedModel ���܂ރf�B���N�g���̃p�X���w�肷��B
*   `--keras_model_file` ������^�B TensorFlow 1.x �������� 2.0 �ō\�z���� tf.keras ���f�����܂� HDF5�t�@�C���̃p�X���w�肷��B


�g�p��͈ȉ��̂Ƃ���ł��B

```
tflite_convert \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```

## �ǉ��̐���

### �\�[�X����r���h����

TensorFlow Lite Converter �̍ŐV�o�[�W�����𗘗p����ɂ� [pip](https://www.tensorflow.org/install/pip) ���g�p���ăi�C�g���[�r���h���C���X�g�[��������@�ɉ����āA[TensorFlow ���|�W�g���� clone](https://www.tensorflow.org/install/source) ���� `bazel` ���g�����@������܂��B

�g�p��͈ȉ��̂Ƃ���ł��B

```
bazel run //third_party/tensorflow/lite/python:tflite_convert -- \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```
