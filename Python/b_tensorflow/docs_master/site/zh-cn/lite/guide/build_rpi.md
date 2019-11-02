# ��䖔h�㌚ TensorFlow Lite
## ����
### �����H��
�����\�ߍ�64�ʓI ubuntu 16.04.3 �a Tensorflow devel docker image [tensorflow/tensorflow:nightly-devel](https://hub.docker.com/r/tensorflow/tensorflow/tags/) ��B
�v�g�p TensorFlow Lite �������\�C������H��a���I�B
```bash
sudo apt-get update
sudo apt-get install crossbuild-essential-armhf
```
�@�ʎg�p Docker�C�\�ٖ@�g�p `sudo`�B
### ��
������Tensorflow�C�ݓI���ډ��s���r�{�ȉ����L�ˁF
> tensorflow�� /tensorflow ���B�@�ʎg�p�I�� docker �� tensorflow/tensorflow:nightly-develimage�C��g�pTensorflow���C�g�p�ȉ����ߑ��B
```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```
���ӁC�����v�s�ꎟ������B
�R�@�֔\�F
```bash
./tensorflow/lite/tools/make/build_rpi_lib.sh
```
���꘢��,���ʘ��F
tensorflow/lite/tools/make/gen/rpi_armv7l/lib/libtensorflow-lite.a.
## �{�n
�ߍ�Raspberry Pi 3b�CRaspbian GNU / Linux 9.1�istretch�j�Cgcc�Ŗ{6.3.0 20170516�iRaspbian 6.3.0-18 + rpi1�j��s���B
�oRaspberry Pi�C�����H��B
```bash
sudo apt-get install build-essential
```
���C����TensorFlow�B�ݓI���ڍs�F
```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```
���ӁC�����v�s�ꎟ������B
�R�@�֔\�F
```bash
./tensorflow/lite/tools/make/build_rpi_lib.sh
```
���꘢��,���ʘ��F
tensorflow/lite/tools/make/gen/lib/rpi_armv7/libtensorflow-lite.a �B
