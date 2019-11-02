# Segmentation

![segmentation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/images/segmentation.png)

## Get started

DeepLab ���p���������I�Ő�I�[�x�w�͌^�C���ڐ������I�����f���z(��@�l�C��C�L)�B

[Download starter model](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/deeplabv3_257_mv_gpu.tflite)

## How it works

���������I�����f���ۗ^�^�����B�^��`��撆��[��]�I�C(https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/object_detection/overview.md)�a�������s��[����]�I�C(https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/image_classification/overview.md)�`���ƁB

���O�I��ȉ����\�F

1. DeepLabv1 :��g�p atrous convolution �����n�T���ݐ[�x�ɐ_㤒��Z���������I�������B
2. DeepLabv2 :��p atrous spatial pyramid pooling(ASPP) ,�g�p�����ї��a�L����I��,�ݑ��ړx�㌒�n�����ڏہB
3. DeepLabv3 :��g�p������[5,6]���WASPP�͈ȕߍX���I�M���B����������y��[7]�Q���ȉ����B���I�C�ݘa�Ċ���p atrous convolution �����s���o���I�o�����C�ݏo������16�L���I������y��,��ݏo��8�������X���I�ĝ��ʁB
4. DeepLabv3+ :��W�� DeepLabv3 ,�������꘢�A�L���I����́C�ȉ����ʁC�ޑ��������ۊE�B���O�C�݊�-���풆�C�Ȓ� atrous convolution �C�Ӓn�T�������I������I�������C�Ȑܒ����x�a�s�B

## Example output

�͌^���Ȝk���I���x�ݖڏۏ㌚�����B
![segmentation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/segmentation/images/segmentation.gif)

## Read more about segmentation

* [Semantic Image Segmentation with DeepLab in TensorFlow](https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html)
* [TensorFlow Lite Now Faster with Mobile GPUs (Developer Preview)](https://medium.com/tensorflow/tensorflow-lite-now-faster-with-mobile-gpus-developer-preview-e15797e6dee7)
* [DeepLab: Deep Labelling for Semantic Image Segmentation](https://github.com/tensorflow/models/tree/master/research/deeplab)
