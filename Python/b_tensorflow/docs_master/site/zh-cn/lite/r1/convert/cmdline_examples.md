# ��I���ߍs��

���ʓW���@���ݖ��ߍs���g�p TensorFlow Lite ��

[TOC]

## �ݖ��ߍs���g�p�I���� <a name="tools"></a>

�ȉ����ݖ��ߍs���g�p��I���@�F

*   `tflite_convert`: �� TensorFlow 1.9 �N�n�x��
    `tflite_convert` �� Python ��I�ꕔ��������B�֋N�C�ȉ����L����g�p `tflite_convert` �w��B
    *   ����: `tflite_convert --output_file=...`
*   `bazel`: ���g�p�ŐV�Ŗ{�I TensorFlow Lite Converter�C�Ȏg�p
    [pip](https://www.tensorflow.org/install/pip) ��[���� TensorFlow ](https://www.tensorflow.org/install/source) ��������g�p nightly �Ŗ{�I�I `bazel`�B
    *   ����: `bazel run //tensorflow/lite/python:tflite_convert ----output_file=...`

### �ݒᘰ 1.9 �Ŗ{�I TensorFlow ���͌^  <a name="pre_tensorflow_1.9"></a>

�@�ʈ����L�ᘰ 1.9 �Ŗ{�I Tensorflow�C��z�͌^�C�䐄䦎g�p
[Python API](python_api.md#pre_tensorflow_1.9)�B �@�ʑz�v�g�p���ߍs�͌^, �� Tensorflow 1.7 ���C�g�p toco�B

�Ȓʍݒ[����`toco help`����X�������ߍs�Q���I�M���B

�� TensorFlow 1.8 ���v�L�p�I���ߍs�H��B

## ��� <a name="basic"></a>

�ȉ��������W�������e�������x���I�^�� TensorFlow Lite FlatBuffers�B

###  TensorFlow GraphDef <a name="graphdef"></a>

�ȉ��������W���@������{�I TensorFlow GraphDef (�g�p [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py) ) TensorFlow Lite FlatBuffer ���s���_�������B��I��ܑ��ݓ_�������I�ʁC���ʔ�� Const ops �ۑ��B

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1
```

`input_shapes` �I��݉\�펩��B

###  TensorFlow SavedModel <a name="savedmodel"></a>

�ȉ��������W���@������{�I TensorFlow SavedModel  Tensorflow Lite FlatBuffer ���s���_�������B

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --saved_model_dir=/tmp/saved_model
```

[SavedModel](https://www.tensorflow.org/guide/saved_model#using_savedmodel_with_estimators)
�^�@�I��C�����v�X���I�Q���C���R���ۑ��� SavedModel ���I�����������v�B
 `--input_arrays`�a `--output_arrays` �����v�I�� [MetaGraphDef](https://www.tensorflow.org/saved_model#apis_to_build_and_load_a_savedmodel) �� [SignatureDefs](../../serving/signature_defs.md) ���I�꘢�ڍ��N���I�C�Ǝ��ꏘ�r��I���o��\�C���R`saved_model_tag_set`�w��B
 �a GraphDef ��, `input_shapes` �I��݉\�펩��B

�i�s�񋟕s SignatureDef �I MetaGraphDefs ����
�g�p[`assets/`directory](https://www.tensorflow.org/guide/saved_model#structure_of_a_savedmodel_directory) �I MetaGraphDefs �I�x���B

###  tf.Keras �͌^ <a name="keras"></a>

�ȉ������W���@�����꘢ `tf.keras` �͌^�꘢ TensorFlow Lite Flatbuffer�B 

 `tf.keras` �����K����ܖ͌^�a�d�B

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --keras_model_file=/tmp/keras_model.h5
```

## �ʉ�

### ���꘢TensorFlow GraphDef �ʉ��I���� <a name="graphdef_quant"></a>

TensorFlow Lite Converter ���e��_�ʉ��͌^�C��[��](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/quantize/README.md)�B
���_�͌^���L `FakeQuant*` ops �C���흇���ݍ����I�E���ő�ŏ��I䗐M���B

���꘢�ʉ��I�����H�여�C��������g�p�I�ʉ��s�B

���񖽗ߘ�"�ʉ��I" TensorFlow GraphDef �����ʉ��I TensorFlow Lite FlatBuffer�B


```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/some_quantized_graph.pb \
  --inference_type=QUANTIZED_UINT8 \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --mean_values=128 \
  --std_dev_values=127
```

### �g�p "dummy-quantization\" �ݕ��_����s�ʉ����� <a name="dummy_quant"></a>

���Đ����ʉ��I�\�I�D�C���ݕ��_��s "dummy-quantization"�B�Q��
`--default_ranges_min` �a `--default_ranges_max` �ݏ��L�s�ܗL�ő�ŏ��M���I array ���w��ő�ŏ�䗁B"Dummy-quantization" �I���x��ꍱ�C�A��ߎ����꘢���ʉ��͌^�B

�����I��q�W�����꘢�L Relu6 ���������I�͌^�B�R���C��ȓ��o�꘢�����I�ȁC�啔���I���������I䗍�[0, 6]�B

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --output_file=/tmp/foo.cc \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --inference_type=QUANTIZED_UINT8 \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --default_ranges_min=0 \
  --default_ranges_max=6 \
  --mean_values=128 \
  --std_dev_values=127
```

## ����a�o�I��

### ������

�@�����I��q�����C�Q�� `input_arrays` �ڎ�꘢�p�������u�I��\������B

���L�����I�͌^���q�����k�L�p�I�B

```
curl https://storage.googleapis.com/download.tensorflow.org/models/inception_v1_2016_08_28_frozen.pb.tar.gz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/inception_v1_2016_08_28_frozen.pb \
  --output_file=/tmp/foo.tflite \
  --input_shapes=1,28,28,96:1,28,28,16:1,28,28,192:1,28,28,64 \
  --input_arrays=InceptionV1/InceptionV1/Mixed_3b/Branch_1/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_2/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_3/MaxPool_0a_3x3/MaxPool,InceptionV1/InceptionV1/Mixed_3b/Branch_0/Conv2d_0a_1x1/Relu \
  --output_arrays=InceptionV1/Logits/Predictions/Reshape_1
```

���v���ӓI���C `input_shapes` ���p�`�������I��\�B�����C �����`�󘰊e�����������ʒu�I�����B

### ���o��

�@�����I��q�����C�Q�� `output_arrays` �ڝ��꘢�p�������u�I��\��o���B

���L���o�I�͌^���q�����k�L�p�I�B

```
curl https://storage.googleapis.com/download.tensorflow.org/models/inception_v1_2016_08_28_frozen.pb.tar.gz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/inception_v1_2016_08_28_frozen.pb \
  --output_file=/tmp/foo.tflite \
  --input_arrays=input \
  --output_arrays=InceptionV1/InceptionV1/Mixed_3b/Branch_1/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_2/Conv2d_0a_1x1/Relu
```

### �w��q

���������I�C�����s�Ȕ�w������o���C�ȕ֘����I���������q�BTensorFlow Lite
Converter �����w��q䗔V�O�I�I���������B �g�p [graph visualizations](#graph_visualizations) ���������q�I���a�o���B

���񖽗ߓW�������꘢ TensorFlow GraphDef ����昢�����B

```
curl https://storage.googleapis.com/download.tensorflow.org/models/inception_v1_2016_08_28_frozen.pb.tar.gz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/inception_v1_2016_08_28_frozen.pb \
  --output_file=/tmp/foo.pb \
  --input_shapes=1,28,28,96:1,28,28,16:1,28,28,192:1,28,28,64 \
  --input_arrays=InceptionV1/InceptionV1/Mixed_3b/Branch_1/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_2/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_3/MaxPool_0a_3x3/MaxPool,InceptionV1/InceptionV1/Mixed_3b/Branch_0/Conv2d_0a_1x1/Relu \
  --output_arrays=InceptionV1/InceptionV1/Mixed_3b/concat_v2
```

���ӁCTensorFlow Lite FlatBuffers ���I�ŕ\���I���x������ TensorFlow GraphDef ���I�\�����x�X�e�B��@�C�R�� TensorFlow GraphDef ���C�꘢�S�ڒʏ��\�������l���ƓI op (�`�C�阩�@�C�Βu�ډ��CRelu�c)�C�A�݊�I�ŕ\���a�ŏ�I�\�����C���ʏ��\�����g�����Iop�h�B

�R�����x�e�C�ꍱ���I�� (��@ TensorFlow GraphDef ���阩�a�Βu���V�I��)����P�B

���g�p`--input_arrays` �a `--output_arrays`�w�蒆���C��䦁i�L���K�j�w��ݍ����@�����I�Ō`���I���ۗ��I���B���ʏ퐥���������I�o�i���݈ꒆ�C���L�݌��������O�o�I�����s�����퍬���j�B

## ���u


## ��

����o Graphviz Dot �i���C�g�p`--output_format` �Q������
`--dump_graphviz_dir`�Q�����n�s���B���ʓI���T�q�������p��B

### �g�p `--output_format=GRAPHVIZ_DOT` <a name="using_output_format_graphviz_dot"></a>

���� Graphviz �I�������� GRAPHVIZ_DOT` �Q����
`�A`output_format`�B���������B������~�ᗹ�� TensorFlow GraphDef �a TensorFlow Lite FlatBuffer �I�v���B���� TFLite �I���C�����쐥�k�L�p�I�B

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --output_file=/tmp/foo.dot \
  --output_format=GRAPHVIZ_DOT \
  --input_shape=1,128,128,3 \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1
```

�����I`.dot` �����Ȏg�p�ȉ����ߐ�pdf�����F

```
dot -Tpdf -O /tmp/foo.dot
```

�����I `.dot.pdf` �����ȍݔC�� PDF ���ŁC�A�䌚�g�p�꘢�\�ݑ�ʏ�����@�I�ōH��C��@ Google Chrome �F

```
google-chrome /tmp/foo.dot.pdf
```

�݉��ꒆ�݊Ŏ���I PDF�B

### �g�p `--dump_graphviz_dir`

���� Graphviz �I�@���� `dump_graphviz_dir`�Q���C��w��ۑ����ʕ����I�ږځB

�a�O�꘢���@�s���I���C�����@�ۗ������n�o�i���B���񋟗��R���萶���I���I���B

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --output_file=/tmp/foo.tflite \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --dump_graphviz_dir=/tmp
```

�����쏫�ݖڕ����������ꍱ�����B �����C���ŏd�v�I������ `toco_AT_IMPORT.dot` �a`/tmp/toco_AFTER_TRANSFORMATIONS.dot`�B
`toco_AT_IMPORT.dot` ��������ܓI���n�C������ݓ��A�튮���B�R�����_�I�M���L���C

�v�����I���ʕs�D�����B������ݖ��ߎ��\���L�p�B

`toco_AFTER_TRANSFORMATIONS.dot` �ܗL�͌^�ݔ�o�V�O�C���ݍs�����L�I�V�@�I�M���B

�ʏ�C�������䏬�C����ܘ��_�X���I�M���B

�a�V�O��C�������Ȕ��PDF�����F

```
dot -Tpdf -O /tmp/toco_*.dot
```

����o�����@�������B���v���ӓI���C���W���I�s���ЉE��p�I���꘢
`AveragePool` �_�B

<table><tr>
  <td>
    <a target="_blank" href="https://storage.googleapis.com/download.tensorflow.org/example_images/toco_AT_IMPORT.dot.pdf">
      <img src="../images/convert/sample_before.png"/>
    </a>
  </td>
  <td>
    <a target="_blank" href="https://storage.googleapis.com/download.tensorflow.org/example_images/toco_AFTER_TRANSFORMATIONS.dot.pdf">
      <img src="../images/convert/sample_after.png"/>
    </a>
  </td>
</tr>
<tr><td>before</td><td>after</td></tr>
</table>

### ���g���h����u

���g�p `--dump_graphviz_dir` ���߁C�ʏ��ē��꘢
`dump_graphviz_video`���߁B�����ߎg�����@�C�s��ۑ��꘢���g���Ɓh�B�\�v���v����푽�I�������B
�ʏ�C�l�ʊō�����������I�����B

### �`���I�� <a name="graphviz_legend"></a>

*   �g����h�F��:
    *   �啔���I����ŋN������
        <span style="background-color:#db4437;color:white;border:1px;border-style:solid;border-color:black;padding:1px">bright
        red</span>�B
    *   �ꍱ�d�ʑ��� (��@��)�ŋN������
        <span style="background-color:#c53929;color:white;border:1px;border-style:solid;border-color:black;padding:1px">darker
        red</span>�B
*   ���ŋN������:
    *   ��ʐ�
        <span style="background-color:#4285f4;color:white;border:1px;border-style:solid;border-color:black;padding:1px">blue</span>�B
    *   ������
        *   ���� (��) ������
            <span style="background-color:#f5f5f5;border:1px;border-style:solid;border-color:black;border:1px;border-style:solid;border-color:black;padding:1px">light
            gray</span>�B
        *   ��w�� `--input_arrays` ��`--output_arrays` �I������
            <span style="background-color:#9e9e9e;border:1px;border-style:solid;border-color:black;padding:1px">dark
            gray</span>�B
    *   RNN �I�󐔐��F�I�B �R���펮�n�\��RNN�I��C��RNN ���\�����F��:
        *   ��RNN����I������ (��@�C�����I���e�ݔ�Z�@����RNN�I�󐔁j�C�����ŋN������
            <span style="background-color:#b7e1cd;border:1px;border-style:solid;border-color:black;padding:1px">light
            green</span>�B
        *   �I RNN �󐔊ŋN����
            <span style="background-color:#0f9d58;color:white;border:1px;border-style:solid;border-color:black;padding:1px">dark
            green</span>�B����RNN��X�V�I�ځB