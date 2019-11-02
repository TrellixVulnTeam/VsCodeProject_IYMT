# �����^�͌^

���T�����L�L���I RAM �a����C����������w�͌^�I�́B���O�C�ʌ����T����I TensorFlow Lite �ڑO���x���L���I�ꕔ���Z�C������񏊗L�I�͌^�s���s�I�B

�{�����𗹈꘢ TensorFlow �͌^�Ȏg���ݔ��T�����s�I���B�{������T�q���x���I�Z�C�󘰗^�꘢�͌^�Ȏg���������������o���ꍱ�w�B

�꘢�[���[�I�A�s�I�����^�͌^�I����C���@���I Jupyter notebook ���F
<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/hello_world/create_sine_model.ipynb">create_sine_model.ipynb</a>


## �͌^

���꘢�ߍD�I TensorFlow �͌^�Ȏg���ݔ��T�����s�C�g�p [TensorFlow Lite �� Python API](https://tensorflow.google.cn/lite/convert/python_api) �B���\���͌^�� [`FlatBuffer`](https://google.github.io/flatbuffers/) �i���C���͌^�́C��C���͌^�Ȏg�p TensorFlow Lite �x���I�Z�B

### �ʉ�
�����s�\���I�͌^�́C�l�g�p[�@�ʉ�](https://tensorflow.google.cn/lite/performance/post_training_quantization)�B����~��͌^�������I���x�C�������͌^�́B�s�C����\��v�͌^�y���I���~�C�����͖͌^���ޔ@���B�ݗʉ��O�@���͖͌^�I�y���ȕێ��݉ڎ�䗓������d�v�I�B

�ȉ��I Python ��Вi�W�����@���g�p�ʉ��s�͌^�F

```python
import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_quant_model)
```

### �꘢ C ��
�����T���핽��v�L�{�n�����n�I�x���B���������g�p�꘢�͌^�œI�����������Ȉ꘢ C ���I�`����ܛ�I�����B

�ȉ��I unix ���߉���꘢�� `char` ���`����� TensorFlow Lite �͌^�I C �������F

```bash
xxd -i converted_model.tflite > model_data.cc
```

���o���@���F

```c
unsigned char converted_model_tflite[] = {
  0x18, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, 0x00, 0x00, 0x0e, 0x00,
  // <Lines omitted>
};
unsigned int converted_model_tflite_len = 18200;
```

��U�ߐ������������C�ȏ�����ܓ��I�����B�ݛƓ��������C���������� `const` �^�ȓ��X�D�I�����������d�v�I�B

�꘢�@���ݓI��������܋y�g�p�͌^�I��q�C���^�����ᒆ�I [`tiny_conv_micro_features_model_data.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/tiny_conv_micro_features_model_data.h) �B

## �͌^�^

�݈꘢�ʌ����T����I�͌^�C�l�͌^�I�́A�H��C�ȋy�p���I�Z�����d�v�I�B

### �͌^��

�꘢�͌^�K�ݓ񐧘a�s���ʓs�����C�Ȏg���Șa�����I����������N�����ړI���������B

�����꘢�X���I�͌^�C�ȍݓI���g�p�X���a�X���I�B�R���C���͓I�͌^�X�Ֆʌ����B�Ӗ��������C��g�p�������������I�s�\��͓I�͌^���L�ӓI�B�A���C�g�p�X��͓I�͌^���v����H��I�����B

���F�݈꘢ Cortex M3 ��C�ʌ����T����I TensorFlow Lite �I�j�S�s�� 16 KB�B

### �H��

�H��󓞖͌^�͗^�x�I�e�B��́A�I�͌^�\��v�X���I����C���v���p����I�H�����A��Z�B�I�p�C��v�����I�͏��՗^�ʏo�I�����\��꘢�B

### �Z�x��
�ʌ����T����I TensorFlow Lite �ڑO�x���L���I���� TensorFlow �Z�C�e���ȍs�I�͌^�B�䐳�v�͘��ݎQ�l�a����I�����ʓW�Z�x���B

�ߎx���I�Z�ȍݕ��� [`all_ops_resolver.cc`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.cc) ���œ��B
