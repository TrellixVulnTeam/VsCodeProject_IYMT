#  TensorFlow Lite ��GPU����

[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)�x�����d��������B�{������@���݈���n�i�v��OpenGL ES 3.1���X���Ŗ{�j�aiOS�i�v��iOS 8 ���X���Ŗ{�j�IGPU�@�[�ibackend�j�g�pTensorFLow Lite delegate APIs�B

## �g�pGPU�����I

### ���x

GPUs ��L���f�ʁA��͛�s���I�H��iworkloads�j�B�����C����퍇���꘢�R��ʎZ�����I�[�x�_㤁C�����꘢GPU�s�ȗ��ꍱ���ʁitensor�j�󊎗e�Օ����I�H��iworkloads�j�C�R�@��s�s�B��s���ʏ�\�L��I���B�ݍōD�I��v���C��GPU�㐄�f�iinference�j�ȍs�������C�Ȓ����C�݈ȑO���s�\�I�B

### ���x

GPU�g�p16�ʈ�32�ʕ��_���s�Z�C�󊎁i�^CPU�s���j�s���v�ʉ��iquantization�j�ȓ��ŉ��I���\�B�@�ʐ��x�~��g���͌^�I�ʉ��iquantization�j�ٖ@���v���C�ߍ�GPU��s�_㤉\�ȏ����S�B

### �\��

�g�pGPU�s���f�iinference�j�I�꘢�D�ݘ����I�\���BGPU�\�Ȕ��L���a�����@���s�Z�C���CPU��s�����C���ՍX���I�\���󐶍X���I�ʁB

### �x���IOps

TensorFlow Lite ��GPU��x��16�ʘa32�ʕ��_���x���I�ȉ�����F

* `ADD v1`
* `AVERAGE_POOL_2D v1`
* `CONCATENATION v1`
* `CONV_2D v1`
* `DEPTHWISE_CONV_2D v1-2`
* `FULLY_CONNECTED v1`
* `LOGISTIC v1`
* `MAX_POOL_2D v1`
* `MUL v1`
* `PAD v1`
* `PRELU v1`
* `RELU v1`
* `RELU6 v1`
* `RESHAPE v1`
* `RESIZE_BILINEAR v1`
* `SOFTMAX v1`
* `STRIDED_SLICE v1`
* `SUB v1`
* `TRANSPOSE_CONV v1`

## ��{�p�@

### Android (Java)

�g�p`TfLiteDelegate`��GPU��sTensorFlow Lite�C��Java���C�Ȓ�`Interpreter.Options`���w��GpuDelegate�B

```java
// NEW: Prepare GPU delegate.
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);

// Set up interpreter.
Interpreter interpreter = new Interpreter(model, options);

// Run inference.
writeToInputTensor(inputTensor);
interpreter.run(inputTensor, outputTensor);
readFromOutputTensor(outputTensor);

// Clean up.
delegate.close();
```

### Android (C/C++)

��Android GPU��g�pC/C++���ITensorFlow Lite�C�Ȏg�p`TfLiteGpuDelegateCreate()`���C��g�p`TfLiteGpuDelegateDelete()`�B

```c++
// Set up interpreter.
auto model = FlatBufferModel::BuildFromFile(model_path);
if (!model) return false;
ops::builtin::BuiltinOpResolver op_resolver;
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, op_resolver)(&interpreter);

// NEW: Prepare GPU delegate.
const TfLiteGpuDelegateOptions options = {
  .metadata = NULL,
  .compile_options = {
    .precision_loss_allowed = 1,  // FP16
    .preferred_gl_object_type = TFLITE_GL_OBJECT_TYPE_FASTEST,
    .dynamic_batch_enabled = 0,   // Not fully functional yet
  },
};
auto* delegate = TfLiteGpuDelegateCreate(&options);
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
if (interpreter->Invoke() != kTfLiteOk) return false;
ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));

// NEW: Clean up.
TfLiteGpuDelegateDelete(delegate);
```

�p��Android C / C ++�ITFLite GPU�g�p[Bazel](https://bazel.io)���n�B��@�C�Ȏg�p�ȉ����ߌ��ϑ�idelegate�j�F

```sh
bazel build -c opt --config android_arm64 tensorflow/lite/delegates/gpu:gl_delegate                  # for static library
bazel build -c opt --config android_arm64 tensorflow/lite/delegates/gpu:libtensorflowlite_gpu_gl.so  # for dynamic library
```

### iOS(ObjC++)

�v��GPU��sTensorFlow Lite�C���v��`NewGpuDelegate()`GPU�ϑ�idelegate�j�C�R�@����`Interpreter::ModifyGraphWithDelegate()`�i���s���p`Interpreter::AllocateTensors()`�j

```c++
// Set up interpreter.
auto model = FlatBufferModel::BuildFromFile(model_path);
if (!model) return false;
tflite::ops::builtin::BuiltinOpResolver op_resolver;
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, op_resolver)(&interpreter);

// NEW: Prepare GPU delegate.

const GpuDelegateOptions options = {
  .allow_precision_loss = false,
  .wait_type = kGpuDelegateOptions::WaitType::Passive,
};

auto* delegate = NewGpuDelegate(options);
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
if (interpreter->Invoke() != kTfLiteOk) return false;
ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));

// Clean up.
DeleteGpuDelegate(delegate);
```

���ӁF�p`Interpreter::ModifyGraphWithDelegate()`��`Interpreter::Invoke()`�C�p�ҕK�ݓ��O�����L�꘢`EGLContext`�C�󊎘����꘢`EGLContext`���p`Interpreter::Invoke()`�B�@��`EGLContext`�s���݁C�ϑ�idelegate�j���ݓ������꘢�C�A���l�K�ێn���p`Interpreter::Invoke()`�I���꘢���p`Interpreter::ModifyGraphWithDelegate()`�B

## ���p�@

### �ϑ�iDelegate�jiOS 

`NewGpuDelegate()`�ڎ�꘢ `struct` �B

```c++
struct GpuDelegateOptions {
  // Allows to quantify tensors, downcast values, process in float16 etc.
  bool allow_precision_loss;

  enum class WaitType {
    // waitUntilCompleted
    kPassive,
    // Minimize latency. It uses active spinning instead of mutex and consumes
    // additional CPU resources.
    kActive,
    // Useful when the output is used with GPU pipeline then or if external
    // command encoder is set
    kDoNotWait,
  };
  WaitType wait_type;
};
```

��`nullptr``NewGpuDelegate()`�C��u�ҁi���ݏ�ʓI��{�p�@���ᒆ�q�j�B

```c++
// THIS:
const GpuDelegateOptions options = {
  .allow_precision_loss = false,
  .wait_type = kGpuDelegateOptions::WaitType::Passive,
};

auto* delegate = NewGpuDelegate(options);

// IS THE SAME AS THIS:
auto* delegate = NewGpuDelegate(nullptr);
```

�R�g�p`nullptr`�k���ցC�A�䌚�w��u�C�Ȕ�ƍ݈ȍ@�X���ҏo�C�����v�B

### ��/�o�t��

�v�z��GPU��s�Z�C�����K�\GPU�B�ʏ���v�s�������B�@�ʉȓI�C�ōD�s�v����CPU / GPU�����E�C�����p��ʁB�ʏ허�C�������s��ƓI�C�A�ݖ^�������v���C�ȍ��������꘢�B

�@��㤓I�����߉���GPU�������I���i��@�C��ܑ����IGPU���j�C�߉Ȓ��ڕۗ���GPU���������َ�����CPU�����B���C�@��㤓I�o�їp�����I�i���i��@�C [image style transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)_)�C�ߛ��Ȓ��ڎ��ݛ�����B

�����ŉ����\�CTensorFlow Lite�p�Ȓ��ڎ�a�ʓ�TensorFlow�d���t����ƓI�������{�B

#### Android

�������GPU���풆�C�K��揫��OpenGL���F�푶�t��ہiSSBO�j�B�Ȏg�p`Interpreter.bindGlBufferToTensor()`��TfLiteTensor�^�p�y�ISSBO���B���ӁF`Interpreter.bindGlBufferToTensor()`�K��`Interpreter.modifyGraphWithDelegate()`�V�O�p�B

```java
// Ensure a valid EGL rendering context.
EGLContext eglContext = eglGetCurrentContext();
if (eglContext.equals(EGL_NO_CONTEXT)) return false;

// Create an SSBO.
int[] id = new int[1];
glGenBuffers(id.length, id, 0);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, id[0]);
glBufferData(GL_SHADER_STORAGE_BUFFER, inputSize, null, GL_STREAM_COPY);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);  // unbind
int inputSsboId = id[0];

// Create interpreter.
Interpreter interpreter = new Interpreter(tfliteModel);
Tensor inputTensor = interpreter.getInputTensor(0);
GpuDelegate gpuDelegate = new GpuDelegate();
// The buffer must be bound before the delegate is installed.
gpuDelegate.bindGlBufferToTensor(inputTensor, inputSsboId);
interpreter.modifyGraphWithDelegate(gpuDelegate);

// Run inference; the null input argument indicates use of the bound buffer for input.
fillSsboWithCameraImageTexture(inputSsboId);
float[] outputArray = new float[outputSize];
interpreter.runInference(null, outputArray);
```

���I���@�ȗp���o��(tensor)�B�ݏ�v���C`Interpreter.Options.setAllowBufferHandleOutput(true)`��p���C���֗p��GPU������CPU�����I㤏o���I�ґ���B

```java
// Ensure a valid EGL rendering context.
EGLContext eglContext = eglGetCurrentContext();
if (eglContext.equals(EGL_NO_CONTEXT)) return false;

// Create a SSBO.
int[] id = new int[1];
glGenBuffers(id.length, id, 0);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, id[0]);
glBufferData(GL_SHADER_STORAGE_BUFFER, outputSize, null, GL_STREAM_COPY);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);  // unbind
int outputSsboId = id[0];

// Create interpreter.
Interpreter.Options options = (new Interpreter.Options()).setAllowBufferHandleOutput(true);
Interpreter interpreter = new Interpreter(tfliteModel, options);
Tensor outputTensor = interpreter.getOutputTensor(0);
GpuDelegate gpuDelegate = new GpuDelegate();
// The buffer must be bound before the delegate is installed.
gpuDelegate.bindGlBufferToTensor(outputTensor, outputSsboId);
interpreter.modifyGraphWithDelegate(gpuDelegate);

// Run inference; the null output argument indicates use of the bound buffer for output.
ByteBuffer input = getCameraImageByteBuffer();
interpreter.runInference(input, null);
renderOutputSsbo(outputSsboId);
```

#### iOS

�������GPU���풆�C�K��揫��Metal�I`MTLBuffer`�ہB�ȏ�TfLiteTensor�^�p�y�I`MTLBuffer`�a`BindMetalBufferToTensor()`���B���ӁF�K��`Interpreter::ModifyGraphWithDelegate()`�V�O�p`BindMetalBufferToTensor()`�B���O�C�ҏ�v���C���f�iinference�j�ʓI�o�C�GPU��������CPU�����B�ݏ��n�����p`Interpreter::SetAllowBufferHandleOutput(true)`�ȑ���B

```c++
// Prepare GPU delegate.
auto* delegate = NewGpuDelegate(nullptr);
interpreter->SetAllowBufferHandleOutput(true);  // disable default gpu->cpu copy
if (!BindMetalBufferToTensor(delegate, interpreter->inputs()[0], user_provided_input_buffer)) return false;
if (!BindMetalBufferToTensor(delegate, interpreter->outputs()[0], user_provided_output_buffer)) return false;
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
if (interpreter->Invoke() != kTfLiteOk) return false;
```

���ӁF��U��GPU��������CPU�����I����@�C�����f�iinference�j�ʏo��GPU��������CPU�������v���o�ʎ��p`Interpreter::EnsureTensorDataIsReadable()`�B

## �񎦗^�Z�I

* ��CPU��s�ꍱ���s�����I����\���v��퍂�I����C栔@�e�`���Ireshape����i�`BATCH_TO_SPACE`�C`SPACE_TO_BATCH`�C`SPACE_TO_DEPTH`�a�������I����j�B�@�ʕs���v������i��@�g�p�����쐥��������㤉˘a���𐮘��n�A�s��e�o�j�C�ߓ������Ȓ񍂐��\�B
* ��GPU��C�ʁitensor�j�����핪4���ʓ��ichannel�j�B�����`��`[B, H, W, 5]` �I�ʁitensor�j�I�Z�ʑ�v�^`[B, H, W, 8]`�����C�A����`[B, H, W, 4]`�v��B
  * ��@�F�@�ʑ����I�d���x��RGBA�C��4�ʓ��ichannel�j�����I���x�v�������C���Ȕ�Ɠ������i��3�ʓ�RGB��4�ʓ�RGBX�j�B
* �����ŉ����\�C�s�v๘��g�p�ډ��imobile-optimized�j�I㤉ˏd�V�I����B �����f�iinference�j���I�d�v�����B

