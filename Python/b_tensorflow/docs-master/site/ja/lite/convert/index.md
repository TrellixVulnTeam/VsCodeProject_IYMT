# TensorFlow Lite �R���o�[�^

TensorFlow Lite �R���o�[�^�́A TensorFlow ���f������͂Ƃ��� TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) �t�@�C���𐶐����܂��B

�R���o�[�^�� [SavedModel �f�B���N�g��](https://www.tensorflow.org/guide/saved_model)�A [`tf.keras` ���f��](https://www.tensorflow.org/guide/keras/overview)�A [��ۊ֐�](concrete_function.md) ���T�|�[�g���Ă��܂��B

Note: ���̃y�[�W�� TensorFlow 2.0 �̃R���o�[�^ API �Ɋւ���h�L�������g�ł��BTensorFlow 1.X �� API �ɂ��Ă� [������](https://www.tensorflow.org/lite/convert/) ���������������B

## �f�o�C�X�ւ̃f�v���C

TensorFlow Lite `FlatBuffer` �t�@�C���́A�N���C�A���g�f�o�C�X�i���o�C���f�o�C�X��g�ݍ��݃f�o�C�X�j�Ƀf�v���C���ATensorFlow Lite �C���^�[�v���^���g���ă��[�J���Ŏ��s�ł��܂��B���̕ϊ��v���Z�X�͉��}�̂Ƃ���ł��B

![TFLite converter workflow](../images/convert/workflow.svg)

## ���f����ϊ�����

TensorFlow Lite �R���o�[�^�� [Python API](python_api.md) ���g���ׂ��ł��B
Python API ���g�����ƂŁA���f���̕ϊ����f�v���C�p�C�v���C���̒��ɑg�ݍ��ނ��Ƃ��ȒP�ɂȂ�A[�݊���](../../guide/ops_compatibility.md) �̖��ɑ����i�K�őΏ����₷���Ȃ�܂��B

����̕��@�Ƃ��� [�R�}���h���C���c�[��](cmdline.md) ���g���Ċ�{�I�ȃ��f����ϊ����邱�Ƃ��ł��܂��B
