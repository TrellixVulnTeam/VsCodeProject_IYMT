# �� TensorFlow ���Z��

���ӁF���\�����I�B

TensorFlow Lite �ߓ��u���k���Z���C�󊎍ݕs�f�W�C�A�����R�L�ꕔ�� TensorFlow �Z���v�L�� TensorFlow Lite �����x���B���s��x���I�Z���� TensorFlow Lite �I�͌^���ꍱ�j�́B�����͌^�I�j�́CTensorFlow Lite �ŋ߈꒼�v�͘��꘢�����\�I�B

�ѕ�������� TensorFlow Lite �g�p TensorFlow �Z���B*���ӁC�����꘢���I���\�C�󊎍ݒ��B* �ݎg�p���\�I��C�Z��[�ߒm�I�ǌ���](#�ߒm�I�ǌ���)�C�󊎏��g�p�������I���� tflite@tensorflow.org�B

TensorFlow Lite ��ژa�Ɠ�����[���u�I�Z��](ops_compatibility.md)�B�A���݁C�� TensorFlow Lite ���u�I�Z���s�I��CTensorFlow Lite �͌^�Ȏg�p���� TensorFlow �I�Z���B

TensorFlow Lite ����ݗ��@�I��� TensorFlow �Z���I�͌^�I��C��䗝����� TensorFlow Lite ���u�Z���I�͌^��p�X���I��B�󊎁CTensorFlow Lite �͌^����ܓI�C�� TensorFlow �Z���C���\�s�s��퉻�B

�ѕ�������s���I����[](#�͌^)�a[�s](#�s�͌^)��� TensorFlow �Z���I TensorFlow Lite �͌^�B�󊎗��ꍱ[�ߒm�I�ǌ���](#�ߒm�I�ǌ���)�A�����\����I[�����I](#�����I)�ȋy��{�I[���\�a��w](#���\�a��w)�B

## �͌^

���\��� TensorFlow �Z���I TensorFlow Lite �͌^�C�g�p�ʘ� [TensorFlow Lite ��](../convert/) ���I `target_spec.supported_ops` �Q���B`target_spec.supported_ops` �I�@���F

*   `TFLITE_BUILTINS` - �g�p TensorFlow Lite ���u�Z���͌^�B
*   `SELECT_TF_OPS` - �g�p TensorFlow �Z���͌^�B�ߎx���I TensorFlow �Z���I������\�ȍݔ���
    `lite/delegates/flex/whitelisted_flex_ops.cc` ���ŁB

���ӁF`target_spec.supported_ops` ���V�O Python API ���I `target_ops`�B

��搄䦎g�p `TFLITE_BUILTINS` �͌^�C�R�@�����g�p `TFLITE_BUILTINS,SELECT_TF_OPS` �C�ō@�����g�p `SELECT_TF_OPS`�B���g�p���i��A�� `TFLITE_BUILTINS,SELECT_TF_OPS`�j��p TensorFlow Lite ���u�I�Z�����x���I�Z���B�L�� TensorFlow �Z�� TensorFlow Lite ���x�������p�@�C�Ȏg�p `SELECT_TF_OPS` ����Ƌǌ����B

���ʓI����W������ Python API ���I [`TFLiteConverter`](./convert/python_api.md) ���g�p���\�B

```
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,
                                       tf.lite.OpsSet.SELECT_TF_OPS]
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

���ʓI����W�����ݖ��ߍs�H�� [`tflite_convert`](../convert/cmdline_examples.md) ���� `target_ops` ���g�p���\�B

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/foo.pb \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --target_ops=TFLITE_BUILTINS,SELECT_TF_OPS
```

�@�ʒ��ڎg�p `bazel` �a�s `tflite_convert`�C���Q�� `--define=with_select_tf_ops=true`�B

```
bazel run --define=with_select_tf_ops=true tflite_convert -- \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/foo.pb \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --target_ops=TFLITE_BUILTINS,SELECT_TF_OPS
```

## �s�͌^

�@�� TensorFlow Lite �͌^�ݓI��x�� TensorFlow select �Z���C�ߍݎg�p�I�� Tensorflow Lite �s�K��� TensorFlow �Z���I�B

### Android AAR

���֘��g�p�C�V�����꘢�x�� TensorFlow select �Z���IAndroid AAR�B�@�ʛߗL��<a href="android.md">�p�I TensorFlow Lite
��</a>�C�ȈƉ��ʓI�����x���g�p TensorFlow select �Z���I Android AAR�F

```sh
bazel build --cxxopt='--std=c++11' -c opt             \
  --config=android_arm --config=monolithic          \
  //tensorflow/lite/java:tensorflow-lite-with-select-tf-ops
```

��ʓI���߉�� `bazel-genfiles/tensorflow/lite/java/` �ډ������꘢ AAR �����B�Ȓ��ڏ��� AAR ���������ڒ��C��ȏ����z���{�n�I Maven �F

```sh
mvn install:install-file \
  -Dfile=bazel-genfiles/tensorflow/lite/java/tensorflow-lite-with-select-tf-ops.aar \
  -DgroupId=org.tensorflow \
  -DartifactId=tensorflow-lite-with-select-tf-ops -Dversion=0.1.100 -Dpackaging=aar
```

�ō@�C�ݗp�I `build.gradle` ���������v�ۗL `mavenLocal()` �ˁC�󊎎��v�p�x�� TensorFlow select �Z���I TensorFlow Lite �ˋ��֏y�I TensorFlow Lite �ˁF

```
allprojects {
    repositories {
        jcenter()
        mavenLocal()
    }
}

dependencies {
    implementation 'org.tensorflow:tensorflow-lite-with-select-tf-ops:0.1.100'
}
```

### iOS

�@�ʈ����� XCode ���ߍs�H��C�ȗp���ʓI���ߎx�� TensorFlow select �Z���I TensorFlow Lite�F

```sh
tensorflow/contrib/makefile/build_all_ios_with_tflite.sh
```

�𖽗߉�� `tensorflow/contrib/makefile/gen/lib/` �ډ����������v�I�ÐځB

TensorFlow Lite �I��������p�ȗp���s�B�꘢�V�I�x�� TensorFlow select �Z���I TensorFlow Lite XCode �ڛߓY���� `tensorflow/lite/examples/ios/camera/tflite_camera_example_with_select_tf_ops.xcodeproj` ���B

�@�ʑz�v�ݎ��ȓI�ڒ��g�p�����\�C�ȍ�������ځC��ȈƉ��ʓI�����ڍs�u�F

*   �� Build Phases -> Link Binary With Libraries ���C�Y�� `tensorflow/contrib/makefile/gen/lib/` �ڒ��I�ÁF
    *   `libtensorflow-lite.a`
    *   `libprotobuf.a`
    *   `nsync.a`
*   �� Build Settings -> Header Search Paths ���C�Y�����ʓI�H�a�F
    *   `tensorflow/lite/`
    *   `tensorflow/contrib/makefile/downloads/flatbuffer/include`
    *   `tensorflow/contrib/makefile/downloads/eigen`
*   �� Build Settings -> Other Linker Flags ���C�Y�� `-force_load
    tensorflow/contrib/makefile/gen/lib/libtensorflow-lite.a`�B
    
������z�x�� TensorFlow select �Z���I CocoaPod �B

### C++

�@�ʎg�p bazel  TensorFlow Lite �C�ȈƉ��ʓI�����Y���a�x���O�I TensorFlow �Z���I�B

*   �@�ʎ��v�́C�ȓY�� `--config=monolithic` �B
*   �����ʓI���Ē��꘢�F
    *   �ݗp `bazel build` ���� TensorFlow Lite �Y�� `--define=with_select_tf_ops=true` �B
    *   �݈˒��Y�� TensorFlow �Z���� `tensorflow/lite/delegates/flex:delegate`�B

���ӁC���v�ϑ�ړ����q�[�C�ݍs������I��A����������I `TfLiteDelegate`�C���s���v�������ϑ�^���������ϑ��B

### Python pip Package

 Python �I�x���ݓ����B

## ���\�a��w

### ���\

�@�� TensorFlow Lite �͌^���������g�p���u�Z���a TensorFlow select �Z���s�I�C�ߖ͌^�ˑR�Ȏg�p TensorFlow Lite �I���ȋy���u�I�����j�B

���\��o���� Pixel 2 �� MobileNet �I���ϐ��f�B�\���I�� 100 ���s�I���ρB�� Android ����I��Y���� `--config=android_arm64 -c opt` �B

                               | ���f (milliseconds)
------------------------------------ | -------------------
Only built-in ops (`TFLITE_BUILTIN`) | 260.7
Using only TF ops (`SELECT_TF_OPS`)  | 264.5

### �񐧕����召

���\��o���s�����������I TensorFlow Lite �񐧕����I�召�B�� Android ����I��Y���� `--config=android_arm -c opt` �B

                 | C++ �񐧕����召 | Android APK �召
--------------------- | --------------- | ----------------
Only built-in ops     | 796 KB          | 561 KB
Built-in ops + TF ops | 23.0 MB         | 8.0 MB

## �ߒm�I�ǌ���

���ʗ�o���ꍱ�ߒm�I�ǌ����F

*   �ڑO�s�x���T�����Z���B
*   �ڑO�s�x�� TensorFlow �Z���I [`post_training_quantization`](https://www.tensorflow.org/performance/post_training_quantization) �C���ȕs��C�� TensorFlow �Z���s�d�ʉ��B�@�ʖ͌^������� TensorFlow Lite �Z������� TensorFlow �Z���C�� TensorFlow Lite ���u�I�Z���I�d���Ȕ�ʉ��I�B
*   �ڑO�s�x���� HashTableV2 ���v���p���s���n���I�Z���B
*   �^�� TensorFlow ����\�s�x�� TensorFlow ��������p��/�o����B

## �����I

���ʗ�o�����ݒ��I���\�I�ꍱ���F

*   *�����e* - �L�ꐳ�݊����I�H�쐥�C��������ܓ���͌^�W�������I Tensorflow �Z���I TensorFlow Lite �񐧕������X�B
*   *�񏡉p��* - �͌^�I�����퉻�C�����v�ꎟ�������B �󊎉�񋟓I Android AAR �a iOS CocoaPod �񐧕����B
*   *�񏡐��\* - �L�ꐳ�݊����I�H�쐥�C�g�p TensorFlow �Z���I TensorFlow Lite ��L�^ TensorFlow Mobile �����I���\�B
