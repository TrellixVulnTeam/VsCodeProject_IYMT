# TensorFlow Lite �㗝

_���FDelegate API �����i�󏫐��s���B_

## �Y�� TensorFlow Lite �㗝�H

TensorFlow Lite �㗝���ꏫ�������S���I�`�Z�ϑ�\����s�I���@�B

## �Y�g�p�㗝�H

�R���ړI���\�͕s���ȋy�ʎ���C�ݑ��V��s���Z�͓I����w�͌^�I���Z���s�s�I�B

����Ɖ��d CPU�i��������j�I�S�C�ꍱ��L�@ GPU�i�`����j�� DSP�i�����M������j���I�d��������ȋ���X���I���\�^�X���I�\���B

## �g�p GPU �㗝

TensorFlow Lite �� GPU �I�񋟗��꘢ GPU �㗝�p�Ȗ͌^�Z�I�����B

�L GPU �㗝�I�T�q�C��
[TensorFlow Lite �� GPU ����](https://www.tensorflow.org/lite/performance/gpu_advanced) �B
�L�� Android �a iOS ��g�p GPU �㗝�I�����C��
[TensorFlow Lite GPU �㗝](https://www.tensorflow.org/lite/performance/gpu) �B

## �㗝���@����I�H

��䏫�꘢���I�`�{�s�@�������I����F

![�����`�{](../images/performance/tflite_delegate_graph_1.png "�����`�{")

�@�ʔc�꘢�㗝�p���s��̑���C�� TensorFlow Lite ��`����������R�㗝�s���I�q�B

��g�p�꘢�L������ Conv2D�i�Ɂj�a�Z Mean�i���ρj����I�\�͊����gMyDelegate�h�I�㗝�C�ߛ����v��X�s�@�������I����B

![�g�p�㗝�I�`�{](../images/performance/tflite_delegate_graph_2.png "�g�p�㗝�I�`�{")

�ݕԉ񒆁C����R�㗝�s���I�q�����X�֘Ďq�I�_�B

�����s���I�͌^�C���Ȉ꘢�_�C�Ӗ������L�I����㗝���ȑ����_�I�q�s���B��ʎ����C�������㗝�؎��厧�s��]�їp�R�㗝���I�����q�C������R�q��I�ՁB��C�������񐥈��S�I�B

## �@���Y�u�꘢�㗝

_���ӈȉ����їp�I API �����i�󏫐��s���B_

��㏊�q�C�Y�u�꘢�㗝���v�����ȉ��F

1.  ��꘢�p���đ㗝�q�I�j�S�_
2.  ���꘢�p�����e�j�S�_�ȋy���㗝�p�_�I�� [TensorFlow Lite �㗝](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/c/c_api_internal.h#L545)

���g�p��s���C���꘢�����s Conv2D �a�Z Mean ����I�㗝�󏫑������gMyDelegate�h�B

```
// ���s���숽�����`�I�n�B
// ��L�꘢��C��̓I�����B
class MyDelegate {
 public:
  // �@�ʑ㗝�ȗ�������C�ԉ�gtrue�h�B
  static bool SupportedOp(const TfLiteRegistration* registration) {
    switch (registration->builtin_code) {
      case kTfLiteBuiltinConv2d:
      case kTfLiteBuiltinMean:
        return true;
      default:
        return false;
    }
  }

  // �㏉�n��
  bool Init() {}
  // ���n�H�앪�z�i��@�F���z�t��j
  bool Prepare(TfLiteContext* context, TfLiteNode* node) {}
  // �㗝�q�n�s�B
  bool Invoke(TfLiteContext* context, TfLiteNode* node) {}
  // ... �Y�����������I���@
};

// �j�S�_���꘢�֑�� TfLite ���I�q�I TfLiteRegistration�B
TfLiteRegistration GetMyDelegateNodeRegistration() {
  // �������Y���� TFLite ����֛��I�q�I�㗝�_�I���n��
  // ����꘢����_�B
  // �A�ݍ��CInit �������p�����n���㗝�C�� Invoke �������p���s�㗝�B
  // �t�B
  // �������B
  TfLiteRegistration kernel_registration;
  kernel_registration.builtin_code = kTfLiteBuiltinDelegate;
  kernel_registration.custom_name = "MyDelegate";
  kernel_registration.free = [](TfLiteContext* context, void* buffer) -> void {
    delete reinterpret_cast<MyDelegate*>(buffer);
  };
  kernel_registration.init = [](TfLiteContext* context, const char* buffer,
                                   size_t) -> void* {
    // �ݓ_�I���n���i���C���n���gMyDelegate�h��B
    const TfLiteDelegateParams* delegate_params =
        reinterpret_cast<const TfLiteDelegateParams*>(buffer);
    MyDelegate* my_delegate = new MyDelegate;
    if (!my_delegate->Init(context, params)) {
      return nullptr;
    }
    return my_delegate;
  };
  kernel_registration.invoke = [](TfLiteContext* context,
                                   TfLiteNode* node) -> TfLiteStatus {
    MyDelegate* kernel = reinterpret_cast<MyDelegate*>(node->user_data);
    return kernel->Invoke(context, node);
  };
  kernel_registration.prepare = [](TfLiteContext* context,
                                    TfLiteNode* node) -> TfLiteStatus {
    MyDelegate* kernel = reinterpret_cast<MyDelegate*>(node->user_data);
    return kernel->Prepare(context, node);
  };

  return kernel_registration;
}

//  TfLiteDelegate ���@

TfLiteStatus DelegatePrepare(TfLiteContext* context, TfLiteDelegate* delegate) {
  // �����L��㗝�ēI�_�ȋy���y�ˎg�p�㗝�j�S�ցB
  // ������v��_�I�召�C�ۗ��꘢�_�B
  std::vector<int> supported_nodes(1);
  TfLiteIntArray* plan;
  TF_LITE_ENSURE_STATUS(context->GetExecutionPlan(context, &plan));
  TfLiteNode* node;
  TfLiteRegistration* registration;
  for (int node_index : TfLiteIntArrayView(plan)) {
    TF_LITE_ENSURE_STATUS(context->GetNodeAndRegistration(
        context, node_index, &node, &registration));
    if (MyDelegate::SupportedOp(registration)) {
      supported_nodes.push_back(node_index);
    }
  }
  // �u�֏��L�_�I�_�B
  supported_nodes[0] = supported_nodes.size() - 1;
  TfLiteRegistration my_delegate_kernel_registration =
      GetMyDelegateNodeRegistration();

  // �ԉ񏫕����q�C���q�C������㗝�꘢  
  // �emy_delegate_kernel_registration�f�s���B
  return context->ReplaceNodeSubsetsWithDelegateKernels(
      context, my_delegate_kernel_registration,
      reinterpret_cast<TfLiteIntArray*>(supported_nodes.data()), delegate);
}

void FreeBufferHandle(TfLiteContext* context, TfLiteDelegate* delegate,
                      TfLiteBufferHandle* handle) {
  // �p���������I���@�B
}

TfLiteStatus CopyToBufferHandle(TfLiteContext* context,
                                TfLiteDelegate* delegate,
                                TfLiteBufferHandle buffer_handle,
                                TfLiteTensor* tensor) {
  // ��L�����C�� tensor�i�ʁj�I�������㗝�I�t��B
  return kTfLiteOk;
}

TfLiteStatus CopyFromBufferHandle(TfLiteContext* context,
                                  TfLiteDelegate* delegate,
                                  TfLiteBufferHandle buffer_handle,
                                  TfLiteTensor* tensor) {
  // ���㗝�I�t�摶�������� tensor �I���n�������B
  return kTfLiteOk;
}

// �񔟐���ԉ�w�I���L�B
TfLiteDelegate* CreateMyDelegate() {
  TfLiteDelegate* delegate = new TfLiteDelegate;

  delegate->data_ = nullptr;
  delegate->flags = kTfLiteDelegateFlagsNone;
  delegate->Prepare = &DelegatePrepare;
  // �s��B
  delegate->CopyFromBufferHandle = &CopyFromBufferHandle;
  // ��B
  delegate->CopyToBufferHandle = &CopyToBufferHandle;
  // ��B
  delegate->FreeBufferHandle = &FreeBufferHandle;

  return delegate;
}

// �Y�������p�I�㗝

auto* my_delegate = CreateMyDelegate();
if (interpreter->ModifyGraphWithDelegate(my_delegate) !=
        kTfLiteOk) {
  // �p����r��I���@
} else {
  interpreter->Invoke();
}
...
// �ō@�疜�v�Z���㗝�B
delete my_delegate;
```
