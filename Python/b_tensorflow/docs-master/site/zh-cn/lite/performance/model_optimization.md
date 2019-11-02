# �͌^��

Tensorflow Lite �a [Tensorflow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization) (Tensorflow�͌^���H���)�񋟗��ŏ����������I�H��B

���ژa��� (IoT) ��,���������ޑ��d�v�B���ݗ��C�����C�\�՘a�͌^�����ʗL�������B
���O�C�͌^���𗹒�_�d�� (fixed-point hardware) �a�����d��������I���\�́B

## �͌^�ʉ�

�[�x�_㤓I�ʉ��g�p���ꍱ�Z�C���Z�ȍ~��d�I���\���C�󊎉I�~�ᑶ�a�Z�I�����B�ʉ��I�D�L:

* �L CPU ����I�x���B
* �������I�ʉ��~�ᗹ�p����a���������I���퐬�{�B
* �� CPU �a�d��������� SIMD �w�ߌ��\�C�ʉ����L�v�B

TensorFlow Lite �ʉ��񋟗����I�ʉ��x���B

* Tensorflow Lite [post-training quantization](post_training_quantization.md) �ʉ��g�d�a�����I Post training �X�B
* [Quantization-aware training](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize){:.external} �Ȉȍŏ����x���~��㤁G�p���ɐ_㤓I�꘢�q�W�B

### ���a�y����

�ȉ����ꍱ�͌^ post-training quantization �a quantization-aware training �@�I���a�y���ʁB���L�����s���ݎg�p������j�I Pixel 2 ��ʓI�B�����H���I���C���������V��:

<figure>
  <table>
    <tr>
      <th>�͌^</th>
      <th>Top-1 ����(���n) </th> 
      <th>Top-1 ����(Post Training�ʉ�) </th>
      <th>Top-1 ���� (Quantization Aware Training) </th>
      <th>�� (���n) (ms) </th> 
      <th>�� (Post Training�ʉ�) (ms) </th>
      <th>�� (Quantization Aware) (ms) </th>
      <th> �召 (���n) (MB)</th>
      <th> �召 (���@) (MB)</th>
    </tr> <tr><td>Mobilenet-v1-1-224</td><td>0.709</td><td>0.657</td><td>0.70</td>
      <td>124</td><td>112</td><td>64</td><td>16.9</td><td>4.3</td></tr>
    <tr><td>Mobilenet-v2-1-224</td><td>0.719</td><td>0.637</td><td>0.709</td>
      <td>89</td><td>98</td><td>54</td><td>14</td><td>3.6</td></tr>
   <tr><td>Inception_v3</td><td>0.78</td><td>0.772</td><td>0.775</td>
      <td>1130</td><td>845</td><td>543</td><td>95.7</td><td>23.9</td></tr>
   <tr><td>Resnet_v2_101</td><td>0.770</td><td>0.768</td><td>N/A</td>
      <td>3973</td><td>2868</td><td>N/A</td><td>178.3</td><td>44.9</td></tr>
 </table>
  <figcaption>
    <b>Table 1</b> �͌^�ʉ�CNN�͌^�I�D
  </figcaption>
</figure>

## �H��

���C [hosted models](../guide/hosted_models.md) ���I�͌^���ۍ��I�p�����B�@�ʖv�L�C�䌚�p�� [post-training quantization tool](post_training_quantization.md) �n�C���������p�I�C���َ������B

�����x�a���ږv�L���C���Ҏ��v�d��������x����v�C [quantization-aware training](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize) {:.external} ���X�D�I�B�Q Tensorflow �͌^���H���[Tensorflow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization) ���I�I�������Z�B

����: Quantization-aware training �x���ɐ_㤑̌n�I�q�W�B
