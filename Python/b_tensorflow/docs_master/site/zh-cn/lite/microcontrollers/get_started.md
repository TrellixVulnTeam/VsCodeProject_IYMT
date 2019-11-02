# ���T�����

�{���������n�g�p�p�����T����I Tensorflow Lite�B

����s��I[����](#����)

���ӁF�@�ʎ��v�꘢���C�䌚�g�p 
[�R Tensorflow �񋟋Z�x���I SparkFun Edge](https://www.sparkfun.com/products/15170)�B
�����^ Tensorflow Lite ����I�C�ݔ��T�����s�[�x�w�񋟗����I����B

�L�s���f������I��C�Q�����I*�s���f*����

## ����

���ʙ{�����቉�����@���g�p Tensorflow Lite ���Ɠ�������w�p�����F

### Hello World ����

�{����|�݉����� Tensorflow Lite �p�����T����I��m�B������͌^�A���͌^�ȋ� Tensorflow Lite �g�p�ȋy�ݔ��T�����s���f�I�����[���[�H�여���B

�ݘ����ᒆ�C�꘢�͌^��p���͐��������B���������T�����C���p�� LED ���ҍT����B

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/hello_world">Hello
World ����</a>

������܈꘢�����@���a�͌^�I Jupyter notebook�F

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/hello_world/create_sine_model.ipynb">create_sine_model.ipynb</a>

�w��[�g���^�͌^�h](build_convert.md)�������a�͌^�I�����B

�v���𐄒f���@���s�I�C�� [hello_world_test.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/hello_world/hello_world_test.cc)�B

����݈ȉ������s���F

-   [�R Tensorflow �񋟋Z�x���I SparkFun Edge(Apollo3 Blue)](https://www.sparkfun.com/products/15170)
-   [Arduino MKRZERO](https://store.arduino.cc/usa/arduino-mkrzero)
-   [STM32F746G �T���iDiscovery Board�j](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)
-   Mac OS X

### ��������

������g�p�꘢�I
[���͌^](https://www.tensorflow.org/tutorials/sequences/audio_recognition)
�������I���B����㘸�I�������߉��B�͌^�ʉ��s�����营�ہg���h���g�ۈ�B

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/micro_speech">��������</a>

[�g�s���f�h](#�s���f) ��������������I���𑴍H�쌴���B

����݈ȉ������s���F

-   [�R Tensorflow �񋟋Z�x���I SparkFun Edge(Apollo3 Blue)](https://www.sparkfun.com/products/15170)
-   [STM32F746G �T���iDiscovery Board�j](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)
-   Mac OS X

���ӁF��v�n�g�p SparkFun Edge �C�䌚���z[�g�ݎg�p SparkFun Tensorflow �I���T�����s����w�h](https://codelabs.developers.google.com/codelabs/sparkfun-tensorflow)�����`�q�I����,���꘢����H�여���I�㎺�icodelab�j�B

### ������

�{����W�����@���g�p Tensorflow Lite �s�꘢ 25 �����I�_㤗��R�������I�����I�l�B����퐬�ȍ݋�L���ʓ����I�n��s�C�@���T����a DSP�B

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/micro_vision">������</a>

����݈ȉ������s���F

-   [�R Tensorflow �񋟋Z�x���I SparkFun Edge(Apollo3 Blue)](https://www.sparkfun.com/products/15170)
-   [STM32F746G �T���iDiscovery Board�j](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)
-   Mac OS X

## �s���f

�ȉ���������[����](#��������)���ᒆ�I [main.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/main.cc) ������𗹛��@���g�p�p�����T����I Tensorflow Lite ���s���f�B

### ���

�v�g�p�C�K��܈ȉ������F

```C++
#include "tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h"
#include "tensorflow/lite/experimental/micro/micro_error_reporter.h"
#include "tensorflow/lite/experimental/micro/micro_interpreter.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "tensorflow/lite/version.h"
```

-   [`all_ops_resolver.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h)
    �񋟉���iinterpreter�j�p���s�͌^�I����B
-   [`micro_error_reporter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_error_reporter.h)
    �o�M���B
-   [`micro_interpreter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_interpreter.h)
    ��ܗ��a�s�͌^�I��B
-   [`schema_generated.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema_generated.h)
    ��� TensorFlow Lite
    [`FlatBuffer`](https://google.github.io/flatbuffers/) �͌^�����i���I�͎��B
-   [`version.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/version.h)
    �� Tensorflow Lite �˓I�Ŗ{�M���B

���������ꍱ�����B�ȉ������ŏd�v�I�F

```C++
#include "tensorflow/lite/experimental/micro/examples/micro_speech/feature_provider.h"
#include "tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/micro_model_settings.h"
#include "tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/tiny_conv_micro_features_model_data.h"
```

-   [`feature_provider.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/feature_provider.h)
    ��ܘ����������v�����͌^���I�����I��B
-   [`tiny_conv_micro_features_model_data.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/tiny_conv_micro_features_model_data.h)
    ��ܑ� `char` ���I�͌^�B
    [�g���^�͌^�h](build_convert.md) ������@���� Tensorflow Lite �͌^�i���B
-   [`micro_model_settings.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/micro_model_settings.h)
    ��^�͌^���I�e��ʁB

### �u���u

�v�u���u�C���v�g�p�꘢�w�� `tflite::MicroErrorReporter` ��I�w�����꘢ `tflite::ErrorReporter` �w�F

```C++
tflite::MicroErrorReporter micro_error_reporter;
tflite::ErrorReporter* error_reporter = &micro_error_reporter;
```
�ʔ퓞����iinterpreter�j���C����򛀎ʓ��u�B�R�����T����ʏ��L�����u�����C`tflite::MicroErrorReporter` �I���I���菊�萧�I�B

### ���͌^

�݈ȉ��㒆�C�͌^�����꘢ `char` �����ቻ�I�C`g_tiny_conv_micro_features_model_data` �i�v���𑴐��@�����I�C�Q[�g���^�͌^�h](build_convert.md)�j�B ���@��͌^���ۑ��˔Ŗ{�^��g�p�I�Ŗ{�����e�F

```C++
const tflite::Model* model =
    ::tflite::GetModel(g_tiny_conv_micro_features_model_data);
if (model->version() != TFLITE_SCHEMA_VERSION) {
  error_reporter->Report(
      "Model provided is schema version %d not equal "
      "to supported version %d.\n",
      model->version(), TFLITE_SCHEMA_VERSION);
  return 1;
}
```
### �ቻ�����͊�

����iinterpreter�j���v�꘢ [`AllOpsResolver`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h) �ᗈ Tensorflow ����B�ȓW���Ȍ��I�ړY�����葀��F

```C++
tflite::ops::micro::AllOpsResolver resolver;
```

### ���z����

����v����A�o�ȋy�������z���I�����B���z�I�������꘢�召 `tensor_arena_size` �I `uint8_t` ���C���� `tflite::SimpleTensorAllocator` ��F

```C++
const int tensor_arena_size = 10 * 1024;
uint8_t tensor_arena[tensor_arena_size];
tflite::SimpleTensorAllocator tensor_allocator(tensor_arena,
                                               tensor_arena_size);
```

���ӁF���������召��r���g�p�I�͌^�C�\���v�ʗ���B

### �ቻ����iInterpreter�j

�䌚�꘢ `tflite::MicroInterpreter` ��C�V�O���I�ʁF

```C++
tflite::MicroInterpreter interpreter(model, resolver, &tensor_allocator,
                                     error_reporter);
```

### ���x

`MicroInterpreter` ��Ȓʗp `.input(0)` ��񋟈꘢�w���͌^���ʓI�w�C���� `0` ��\��꘢�i�琥�B��꘢�j���ʁB�䘢�ʈț��I�x�^�^���䏊���]�I�F

```C++
TfLiteTensor* model_input = interpreter.input(0);
if ((model_input->dims->size != 4) || (model_input->dims->data[0] != 1) ||
    (model_input->dims->data[1] != kFeatureSliceCount) ||
    (model_input->dims->data[2] != kFeatureSliceSize) ||
    (model_input->type != kTfLiteUInt8)) {
  error_reporter->Report("Bad input tensor parameters in model");
  return 1;
}
```

�ݘ���i���C�� `kFeatureSliceCount` �a `kFeatureSliceSize` �^���I�������C����� [`micro_model_settings.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/micro_model_settings.h) ���B�� `kTfLiteUInt8` �� Tensorflow Lite �^�ꐔ���^�I���p�C����� [`c_api_internal.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/c/c_api_internal.h) ���B

### ��������

������͌^���I�����K�R���T����I���������B[`feature_provider.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/feature_provider.h) ����I `FeatureProvider` �߉��󏫑��ꏫ����͌^�I�����W���B����ቻ�C��p�V�O��I `TfLiteTensor` �����꘢�w�������I�w�B`FeatureProvider` �g�p�����U�[���͌^�I�������F

```C++
  FeatureProvider feature_provider(kFeatureElementCount,
                                   model_input->data.uint8);
```

�ȉ���g `FeatureProvider` ���ŋ߈�b�I�������������U�[���ʁF

```C++
TfLiteStatus feature_status = feature_provider.PopulateFeatureData(
    error_reporter, previous_time, current_time, &how_many_new_slices);
```

�ݍ���q���C���������a���f���݈꘢�z�����I�C�����\�s�f�n�ߑ��a���V�I���B

���ݎʎ��ȓI�����C�\��ȑ����I�������������C�A���v�ݍs�͌^�V�O�A�p�����U�[���ʁB

### �s�͌^

�v�s�͌^�C��ȍ� `tflite::MicroInterpreter` ���p `Invoke()`�F

```C++
TfLiteStatus invoke_status = interpreter.Invoke();
if (invoke_status != kTfLiteOk) {
  error_reporter->Report("Invoke failed");
  return 1;
}
```

��ȕԉ� `TfLiteStatus` �Ȓ�s���ې����B�� [`c_api_internal.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/c/c_api_internal.h) ����I `TfLiteStatus` �I�\�L `kTfLiteOk` �a `kTfLiteError`�B

### ��o

�͌^�I�o�ʉȒʍ� `tflite::MicroIntepreter` ��p `output(0)` ���C���� `0` ��\��꘢�i�琥�B��꘢�j�o�ʁB

�ݎ��ᒆ�C�o���꘢���C�\���������s���i�g���h�iyes�j�A�g�ہh�ino�j�A�g���m�h�iunknown�j�ȋy�g���ҁh�isilence�j�j�I�T���B�R�������ƏW�����r��I�C��Ȏg�p�I����T���ō��I�F

```C++
    TfLiteTensor* output = interpreter.output(0);
    uint8_t top_category_score = 0;
    int top_category_index;
    for (int category_index = 0; category_index < kCategoryCount;
         ++category_index) {
      const uint8_t category_score = output->data.uint8[category_index];
      if (category_score > top_category_score) {
        top_category_score = category_score;
        top_category_index = category_index;
      }
    }
```

�ݎ��ᑴ���������C�g�p���꘢�X���I�Z�@���������I�ʁB������ [recognize_commands.h](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/recognize_commands.h) ���L����B�ݗ��C���I�������C��Ȏg�p�����I�Z���񍂉��ϐ��B

## ����

����s����@�C�ȉ������F

*   ��[�g���^�͌^�h](build_convert.md)������@���g�p�͌^�B
*   ��[�g����C++�h](library.md)�������X���� C++ �I���e�B
