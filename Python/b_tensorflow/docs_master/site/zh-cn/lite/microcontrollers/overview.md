# TensorFlow Lite for Microcontrollers

TensorFlow Lite for Microcontrollers �� TensorFlow Lite �I�꘢���ڐA�Ŗ{�C���p�����T����a�����ꍱ�L���玚�����I�B

���Ȓ��ڍ݁g�����h��s�C�s���v����n�x���A�C���y C/C++ �a�������z�B�j�S�s(core runtime)�� Cortex M3 ��s�� 16KB�C���㑫�ȗp���s�����͌^�I����C����� 22KB �I��B

## �n

�v��������s TensorFlow Lite for Microcontrollers�C[���T�����](get_started.md)�B

## �Y���T����k�d�v

���T����ʏ퐥���^�A��\�ՓI�Z�C��Ɠ��ݑ����v�s��{�Z�I�d�����C��Ɨp��a��㤓��B�N�s�L���\�����T����퐶�o���B

���T����ʏ��\�՘a���ڐ��s���C�A������~�ᗹ���\�́A�����a���B�ꍱ���T�����L�p��������w�C���\�I���\�B

�ʍݔ��T�����s����w���f�C�l�ȍݕs�˘�㤐ړI��v���� AI �Y�����e�e�I�d�����C��p�������A�����ȋy�R�����v�I�����������I���B�ݏ�s���f��ȏ��ێ��C���v�L�����������o���B

## ���\�a��

* C++ API�C���s(runtime)�� Cortex M3 ��� 16KB
* �g�p�y�I TensorFlow Lite [FlatBuffer](https://google.github.io/flatbuffers/) ��(schema)
*  Arduino�AKeil �a Mbed �����s�I�Ɠ������䐶���I�ڕ���
* �����Ɠ������䉻
* �������I[�����](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/micro_speech)

## �H�여��

���� TensorFlow �͌^���������T����I���F

1. **������ TensorFlow �͌^**

    �͌^�K��포�C�ȕ֍ݍ@���I�ځB�����\�g�p[�x���I����](build_convert.md#�x���I����)�B�@�ʗv�g�p���O�s��x���I����C�Ȓ񋟎��ȓI�B

2. **���͌^ TensorFlow Lite FlatBuffer**

    ���g�p [TensorFlow Lite ��](build_convert.md#�͌^)�����͌^�y TensorFlow Lite �i���B�\��]�o�ʉ��͌^�C�����I�ڐ��X���A�s�����X���B

3. **�� FlatBuffer  C byte ��**

    �͌^�ۑ��ݑ��������풆�C��ȓI C �����I�`���񋟁B�y�H��p��[�� FlatBuffer  C ��](build_convert.md#-C-��)�B

4. **�W�� TensorFlow Lite for Microcontrollers �I C++ **

    �ʔ��T�����Ȏg�p [C++ ](library.md)�s���f�B

5. **�������I**

    �������󏫑��������I�B

## �x���I����

�Ɠ������I���V�ꐥ���ݑ��s���I�̌n�A�A����n�a���n�B��I�ڐ��s�\���n�x�����s�I���C��s�\�n�����Y���x�����B

�@�ʐ��i�l�C�ȉ���񋟓I�ȉ�����I�����������I�ڕ����F

                                                                                           | Mbed                                                                           | Keil                                                                           | Make/GCC
---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------
[STM32F746G Discovery Board](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)     | [��](https://drive.google.com/open?id=1OtgVkytQBrEYIpJPsE8F6GUKHPBS3Xeb)     | -                                                                              | [��](https://drive.google.com/open?id=1u46mTtAMZ7Y1aD-He1u3R8AE4ZyEpnOl)
["Blue Pill" STM32F103 ���e��](https://github.com/google/stm32_bare_lib)                   | -                                                                              | -                                                                              | [��](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/README.md#building-for-the-blue-pill-stm32f103-using-make)
[Ambiq Micro Apollo3Blue EVB�i�g�p Make�j](https://ambiqmicro.com/apollo-ultra-low-power-mcus/)| -                                                                              | -                                                                              | [��](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/README.md#building-for-ambiq-micro-apollo3blue-evb-using-make)
[Generic Keil uVision Projects](http://www2.keil.com/mdk5/uvision/)                            | -                                                                              | [��](https://drive.google.com/open?id=1Lw9rsdquNKObozClLPoE5CTJLuhfh5mV)     | -
[Eta Compute ECM3531 EVB](https://etacompute.com/)                                             | -                                                                              | -                                                                              | [��](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/README.md#Building-for-the-Eta-Compute-ECM3531-EVB-using-Make)

�@�ʓI������x���C�Y���x�����s���B�ȍ� [README.md](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/README.md#how-to-port-tensorflow-lite-micro-to-a-new-platform) ��������B

### �ڐA�Q�l��

�@�ʖv�L�l��̓I�I���T���핽��C���ґ��z�ݎn�ڐA�V�O�p��C�œI���@��[���^����ٓI�Q�l��](https://drive.google.com/open?id=1cawEQAkqquK_SO4crReDYqf_v7yAwOY8)�B

�����L�k�������C����������܌��꘢�񐧕��������I�������B�������s�L�꘢�I Makefile �����C�\�����������{���C�� IDE ���󌚛��B��񋟗��ߒu�D�I [Visual Studio Code](https://code.visualstudio.com/) �ڕ����C�����ȏ��n�݌ו��� IDE ����B

## ��

��I�ڐ��g�y�ˉA�՘��C���A�ǍD�A�՘��W���C��ʈ�v�I�����ˁA����AAPI �a���j�ڌ��^ TensorFlow Lite ���S���e�B

�ȍX����[�ژa�t](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro#goals)���ʗL�I�M���B

## ����

TensorFlow Lite for Microcontrollers ���T���풆�I����������B�@�ʐ��ݎg�p�X��I�i��@�� Raspberry Pi �I�Ɠ��� Linux �j�C�y�I TensorFlow Lite �y�ˉ\�X�e�ՏW���B

�l�ȉ������F

* �x�� TensorFlow ����I[�L���q�W](build_convert.md#�x���I����)
* �x���L���I�ꍱ
* �� C++ API ���v������Ǘ�
