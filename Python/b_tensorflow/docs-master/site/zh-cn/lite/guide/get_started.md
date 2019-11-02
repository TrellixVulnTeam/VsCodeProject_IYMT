# �n�g�p TensorFlow Lite

TensorFlow Lite �񋟗� TensorFlow �͌^�C��݈ڒ[�imobile�j�A�Ɠ����iembeded�j�a��㤁iIoT�j��s TensorFlow �͌^�����I���L�H��B�ȉ��w���l�H�여���I���C��񋟗��ꖾ�I�ځB

## 1. �꘢�͌^

<a id="1_choose_a_model"></a>

TensorFlow Lite ��ݑ���s TensorFlow �͌^�BTensorFlow �͌^���ꐔ���C������ܗ��݉�r�꘢����C�����I����w㤓I�a�m�B

�L�������ȓ� TensorFlow �͌^�C���g�p�͌^�ipre-trained models�j�����ȓI�͌^�B���� TensorFlow Lite ���g�p�͌^�C�͌^�K�������i���B���ݑ��[�͌^](#2_convert_the_model_format)�����B

Note: �s�����L�I TensorFlow �͌^�s�\�� TensorFlow Lite ���s�C������iinterpreter�j���x�������ia limited subset�jTensorFlow �Z���ioperations�j�B�Q�l���[�͌^](#2_convert_the_model_format)���������e���B

### �g�p�͌^

TensorFlow Lite �񋟗���n��͌^�ipre-trained models�j�C�p����r�e����w�B���͌^�ߔ\�^ TensorFlow Lite ��N�g�p�C���ȍݓI�p�������g�p�I�͌^�B

���͌^��F

*	[�����iImage classification�j](../models/image_classification/overview.md)
*	[���́iObject detection�j](../models/object_detection/overview.md)
*	[�q�\��iSmart reply�j](../models/smart_reply/overview.md)
*	[�p�āiPose estimation�j](../models/pose_estimation/overview.md)
*	[�����iSegmentation�j](../models/segmentation/overview.md)

��[�͌^��\�iModels�j](../models)���Ŗ͌^�I������\�B

#### �������������I�͌^

�ȍݑ������n�������I TensorFlow �͌^�C� [TensorFlow Hub](https://www.tensorflow.org/hub)�B�ݑ命����v���C���͌^�s��� TensorFlow Lite �i���񋟁C�K�ݎg�p�O[�iconvert�j](#2_convert_the_model_format)���͌^�B

### �d�V�͌^�i�ڊw�j

�ڊw�itransfer learning�j��їp�D�I�͌^��d�V�ire-train�j�C�ȍs�����C�B��@�C�꘢[����](../models/image_classification/overview.md)�͌^�ȏd�V�ȐV�I���B�^���n�͌^����C�d�V�ԓI�X���C�����I�����X���B

�Ȏg�p�ڊw�C�����I�p�����萧�͌^�B��<a href="https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android">�p TensorFlow ��</a>�I codelab ���C�Ȋw�@���s�ڊw�B

### ����͌^

�@�ʛ󗹎��ȓI TensorFlow �͌^�C���җ����������������I�͌^�C�ݎg�p�O�C���v�����͌^�� TensorFlow Lite �I�i���B

## 2. �͌^

<a id="2_convert_the_model_format"></a>

TensorFlow Lite �I�|�ݍ݊e�㍂���s�͌^�B�������������ݑ��͌^�C�їp�������I�i���BTensorFlow �͌^�ݔ\�� TensorFlow Lite �g�p�O�C�K���i���B

�͌^�����͌^�����召�C��������s�e�y���iaccuracy�j�I���[�{�ioptimizations�j�B�l�ȍݍs�ꍱ���q�I��v���C�ꏬ�͌^�����召�C��񍂍s���x�B�Ȏg�p TensorFlow Lite ��iconverter�j�v�s�I���[�{�B

�� TensorFlow Lite �x������ TensorFlow �Z���ioperations�j�C���ț�񏊗L�͌^�s�\�B�Q��[ Ops ���e��](#Ops���e��)���X���M���B

### TensorFlow Lite ��

[TensorFlow Lite ��iconverter�j](../convert)���꘢���D�I TensorFlow �͌^�� TensorFlow Lite �i���I�H��B���\�������[�{�ioptimizations�j�C���ݑ�l[���I�͌^](#4_optimize_your_model_optional)����B

��� Python API �I�`���񋟁B���ʓI��q�������꘢ TensorFlow `SavedModel` �� TensorFlow Lite �i���I���F

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

�ȗp���I���@[ TensorFlow 2.0 �͌^](../convert)

�R��\��[���ߍs](../convert/cmdline_examples)�g�p��C�A����䦗p Python API �s�B

### 

��Ș��e���^�͌^�B

��[ TensorFlow 1.x �͌^](../convert/python_api.md)�C�����^�L�F

*	[SavedModel ����](https://www.tensorflow.org/guide/saved_model)
*	Frozen GraphDef (��[ freeze_graph.py ](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py)�����I�͌^)
*	[Keras](https://keras.io) HDF5 �͌^
*	�� `tf.Session` �����I�͌^

��[ TensorFlow 2.x �͌^](../convert/python_api.md)�C�����^�L�F

*	[SavedModel ����](https://www.tensorflow.org/guide/saved_model)
*	[`tf.keras` �͌^](https://www.tensorflow.org/guide/keras/overview)
*	[��̔����iConcrete functions�j](../convert/concrete_function.md)

��Ȕz�u�p�e���[�{�ioptimizations�j�C�����[�{�Ȓ񍂐��\�C�������召�B���ݑ�l[���I�͌^](#4_optimize_your_model_optional)����B

### Ops ���e��

TensorFlow Lite ���O�x��[�ꕔ���ilimited subset�j](ops_compatibility.md) TensorFlow �Z���ioperations�j�B���ڐ������\�x���S���I TensorFlow �Z���B

�@�ʊ��]�I�͌^���ܗL�s��x���I�Z���C�Ȏg�p[ TensorFlow Select](ops_select.md) ��ܗ��� TensorFlow �I�Z���B��g����������I�񐧕����X��B


## 3. �g�p�͌^�s����

<a id="3_use_the_tensorflow_lite_model_for_inference_in_a_mobile_app"></a>

*�����iInference�j* ���ʖ͌^�imodel�j�s�����idata�j�ȓ��ipredictions�j�I���B�������v�͌^�imodel�j�A����iinterpreter�j�a�������iinput data�j�B

### TensorFlow Lite ����

[TensorFlow Lite ����iinterpreter�j](inference.md)���꘢�ilibrary�j�C���ڝ��꘢�͌^�����imodel file�j�C�s�͌^�����ݓ������iinput data�j���I�Z���ioperations�j�C��񋟏o�ioutput�j�I�B

����iinterpreter�j�p����������C�񋟗��꘢�I API�C�p���� Java�ASwift�AObjective-C�AC++ �a Python �s TensorFlow Lite �͌^�B

���ʓI�㎦���� Java �p����I����:

```java
try (Interpreter interpreter = new Interpreter(tensorflow_lite_model_file)) {
  interpreter.run(input, output);
}
```

### GPU �����a�ϑ�

�ꍱ����w�Z���񋟍d�������ihardware acceleration�j�B��@�C�命������L GPU�C�� GPU �Ȕ� CPU �s�X���I���_��Z�ifloating point matrix operations�j�B

���x�񏡁ispeed-up�j�\�L���isubstantial�j���ʁB��@�C���g�p GPU �����CMobileNet v1 �����͌^�� Pixel 3 �����I�s���x�񍂗� 5.5 �{�B

TensorFlow Lite ����Ȕz�u[�ϑ�iDelegates�j](../performance/delegates.md)�ȍݕs����g�p�d�������B[GPU �ϑ�iGPU Delegates�j](../performance/gpu.md)�����ݓI GPU ��s���I�Z���B

���ʓI�㎦���� Java ���g�p GPU �ϑ�I����:

```java
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);
Interpreter interpreter = new Interpreter(tensorflow_lite_model_file, options);
try {
  interpreter.run(input, output);
}
```

�v�Y���V�d��������I�x���C��[�莩�ȓI�ϑ�](../performance/delegates.md#how_to_add_a_delegate)�B

### Android �a iOS

TensorFlow Lite ����k�e�Սݘ���v�ڕ����g�p�B�v���C[ Android ������](android.md)�a[ iOS ������](iOS.md)�w��B������C�s�L[����p����](https://www.tensorflow.org/lite/examples)�B

�v�������I�ilibraries�j�CAndroid �l�g�p[ TensorFlow Lite AAR](android.md#use_the_tensorflow_lite_aar_from_jcenter)�BiOS �l�g�p[ CocoaPods for Swift or Objective-C](ios.md#add_tensorflow_lite_to_your_swift_or_objective-c_project)�B

### Linux

�Ɠ��� Linux ���꘢��������w�I�d�v����B��[ Raspberry Pi ](build_rpi.md)�a[� Arm64 �I���](build_arm64.md)�C�@ Odroid C2�APine64 �a NanoPi�C�񋟗������B

### ���T����

[TensorFlow Lite ���T����iMicrocontrollers�j��](../microcontrollers/overview.md)���꘢ TensorFlow Lite �I�[���C�[�����L�{�玚�ikilobytes�j�����imemory�j�I���T����a�����B

### �Z��

�@�ʓI�͌^���v TensorFlow Lite �������I TensorFlow �Z���ioperations�j�C�Ȏg�p[ TensorFlow Select ](ops_select.md)�ݖ͌^���g�p���B���v���꘢��� TensorFlow �Z���I����Ŗ{����B

�ȗp[����Z���iCustom operators�j](ops_custom.md)�ʎ��ȓI�Z���ioperations�j�C�����V�Z���ڐA�iport�j�� TensorFlow Lite ���B

[�Z���Ŗ{�iOperator versions�j](ops_version.md)�\�ߗL�I�Z���Y���V�I���\�a�Q���B

## 4. ���I�͌^

<a id="4_optimize_your_model_optional"></a>

TensorFlow Lite �񋟗����͌^�召�isize�j�a���\�iperformance�j�I�H��C�ʏ�y���iaccuracy�j�e�r���B���͌^�\���v�c���I�itraining�j�C�iconversion�j���W���iintegration�j�B

����w�����꘢�s�f�W�I��CTensorFlow Lite �I[�͌^���H���iModel Optimization Toolkit�j](#�͌^���H���)�����V�Z�I�W���s�f�W�B

### ���\

�͌^���I�ڐ��ݒ��C���\�iperformance�j�A�͌^�召�imodel size�j�a�y���iaccuracy�j�I���z���t�B
[���\�ŉ��H�iPerformance best practices�j](../performance/best_practices.md)�ȏ��w���������B

### �ʉ�

�ʍ~��͌^�����ivalues�j�a�Z���ioperations�j�I���x�iprecision�j�C�ʉ��iquantization�j�ȏ��͌^�I�召�a���������I�B�k���͌^�C���L���I�y���iaccuracy�j���B

TensorFlow Lite ��ʉ� TensorFlow �͌^���B���ʓI Python ��ʉ����꘢ `SavedModel` �󏫑��ۑ��ݍd���F

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_quantized_model)
```

�v����L�ʉ��I�X���M���C�Q[�@�ʉ��iPost-training quantization�j](../performance/post_training_quantization.md)�B

### �͌^���H���

[�͌^���H���iModel Optimization Toolkit�j](../performance/model_optimization.md)���꓅�H��a�Z�C�|�ݎg�l�ȏ������I�͌^�B�R�����I���Z�ȗp�����L TensorFlow �͌^�C�����蘰 TensorFlow Lite�C�A�݌��L���I��s�����iinference�j�C�����L���B

## ����

���R�ߏn���� TensorFlow Lite�C�T���ȉ��ꍱ���F

*	�@�ʐ��ڐl�C[ Android ������](android.md)��[ iOS ������](ios.md)�B
*	�T����I[�͌^](../models)�B
*	��I[����p����](https://www.tensorflow.org/lite/examples)�B
