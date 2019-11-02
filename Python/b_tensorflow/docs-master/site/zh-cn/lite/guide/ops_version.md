TensorFlow Lite ����(operator)�I�Ŗ{

�{�����`�q��TensorFlow Lite�I����(operator)�Ŗ{�ˁB ����(operator)�I�Ŗ{�g�l�\���V���\�a�Q���Y�����L���쒆�B ���O�C���ۈȉ����e�F

* ���@���e���F�V�Ŗ{�I TensorFlow Lite �����ȗ����I�͌^�����B
* ���O���e���F���v�v�L�g�p�V���\�C���Ŗ{�I TensorFlow Lite �����ȗ��R�V�� TOCO �����I�V�Ŗ{�I�͌^�����B 
* �O�����e���F�@�ʋ��I TensorFlow Lite ���ܕs�x���I�V�Ŗ{�I�͌^�C���B

##����F���c(Dilation)�Y�����ɑ��쒆
�{�����I���]�����ʓW���@���ݙɑ��쒆�Y���c�n������ TFLite ������(operator)�I�Ŗ{�B

����{�������e��s���v����Ɋj�c�I�m�B���v���ӓI���F

* ���Y��2���V�I�����Q���F'dilation_width_factor' �a 'dilation_height_factor'�B  
* �s�x���c�I���Ɋj�����������q�c�n���u1�B

### �X�� FlatBuffer ��(Schema)

�v���V�Q���Y��������(operator)���C�X��`lite/schema/schema.fbs`���I�\ �B

��@�C�ɓI�\�@�������F

```
table Conv2DOptions {
  padding:Padding;
  stride_w:int;
  stride_h:int;
  fused_activation_function:ActivationFunctionType;
}
```

�ݓY���V�Q���F

* �Y�����C�w�����Ŗ{�x�����Q���B
* ���V�I��V�Y���I�Q���I�ҁC���^�����S�����B

�Y���V�Q���@�C�Q���\�@�������F

```
table Conv2DOptions {
  // �Ŗ{1�x���I�Q���F
  padding:Padding;
  stride_w:int;
  stride_h:int;
  fused_activation_function:ActivationFunctionType;

  // �Ŗ{2�x���I�Q���F
  dilation_width_factor:int = 1;
  dilation_height_factor:int = 1;
}
```

### �X��C���I�̘a���j

��TensorFlow Lite���C���j�^FlatBuffer�营���B ���j��`lite/builtin_op_data.h`����IC�I�̒���Q���B

���n�ɎQ���@���F

```
typedef struct {
  TfLitePadding padding;
  int stride_width;
  int stride_height;
  TfLiteFusedActivation activation;
} TfLiteConvParams;
```

�^FlatBuffer��(Schema)��C�ʓY�����C�w�������Ŗ{�n�x�����Q���B�ʔ@���F

```
typedef struct {
  // �Ŗ{1�x���I�Q���F
  TfLitePadding padding;
  int stride_width;
  int stride_height;
  TfLiteFusedActivation activation;

  // �Ŗ{2�x���I�Q���F
  int dilation_width_factor;
  int dilation_height_factor;
} TfLiteConvParams;
```

�O�C�X�����j��C�̒���V�Y���I�Q���B �ݍ��s�ďq�B

### �X�� FlatBuffer ��Ȏ�V�Q��

�� FlatBuffer �󐶐� C �̓I���R `lite/model.cc` �I�B

�X�V�����ȗ��V�Q���C�@�������F

```
case BuiltinOperator_CONV_2D: {
  TfLiteConvParams* params = MallocPOD<TfLiteConvParams>();
  if (auto* conv_params = op->builtin_options_as_Conv2DOptions()) {
    params->padding = parse_padding(conv_params->padding());
    params->stride_width = conv_params->stride_w();
    params->stride_height = conv_params->stride_h();
    params->activation =
        parse_activation(conv_params->fused_activation_function());
    params->dilation_width_factor = conv_params->dilation_width_factor();
    params->dilation_height_factor = conv_params->dilation_height_factor();
  }
  *builtin_data = reinterpret_cast<void*>(params);
  break;
}
```

���s���v����Ŗ{�B ���V��㞏����q�I���͌^�����C�����g�p1���ҁC�󊎐V���j���^�����j��v�n�H��B

### �X�����j���e
MutableOpResolver�i��`lite/op_resolver.h`����j�񋟗��ꍱ���e����(operator)���j�I�����B�ҏ�v���C�ŏ��a�ő�Ŗ{�s1�F
```
void AddBuiltin(tflite::BuiltinOperator op, TfLiteRegistration* registration,
                int min_version = 1, int max_version = 1);
void AddCustom(const char* name, TfLiteRegistration* registration,
               int min_version = 1, int max_version = 1);
```

���u�I����� `lite/kernels/register.cc` �����e�B �ݘ���q���C�䗹�꘢�V�I������j�C���ȗ� `Conv2D` �I�Ŗ{1�a�Ŗ{2�C���ȉ���v�����ʍs�F

```
AddBuiltin(BuiltinOperator_CONV_2D, Register_CONV_2D());
```

�C���F

```
AddBuiltin(BuiltinOperator_CONV_2D, Register_CONV_2D(), 1, 2);
```

### �� TOCO TFLite �I�o

�ō@�ꐥ TOCO �U�[(populate)�s����(operator)�����I�Œ�Ŗ{�B�ݘ���q���C���Ӗ����F

* ���c�n����1�C�U�[ �Ŗ{=1�B
* �����V�O�C�U�[ �Ŗ{=2�B

���C���v��`lite/toco/tflite/operator.cc`���d�ʒ葀��(operator)�I(class)���I`GetVersion`�����B

�����L�꘢�Ŗ{�I����C���I `GetVersion` �������F
```
int GetVersion(const Operator& op) const override { return 1; }
```

���x�������Ŗ{�C�Q�����op�I�Ŗ{�C�@�ȉ����Ꮚ���F

```
int GetVersion(const Operator& op) const override {
  const auto& conv_op = static_cast<const ConvOperator&>(op);
  if (conv_op.dilation_width_factor != 1 ||
      conv_op.dilation_height_factor != 1) {
    return 2;
  }
  return 1;
}
```

### �ϑ�

TensorFlow Lite �񋟗��꘢�ϑ� API�C�ȏ�����ϔh�d���@�[�B�� Delegate �I Prepare �������C�Ŗ{���ێx���ϔh�㒆�I���_�B
```
const int kMinVersion = 1;
TfLiteNode* node;
TfLiteRegistration;
context->GetNodeAndRegistration(context, node_index, &node, &registration);

if (registration->version > kMinVersion) {
  // �@�ʕs�x���Ŗ{�C���_�B
}
```
���g�ϔh�x���Ŗ{1�I����C�琥�K���I�C�g�ϔh�ȍݓ��X���Ŗ{���쓞�s���e���B
