# �ʉ��͌^
�{���񋟗L�@���ʉ� TensorFlow Lite �͌^�I�M���B�M���C�Q[�͌^��](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/performance/model_optimization.md)�B

# �@�F���� CPU �^���I�ʉ��͌^
�����͌^�I�ŕ��@���ݐ��������d�ʉ� 8 �ʛ�g�ݍs���h�ʉ���/�����B��L���C�A��l���ڐ��B

�݊��C�� optimizations �u�u�召�s���F
```
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()
```

# �����F�p�������s�I�ʉ��͌^
�p�������s�I�ʉ��͌^����L�X�ቄ�C�X���ڐ��a���������팓�e�͌^�I�͌^�B�ڑO�C���v��L["��ʉ�"�_](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize)�I�͌^ �B

�\�F
```
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.inference_type = tf.lite.constants.QUANTIZED_UINT8
input_arrays = converter.get_input_arrays()
converter.quantized_input_stats = {input_arrays[0] : (0., 1.)}  # mean, std_dev
tflite_model = converter.convert()
```
���S�����͌^�C�� uint8�Bmean �a std_dev values �w��ݖ͌^�� UINT8 �I���@���f�˓����I���_�B

mean �� 0 �� 255 �V�I�����C�f�˓����_�� 0.0f�Bstd_dev = 255 /�ifloat_max - float_min�j

���命���p�C�䌚�g�p�@�ʉ��B�䐳�݌����p���@���a�ʉ��I�V�H��C���]���������ʉ��͌^�B
