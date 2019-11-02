# TensorFlow Lite GPU �㗝

[TensorFlow Lite](https://www.tensorflow.org/lite) �x�����d��������B�{�����`�q���@���� Android �a iOS ��g�p TensorFlow Lite �I�㗝 APIs �����I GPU �@�[���\�B

GPU ���p���������f�ʓI��͛�s�H��I�B�����C����퍇�p�ݕ�ܑ�ʎZ���I�_㤏�C�ꍱ���ʉȗe�ՓI�핪�X���I�H�슎�ȓ��s�C�ʏ��v�X��I���B�ݍŉ���v���C�p GPU �ݗp������������Z�߉ȍs�I�����C���݈ȑO���s�\�I�B

�s���� CPU �I���CGPU �ȎZ 16 �ʕ��_������ 32 �ʕ��_���� GPU �s���v�ʉ������ŉ��I�n���\�B

�g�p GPU �������Z�L�꘢�D�A�����I�\�������BGPU �ȈȔ�퍂���a���I�������s�Z�C���� GPU �݊����a CPU ��I�C�ȏ��ՍX���I�͘a���X���I�ʁB

## �����p��������

�œI GPU �㗝�I���@�A������ʓI�����C���������䐮���g�p GPU ���I�������p�����BGPU ��ݑ��L�񐧓I�`���C�A���k���A��B��U���𗹔@���c��I���������s�N���C�A�ȍݎ��ȓI�͌^��B

### Android�i�g�p Android Studio�j

�@�ʎ��v�꘢������, ��
[�p�� Android �I�� GPU �㗝](https://youtu.be/Xkhgre8r5G0) �I�B

���ӁF���v OpenGL ES 3.1���ҍX���Ŗ{

#### ��� ���� TensorFlow �I������ Android Studio ����

```
git clone https://github.com/tensorflow/tensorflow
```

#### ���  `app/build.gradle` �������g�p nightly �Ŗ{�I GPU AAR

�ݗL�I `dependencies` �͛ߗL�I `tensorflow-lite` ��I�ʒu���Y�� `tensorflow-lite-gpu` ��B

```
dependencies {
    ...
    implementation 'org.tensorflow:tensorflow-lite:0.0.0-nightly'
    implementation 'org.tensorflow:tensorflow-lite-gpu:0.0.0-nightly'
}
```

#### ��O. �a�s

�_ Run ���s�p�����B���s�p�����I���œ��꘢�p GPU �I�B���p�������ʉ��͎������_�͎��@�_ GPU �@�C�������� GPU ��s�B

![�s Android gpu �����p�����a�ؓ� GPU](images/android_gpu_demo.gif)

### iOS (�g�p XCode)

�@�ʎ��v�꘢������, ��
[�p�� iOS �I�� GPU �㗝](https://youtu.be/Xkhgre8r5G0) �I�B

���ӁF���v XCode 10.1 ���ҍX���Ŗ{

#### ���. �扉���p�����I����ۛ��ߔ�

���Ɖ�I iOS �����p����[����](https://www.tensorflow.org/lite/demo_ios)�B��v�L�C���IiOS�����p�������@���݉�I�����s�I�B

#### ���. �C�� Podfile �������g�p TensorFlow Lite GPU CocoaPod

�䌚���꘢��� GPU �㗝�I�� CocoaPod �����B�@�ʎ��v�ؓ��H����g�p���C�C��
`tensorflow/tensorflow/lite/examples/ios/camera/Podfile` �������g�p  `TensorFlowLiteGpuExperimental` �I pod �֑� `TensorFlowLite`�B

```
target 'YourProjectName'
  # pod 'TensorFlowLite', '1.12.0'
  pod 'TensorFlowLiteGpuExperimental'
```

#### ��O. �p GPU �㗝

���ۑ��g�p GPU �㗝�C���v�� `CameraExampleViewController.h` �I
`TFLITE_USE_GPU_DELEGATE` �� 0 �C�� 1 �B

```c
#define TFLITE_USE_GPU_DELEGATE 1
```

#### ��l. �a�s�����p����

�@�ʊ�������ʓI�C�߉ȍs���p�������B

#### ���. �z�͎�

�ݑ�l���ݖ͎����s�I�p�����C�����X�D�I���\�\�C�g�p���I�ŉ� Metal �u���p�������z�Ŗ{�B�����v���ӓI���C���v�C�����u `Product > Scheme > Edit
Scheme...`�C ` Run `�C�� ` Info ` ��C�C�� ` Build Configuration `�C�� `Debug ` �� ` Release `�C��� ` Debug executable`�B

![�u�z](images/iosdebug.png)

�R�@�_ `Options` �R�@�� `GPU Frame Capture` �C���� `Disabled`�C�� `Metal API Validation` �C���� `Disabled`�B

![�u metal ](images/iosmetal.png)

�ō@���v�ەz�Ŗ{���\�� 64 �ʌn�㌚�B�� `Project
navigator -> tflite_camera_example -> PROJECT -> tflite_camera_example -> Build
Settings` �㏫ `Build Active Architecture Only > Release` Yes�B

![�u�z](images/iosrelease.png)

## �ݎ��ȓI�͌^��g�pGPU�㗝

### Android

�ŉ����p����������@���Y���㗝�B�ݓI�p�������C����ʈ�Y�� AAR �C��`org.tensorflow.lite.gpu.GpuDelegate` �́C��g�p `addDelegate` ���\��GPU�㗝���e�����풆�B

```java
import org.tensorflow.lite.Interpreter;
import org.tensorflow.lite.gpu.GpuDelegate;

// ���n���g�p GPU �㗝�I����
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);
Interpreter interpreter = new Interpreter(model, options);

