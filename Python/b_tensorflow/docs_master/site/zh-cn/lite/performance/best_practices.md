# ���\�I�ŉ��H

�R���ژa�Ɠ����I�Z�\�͗L���C���ȕێ��p�I���퍂�����p�����d�v�I�B��ߎʗ���ŉ��H�a�����I���C�\�p�������I TensorFlow Lite �͌^�a�p�B

## �C�ŉ��I�͌^

�����C�I�s���C����v�ݖ͌^�x�a�召�V����q�B�@�ʓI�C���v���y���C�߉\���v�꘢�厧�I�͌^�B�����x�s���I�C�C�A�ōD�g�p����_�I�͌^�C�����I�͌^�s��p�X���I���a�����C���ʍX���X�����B��@�C���W������I�����͌^���y���a���͌^�召�I�e�B

![�͌^�召�a�y�x�I�n](../images/performance/model_size_vs_accuracy.png "�͌^�召�a�y�x")

![�y�x�a���I�n](../images/performance/accuracy_vs_latency.png "�y�x�a��")

�꘢�ډ��I����͌^�A�� [MobileNets](https://arxiv.org/abs/1704.04861)�C�͌^�����ڒ[�p�����I�B��I [�͌^��\](../models/hosted.md) ��o���O�{�ژa�Ɠ������I�͌^�B

�ȗp���ȓI�����ʈڊw�č��͌^�B�ŉ�I�ڊw�����F[����](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0) �a [����](https://medium.com/tensorflow/training-and-serving-a-realtime-mobile-object-detector-in-30-minutes-with-cloud-tpus-b78971cf1193)�B

## �I�͌^

�ݗ��꘢���I�C�I�͌^�V�@�C�͌^�a����y�k�D�I�s�BTensorFlow Lite [�H��](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark) �L���u�I��C�W���꘢�Z���I�����B�\�����𐫔\�r�a���Z���嗹�Z�B

## �a���igraph�j���I�Z��

�@�ʖ^������I�Z���ɏo�ݖ͌^���C�󊎊���Z�����՗��啔���C�߉Ȍ����@�������Z���B��v��폭�C�� TensorFlow Lite ���I�啔���Z���s�����I�Ŗ{�B�R���C�@�ʗ����Z���I�s�����C���Ȏʈ꘢����I�X���I�Ŗ{�B�ŉ�I [����Z������](../custom_operators.md)�B

## ���I�͌^

�͌^�|�݌��X���I�͌^�C�󊎒ʏ�X���A�X�����\�B�������\�핔�����ڏ�B

### �ʉ�

�@�ʓI�͌^�g�p���_�d���Ҍ��㔟���C�ߖ͌^�召���Ȓʗʉ���75%�C���@�L���n�����_�d��32����8���B�ʉ����F[�@�ʉ�](post_training_quantization.md) �a [�ʉ�](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/quantize/README.md){:.external}�B�O�ҕs���v�Ė͌^�C�A���ݏ���v����L���x���B�����x�������ڎ�䗁C�g�p�ʉ��B

���䦗���y�ȕۖ͌^���y���v�L��e�B�ŐM���F[�͌^������](model_optimization.md)�B

## ������

TensorFlow Lite �x�����Z���g�p�������j�B�����������Ȓ񍂎Z���s���x�B�R���C����������g�I�͌^�g�p�X���I���a�\���B

�L���p���C������\�������X�d�v�B�Ȓʒ� [����](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/interpreter.h#L346) �I���ʗ����������B�R���C�������s�I��������s���C�����s���������\�I���B��@�C�u�\�������I���x�����I�{�C�A�@�ʓ��L�꘢�p�ݍs�I�C���\�ʉ\����X���B

## ������]���{

�@�ʓI�p�v�L��k�D�n�C�ݓ��͌^�a��͌^�o�\��L��]���{�B�ې�����]���{�B�@�ʍݎg�p�� API�C�@ Java�C�ێe���\���ӎ��B��@�C�@�ʎg�p ByteBuffers ��[��](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/java/src/main/java/org/tensorflow/lite/Interpreter.java#L175)�CJava API ��������B

## �p�������H��I�p

�������H��C�@ [Android profiler](https://developer.android.com/studio/profile/android-profiler) �a [Instruments](https://help.apple.com/instruments/mac/current/)�C�񋟗��x�I��p���p�I�M���B�L���\�\�s�o�����͌^�C�����^�͌^���ݓI�p��B�ۏn���������H��a����ōD�I���@�B

## �ēI�͌^���ێ�v���g�p��p�I�d��������

TensorFlow Lite �������V�I���@���z���X���I�d�������͌^�C��@ GPU�ADSP �a�_������B��ʗ��C��������� [�㗝](delegates.md) �q�͖\�I�C���q�͐ڊǕ�������s�BTensorFlow Lite �\�ʈȉ����@�g�p�㗝�F

*   �g�p Android �I [�_� API](https://developer.android.com/ndk/guides/neuralnetworks/)�B�ȗ��p���d��������@�䗈�񏡖͌^���x�a�����B�v�p�_� API�C�݉������p [UseNNAPI](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/interpreter.h#L343)�B
*   ��ߕz���꘢���񐧓I GPU �㗝�CAndroid �a iOS ���g�p OpenGL �a Metal�B�v�p���C�� [GPU �㗝����](gpu.md) �a [����](gpu_advanced.md)�B
*   �@�ʔ\��y�d���C��Ȍ����ȓI�㗝�B�X���M���C�� [TensorFlow Lite �㗝](delegates.md)�B

���ӁC�L�I������ݖ^���͌^���ʍX�D�B���㗝����y�ȏo�œI���k�d�v�I�B��@�C�@�ʗL�꘢��포�I�͌^�C�߉\�v�K�v���͌^�ϑ� NN API �� GPU�B�����C����L���Z�x�I��͌^���C������A���꘢�k�D�I�B

## ���v�X�����H

TensorFlow ���ӏ��f�a��ʋ�̓I���\�B�� [GitHub](https://github.com/tensorflow/tensorflow/issues) ��o��`�q�B
