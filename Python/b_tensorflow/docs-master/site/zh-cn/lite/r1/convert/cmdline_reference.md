# �햽�ߍs�Q�l

�{ TensorFlow 1.9 �� TensorFlow �ŐV�Ŗ{�� TensorFlow Lite �햽�ߍs�g�p�I���ߍs�Q���񋟑S�ʎQ�l�B

## �����ߍs�Q��

���񍂖��ߍs�Q���w��������a�o�����I�B���ߍs�Q�� `--output_file` �����v�w��B���O�C`--graph_def_file`�C`--saved_model_dir` �a `--keras_model_file` �������v�w��꘢�B

* `--output_file`�B�^�F�������B�w��o�����I�S�H�a�B

* `--graph_def_file`�B�^�F�������B�w��� GraphDef �����i�g�p [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py)�j�I�S�H�a�B

* `--saved_model_dir`�B�^�F�������B�w���� SavedModel �I�ړI�S�H�a�B

* `--keras_model_file`�B�^�F�������B�w���� tf.keras �͌^�I HDF5 �����I�S�H�a�B 

* `--output_format`�B�^�F�������B㞏ȁF`TFLITE`�B�w��o�����I�i���B�򉺗�F

    * `TFLITE`�FTensorFlow Lite FlatBuffer �i���B    
    * `GRAPHVIZ_DOT`�FGraphViz `.dot` �i����܍@�����꘢���B 

* ���ӁC�� `--output_format`  `GRAPHVIZ_DOT` �� TFLite ���葢�����B�����C�����I���\�ٖ@���f�œI�B�@�ʑz�����f���L�I�ŉ��C�g�p `--dump_graphviz_dir`�B

�ȉ����ߍs�Q���w��g�p SavedModels �I�����Q���B

* `--saved_model_tag_set`�B�^�F�������B㞏ȁF [kSavedModelTagServe](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/cc/saved_model/tag_constants.h)�B�w���Ȑ������u�I�C�p���v���͓I SavedModel ���I MetaGraphDef�B���I���L�s�K�w��B

* `--saved_model_signature_key`�F�^: �������B㞏ȁF`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`�B�w���ܓ��a�o�I SignatureDef �I�B

## �͌^���ߍs�Q��

�͌^���ߍs�Q���񋟗L���ݓ��������I�͌^�I�O�M���B

* `--input_arrays`�B�^�F�Ȑ������u�I��������\�B�w��꘢��ܓ������ʖ��̓I��\�B

* `--output_arrays`�B�^�F�Ȑ������u�I��������\�B �w��꘢��܏o�����ʖ��̓I��\�B

�ȉ����ߍs�Q������ʓI�����B���ߍs�Q�� `--input_arrays` ���I�ꍪ�������ȉ����ߍs�Q�����I��B

* `--input_shapes`�B�^�F�Ȗ`�����u�I��\�C��\�R�Ȑ������u�I�������I�q��\���B���q��\�w��꘢�����I�`��C�`��I�i���Q [TensorFlow ��](https://www.tensorflow.org/guide/tensor#shape)�B

* ��F `--input_shapes=1,60,80,3` ���꘢�T�^�I�͌^�C�\����ʑ召 1 �C �����I�� 60 �C �����I 80 �C �����I�[ 3 �i��\�ʓ��j�B

* ��F `--input_arrays=foo,bar --input_shapes=2,3:4,5,6` �\�� "foo" �I�`�� [2, 3]�C "bar" �I�`�� [4, 5, 6]�B
    
* `--std_dev_values`�C `--mean_values`�B �^�F�Ȑ������u�I���_��\�B���w�蓖�����ʉ��C�����I�ʉ��i�����ʉ��j�����Q���B���L�� `inference_input_type` ��w�� `QUANTIZED_UINT8` �C�ˎ��v�蛀�B

    * `mean_values` �^ `std_dev_values` �I�Ӕ@���F�ʉ��������I���ʉ��������@����������꘢���w���i���꘢�������j�F

    * `real_value = (quantized_input_value - mean_value) / std_dev_value`�B

* ���꘢�ʉ����s���_���f �i`--inference_type=FLOAT`�j �C�ݍs���_���f�V�O�C���f�㏫����������q�����ʉ����s���ʉ��B

* ���s�ʉ����f �i`--inference_type=QUANTIZED_UINT8`�j �C���f��s��s���ʉ��B�R���C���L���I�ʉ������Q���C������� `mean_value` �a `std_dev_value` �w��I�ʉ������Q���C�r�藹�ʉ����f�㒆�g�p�I�s�_�����B`mean_value` �ݍs�ʉ����f�K�������B

## ���ߍs�Q��

���ߍs�Q���w��p�ݏ�I�C�����w��o������L�������B

* `--inference_type`�B�^�F�������B㞏ȁF`FLOAT`�B�o���������L�����I�����^�C���� �i�p `--inference_input_type` �w��j���O�B�K�� `{FLOAT, QUANTIZED_UINT8}`�B

    �����ߍs�Q�����e�����C����_���a�ʉ����B�s��������L�����^�C��ʏ퐮���iplain integer�j���a���������B��̔@���F
    
    * �@�ʎw�� `FLOAT`�C�ߏo�������I�����������_�^�B�@�ʛ��ݓ���������ʉ��C�����픽�ʉ��B

    * �@�ʎw�� `QUANTIZED_UINT8`�C�ߏo�������I��������ʉ� uint8�B�@�ʛ��ݓ������������_�^�C������ʉ��B

* `--inference_input_type`�B�^�F�������B�o�������I�꘢�������I�����^�B���L�����I�����^�I㞏Ȑ��^ `--inference_type`�I�w�葊���B�����ߍs�Q���I��v�ړI�������꘢��L�ʉ������I���_�B�ݓ����V�@�ڒ��Y���꘢���ʉ��Z�q�B�K�� `{FLOAT, QUANTIZED_UINT8}`�B

    �����ߍs�Q����v�p���I�͌^�F�����ʁC�A���v�����_���f�B���I���͌^�C�� uint8 ������ʉ��C�󊎓I�����g�p�I�ʉ������Q�������I `mean_value` �a `std_dev_value` �����Q���B

* `--default_ranges_min`�C `--default_ranges_max`�B�^�F���_�^�B�w��㞏ȁi�ŏ��C�ő�j��C�p�����L�v�L�w���I���B��p���ʉ��I���������җʉ��I�������s�ʉ��B�����ߍs�Q���v�͌^�y���~��B���I�ړI�ݘ��ʁg���ʉ��h���ꉺ�ʉ��B

* `--drop_control_dependency`�B�^�F�z�^�B 㞏ȁFTrue�B�w�营�ې��ҜP�T���ˁB���R�� TensorFlow Lite �s�x���T���ˁB

* `--reorder_across_fake_quant`�B�^�F�z�^�B 㞏ȁFFalse�B�w�营�ۗ��V�O�I�ʒu��I FakeQuant �_�s�d�V�r���B�p�� FakeQuant �_�I�ʒu�j�V�C�Ȏ����e�I��v�B����v�����I�^�ʉ��s���C�L�\����s���I�Z�s�B

* `--allow_custom_ops`�B�^�F�������B 㞏ȁFFalse�B�w�营�ۈ򎩒葀��B���� false �C���L���m����s��B���� true �C���L���m���������葀��B�Ҏ��ʍ� TensorFlow Lite runtime �z�u�����͊허�񋟍��M���B

* `--post_training_quantize`�B�^�F�z�^�B 㞏ȁFFalse�B�w�营�ۗʉ���I���_�͌^�I�d�B�͌^�����C�������P�i�ȏy���~�����j�B

## ���u���ߍs�Q��

���񖽗ߍs�Q���ݒ����I�����_���� [GraphViz](https://www.graphviz.org/) `.dot` �����I���B

- `--dump_graphviz_dir`�B�^�F�������B�w�� GraphViz `.dot` �����o���I�ړI�S�H�a�B�ݓ��V�@�C�ȋy���L�����V�@�C��o�B

- `--dump_graphviz_video`�B�^�F�z�^�B�w�营�ۍݎ��V�@�o GraphViz �����B���v�� `--dump_graphviz_dir` �L�w��B