// �s����
while (true) {
  writeToInput(input);
  interpreter.run(input, output);
  readFromOutput(output);
}

// ����
delegate.close();
```

### iOS
 
�ݓI�p�����㒆�C���� GPU �㗝������`Interpreter::ModifyGraphWithDelegate` ���\�� GPU �㗝���e�����풆�B

```cpp
#import "tensorflow/lite/delegates/gpu/metal_delegate.h"

// ���n���g�p GPU �㗝�I����
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, resolver)(&interpreter);
auto* delegate = NewGpuDelegate(nullptr);  // default config
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// �s���� 
while (true) {
  WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
  if (interpreter->Invoke() != kTfLiteOk) return false;
  ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));
}

// ����
interpreter = nullptr;
DeleteGpuDelegate(delegate);
```

## �x���I�͌^�a Ops

�� GPU �㗝�z�@�C��񋟗������ȍݍ@�[�s�I�͌^�F

* [MobileNet v1 (224x224)����](https://ai.googleblog.com/2017/06/mobilenets-open-source-models-for.html) [[��]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/mobilenet_v1_1.0_224.tflite)
<br /><i>(�ژa�Ɠ����p�I�����͌^)</i>
* [DeepLab ���� (257x257)](https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html) [[��]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/deeplabv3_257_mv_gpu.tflite)
<br /><i>(�������I�����f�w��i��@�C��C�L�B�D�I�������͌^)</i>
* [MobileNet SSD ����](https://ai.googleblog.com/2018/07/accelerated-training-and-inference-with.html) [[��]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/mobile_ssd_v2_float_coco.tflite)
<br /><i>(�p�������L�y�I�ۓI�����͌^)</i>
* [PoseNet�p���p��](https://github.com/tensorflow/tfjs-models/tree/master/posenet) [[��]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/multi_person_mobilenet_v1_075_float.tflite)
<br /><i>(�p���đ������l���I�p�I�͌^)</i>

�@�ʎ��v�����I�x���I Ops �I��\�C��[����](gpu_advanced.md)�B

## �s�x���I�͌^�a ops

�@�ʈꍱ ops ��s�x�� GPU �㗝�C�y�ˑ���� GPU ��s�`�I�ꕔ���C�����I������� CPU ��s�B����v CPU/GPU ���o�k���I�g�p���C���I���s�͎���v�s�N���䐮��㤍� CPU ��s�v���B�ݏ�v���C�p����꘢���I�x���F

```
WARNING: op code #42 cannot be handled by this delegate.
```

```
�x���F���㗝�ٖ@��#42����
```

��v�L���񋟉�C���s���^�I�s�C�A�������҉Ȓ��ӓ��I�C���ȏ�����㤍ݑ㗝��s�B

## ����

�ꍱ�� CPU ��I��I�I����\�� GPU ���L�k���I��p�B�����I�ꑀ��A���k���`���I reshape ����C�� `BATCH_TO_SPACE`, `SPACE_TO_BATCH`, `SPACE_TO_DEPTH` �����B�@�ʍ� ops ����������㤉˓I�v�l�����u��㤒��C���X�D�I���\������㤒��ڏ������I�B

�� GPU ��C�ʐ����핪��4���ʓ��B�����C�Z�꘢ `[B,H,W,5]` �I�ʘa�Z `[B,H,W,8]`�I���ʐ���I�C�A�����s��s `[B,H,W,4]` �I���\�v���I���B

�����ӏ�C�@�ʑ����d���x�� RGBA �`�����C4 �ʓ������X�����Ȕ�Ɠ�����(�� 3 �ʓ� RGB �� 4 �ʓ� RGBX�j�B

�����ŉ����\�C�s�v๘��C�g�p�ډ��I㤉˗��d�V�I����B�������f���\�I�d�v�����B
