# ���\��

�{������o���݈ꍱ Android �a iOS ��s��͌^ TensorFlow Lite �I���B

���������R [Android TFLite benchmark binary](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark) �y [iOS benchmark app](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark/ios) ���B

# ���싫�I��

�����싫�I���C�����I�����CCPU �a����u�g�p��j���B (��[��](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark#reducing-variance-between-runs-on-android))

��͌^�퉺��� `/data/local/tmp/tflite_models` �H�a�B�p�����I�񐧕���

�g�p [�����ߌ�](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark#on-android)�B
���O�C�����ʘ� `/data/local/tmp` �ځB

�g�p�ȉ���s��:

```
adb shell taskset ${CPU_MASK} /data/local/tmp/benchmark_model \
  --num_threads=1 \
  --graph=/data/local/tmp/tflite_models/${GRAPH} \
  --warmup_runs=1 \
  --num_runs=50 \
  --use_nnapi=false
```

�ݗ��C `${GRAPH}`���͌^�I�����C `${CPU_MASK}` ��CPU�a�x�u�B
�����\��:

Device | CPU_MASK 
-------| ----------
Pixel 2 | f0 
Pixel xl | 0c 

<table>
  <thead>
    <tr>
      <th>�͌^����</th>
      <th></th>
      <th>���ϐ���</th>
    </tr>
  </thead>
  <tr>
    <td rowspan = 2>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224.tgz">Mobilenet_1.0_224(float)</a>
    </td>
    <td>Pixel 2 </td>
    <td>123.3 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>113.3 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224_quant.tgz">Mobilenet_1.0_224 (quant)</a>
    </td>
    <td>Pixel 2 </td>
    <td>65.4 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>74.6 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/nasnet_mobile_2018_04_27.tgz">NASNet mobile</a>
    </td>
    <td>Pixel 2 </td>
    <td>273.8 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>210.8 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/squeezenet_2018_04_27.tgz">SqueezeNet</a>
    </td>
    <td>Pixel 2 </td>
    <td>234.0 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>158.0 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_resnet_v2_2018_04_27.tgz">Inception_ResNet_V2</a>
    </td>
    <td>Pixel 2 </td>
    <td>2846.0 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>1973.0 ms </td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_v4_2018_04_27.tgz">Inception_V4</a>
    </td>
    <td>Pixel 2 </td>
    <td>3180.0 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>2262.0 ms</td>
  </tr>


# iOS ��

�v�s iOS ���C  [���p����](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark/ios)�ܗL���I�͌^�C�� benchmark_params.json` ���I` `num_threads` ��u 1�B

<table>
  <thead>
    <tr>
      <th>�͌^����</th>
      <th></th>
      <th>���ϐ���</th>
    </tr>
  </thead>
  <tr>
    <td>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224.tgz">Mobilenet_1.0_224(float)</a>
    </td>
    <td>iPhone 8 </td>
    <td>32.2 ms</td>
  </tr>
  <tr>
    <td>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224_quant.tgz)">Mobilenet_1.0_224 (quant)</a>
    </td>
    <td>iPhone 8 </td>
    <td>24.4 ms</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/nasnet_mobile_2018_04_27.tgz">NASNet mobile</a>
    </td>
    <td>iPhone 8 </td>
    <td>60.3 ms</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/squeezenet_2018_04_27.tgz">SqueezeNet</a>
    </td>
    <td>iPhone 8 </td>
    <td>44.3</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_resnet_v2_2018_04_27.tgz">Inception_ResNet_V2</a>
    </td>
    <td>iPhone 8</td>
    <td>562.4 ms</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_v4_2018_04_27.tgz">Inception_V4</a>
    </td>
    <td>iPhone 8 </td>
    <td>661.0 ms</td>
  </tr>
 </table>

 