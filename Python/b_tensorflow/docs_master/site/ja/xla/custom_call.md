# XLA�̃J�X�^���R�[��

���̃h�L�������g�ł́AXLA�u�J�X�^���R�[���v�̏������Ǝg�����ɂ��Đ������܂��B
�J�X�^���R�[���́AC++��CUDA�Ȃǂ̃v���O���~���O����ŏ����ꂽ�R�[�h���AXLA�v���O��������Ăяo�����Ƃ��ł��܂��B

�x���F �J�X�^���R�[���́A�p���[���[�U�p�̒჌�x���@�\�ł��B
�J�X�^���R�[�����g���ƁA�f�o�b�O���ɂ����i�����ċC�Â��ɂ����j��Ԃ̒��ŁA���Ȃ��̃v���O���������₷���Ȃ�܂��B
�������������Ȃ����Ƃ��A���Ȃ����g��XLA���f�o�b�O�ł��鏀�����ł��Ă��Ȃ��Ȃ�A�J�X�^���R�[�����g���ׂ��ł͂���܂���B
�g���u���ɑ��������Ƃ��Ă��AXLA�J���҂���x���͂��܂���炦�Ȃ��Ǝv���Ă���ׂ��ł��B

�x���F �J�X�^���R�[����API/ABI�́A�����_�ł͌ł܂��Ă��܂���B
���܂���ɕύX�������͂���܂��񂪁A�ύX����\���͂���܂��B
�����\�������邢�����̕ύX�ɂ��Ă͈ȉ��Ő������܂��B

## CPU�ł̃J�X�^���R�[��

XLA�N���C�A���gAPI�o�R�ŁA�J�X�^���R�[����\��HLO���߂���邱�Ƃ��ł��܂��B
����́A���M���_�ł�TensorFlow�o�R�ł͌��J����Ă��܂���B

�Ⴆ�΁A�ȉ��̃R�[�h��CPU��� `A[i] = B[i % 128] + C[i]` ���J�X�^���R�[�����g�p���Čv�Z���܂��i�������A�ʏ��HLO���g���Čv�Z�ł��܂����A���ׂ��ł��I�j�B

```c++
#include "tensorflow/compiler/xla/client/xla_builder.h"
#include "tensorflow/compiler/xla/service/custom_call_target_registry.h"

void do_it() {
  xla::XlaBuilder b("do_it");
  xla::XlaOp param0 =
      xla::Parameter(0, xla::ShapeUtil::CreateShape(F32, {128}), "p0");
  xla::XlaOp param1 =
      xla::Parameter(1, xla::ShapeUtil::CreateShape(F32, {2048}), "p1");
  xla::XlaOp custom_call =
      xla::CustomCall(&b, "do_custom_call", /*operands=*/{param0, param1},
                      /*output_shape=*/ShapeUtil::CreateShape(F32, {2048}));
}

void do_custom_call(void* out, const void** in) {
  float* out_buf = reinterpret_cast<float*>(out);
  const float* in0 = reinterpret_cast<const float*>(in[0]);
  const float* in1 = reinterpret_cast<const float*>(in[1]);
  for (int i = 0; i < 2048; ++i) {
    out_buf[i] = in0[i % 128] + in1[i];
  }
}
XLA_REGISTER_CUSTOM_CALL_TARGET(do_custom_call, "Host");
```

�֐� `do_custom_call` �́A���������s����o�b�t�@�̎�������m���Ă���K�v������܂��B
���̗�ł́A�T�C�Y128��2048�𒼏������Ă��܂��B
�����A������������Ȃ��ꍇ�ɂ́A�p�����[�^�Ƃ��Ď��������֐��ɓn�����Ƃ��ł��܂��B

## GPU�ł̃J�X�^���R�[��

GPU�̃J�X�^���R�[���̃t���[�����[�N�́ACPU�̃t���[�����[�N�Ƒ����قȂ�܂��B
�����ł́A��L��CPU�R�[�h�Ɠ��� `A[i] = B[i % 128] + C[i]` �̌v�Z���s��CUDA�̗�������܂��B

```c++
void do_it() { /* ��Ɠ������� */ }

__global__ custom_call_kernel(const float* in0, const float* in1, float* out) {
  size_t idx = threadIdx.x * blockSize.x + gridIdx.x;
  out[idx] = in0[idx % 128] + in1[idx];
}

void do_custom_call(CUstream stream, void** buffers,
                    const char* opaque, size_t opaque_len) {
  const float* in0 = reinterpret_cast<const float*>(buffers[0]);
  const float* in1 = reinterpret_cast<const float*>(buffers[1]);
  float* out = reinterpret_cast<float*>(buffers[2]);

  const int64 block_dim = 64;
  const int64 grid_dim = 2048 / block_dim;
  custom_call_kernel<<<grid_dim, block_dim,
                       /*dynamic_shared_mem_bytes=*/0, stream>>>(in0, in1, out);
}
XLA_REGISTER_CUSTOM_CALL_TARGET(do_custom_call, "CUDA");
```

�ŏ���GPU�J�X�^���R�[���֐����A*CPU��Ŏ��s�����֐��ł���*���Ƃɒ��ӂ��Ă��������B
CPU�p `do_custom_call` �֐��́AGPU��ł̍�Ƃ��L���[�ɓ����������ʂ����܂��B
�����ł�CUDA�J�[�l�����N�����Ă��܂����Acublas���Ăяo���悤�ȑ��̂��Ƃ��ł��܂��B

`buffers` �̓z�X�g��ɂ���|�C���^�̔z��ŁA�e�v�f�̓f�o�C�X�i�܂�GPU�j���������w���Ă��܂��B
�p�����[�^���ŏ��ɗ��āA���̂��Əo�͂̒l�����܂��B
����́ACPU�̌Ăяo���K���Ƃ͑傫���قȂ�A�Q�̃p�����[�^�A`ins` �� `out` ������܂��B
�Ⴄ������������ȗ��R�́A�^�v���^�̓��o�͂������I�ɏ������邽�߂ł��B
�ȉ��̏͂�����񂭂������B

CPU�̗�̂悤�ɁA���o�̓o�b�t�@�̑傫�����J�X�^���R�[���ɒ��������܂����B
�������ACPU�̏ꍇ�Ƃ͈قȂ�A�I�y�����h�Ƃ��ăo�b�t�@�̑傫����n���Ă����܂������܂���B
�ʏ�ACPU��Ńo�b�t�@�̑傫�����������Ă���K�v������܂��B�Ⴆ�΁A�J�[�l�����N������Ƃ��Ablock/grid�̎�����񂪕K�v�ł��B
�������A�J�X�^���R�[���ɃI�y�����h�Ƃ��ăo�b�t�@�T�C�Y���n�����ƁA���̒l��GPU��������ɂ���܂��B
�����̊J�n���ɁA���̒l��ǂނ��߂̂����ɏ������d�������I�ȃf�o�C�X����z�X�g�ւ̃������R�s�[�����s����K�v������܂��B

�����������邽�߂� `opaque` �p�����[�^��p�ӂ��Ă��܂��B
�J�X�^���R�[��������Ƃ��ɁA�C�ӂ̃o�C�g��������Z�b�g�ł��܂��B

```c++
std::string opaque = "...";
xla::CustomCall(&b, "do_custom_call", /*operands=*/{param0, param1},
                /*output_shape=*/ShapeUtil::CreateShape(F32, {2048}),
                opaque);
```

`xla::Shape` �̓v���g�R���o�b�t�@�\�������̂ŁA `opaque` �̓����ɂ��̃V���A���C�Y���ꂽ�\����ۑ�����GPU�J�X�^���R�[���̓����Ńf�V���A���C�Y�ł��܂��B
�������A `xla::ShapeProto` �͕p�ɂɂ͕ύX����܂��񂪁A `xla::Shape` ��*�ύX����܂�*�B
git���O���`�F�b�N���āA�ߋ��ɂǂ̂悤�ȕύX���s��ꂽ���m�F���Ă��������B

## �J�X�^���R�[���Ƀ^�v����n��

�ȉ��̃J�X�^���R�[���Ăяo�����l���܂��B

```c++
using xla::ShapeUtil;
Shape p0_shape = ShapeUtil::MakeTuple({
    ShapeUtil::MakeShape(F32, {32}),
    ShapeUtil::MakeTuple({
        ShapeUtil::MakeShape(F32, {64}),
        ShapeUtil::MakeShape(F32, {128}),
    }),
    ShapeUtil::MakeShape(F32, {256}),
});
xla::XlaOp p0 = xla::Parameter(0, p0_shape, "p0");

Shape out_shape = ShapeUtil::MakeTuple({
  ShapeUtil::MakeShape(F32, {512}),
  ShapeUtil::MakeShape(F32, {1024}),
});
xla::CustomCall(&b, "do_custom_call", /*operands=*/{p0}, out_shape);
```

CPU��GPU�̗����ŁA�^�v���̓|�C���^�̔z��Ƃ��ă��������ŕ\������܂��B
C++�[���R�[�h�ł́A��L�̃p�����[�^0�͈ȉ��̂悤�ɔz�u����܂��B

```c++
// ��L�̃J�X�^���R�[���̃p�����[�^0�̃����������C�A�E�g
// CPU��GPU�̗����ŗL���ł��B
float* subbuf0 = new float[32];
float* subbuf1 = new float[64];
float* subbuf2 = new float[128]
float* subbuf3 = new float[256];

void* subtuple = new void*[2];
(*subtuple)[0] = subbuf1;
(*subtuple)[1] = subbuf2;

void* p0 = new void*[3];
(*p0)[0] = subbuf0;
(*p0)[1] = subtuple;
(*p0)[2] = subbuf3;
```

CPU��GPU�Ń��������\���͓����ł����ACPU��GPU�̃J�X�^���R�[���Ăяo���K��ł͏������@���قȂ�܂��B

### �ꎞ�o�b�t�@�Ƃ��Ẵ^�v���o��

�J�X�^���R�[���ւ̃^�v�����͕͂֗��ł����A�����ɂ͕K�{�ł͂���܂���B
�J�X�^���R�[���ւ̃^�v�����͂��T�|�[�g����Ă��Ȃ��Ȃ�A�J�X�^���R�[���Ƀ^�v����n���O��get-tuple-element���g���ă^�v���𕪉��ł��܂��B

����A�^�v��*�o��*�́A���̕��@�ł͂ł��Ȃ����Ƃ��ł��܂��B

�^�v���o�͂������m�ȗ��R�́A���ꂪ�J�X�^���R�[���i�܂��́A����XLA���߁j�������̓Ɨ��Ȕz���Ԃ����@������ł��B

�������A���܂薾�m�ł͂Ȃ��ł����A�^�v���o�͂̓J�X�^���R�[���Ɉꎞ��������񋟂�����@�ł�����܂��B
�����A*�o��*�͈ꎞ�o�b�t�@��\���ł��܂��B
�o�̓o�b�t�@�̓I�y���[�V�������������߂�Ƃ��������������Ă��āA�������܂ꂽ���Ƃɓǂݏo�����Ƃ��ł��܂��B
���ꂱ�����A�܂��Ɉꎞ�o�b�t�@�ɕK�v�Ȃ��̂ł��B

��̗�ŁA `F32[1024]` ���ꎞ�o�b�t�@�Ƃ��Ďg�������Ƃ��܂��B
��L�̂悤��HLO���L�q���āA�P�ɃJ�X�^���R�[���̃^�v���C���f�b�N�X1�������ēǂ܂Ȃ��悤�ɂ��܂��B

### CPU�J�X�^���R�[���ł̃^�v��

CPU�R�[�h�ɂ́A `do_custom_call(const void** ins, void* out)` �֐�������܂��B
`ins` �� `param0` ���w���v�f���P�����̔z��ł��B
`param0` �̃T�u�o�b�t�@�́A���̃|�C���^���f���t�@�����X���ăA�N�Z�X�ł��܂��B
`output_tuple` �̃T�u�o�b�t�@�́A`out` ���f���t�@�����X���ăA�N�Z�X�ł��܂��B

### GPU�J�X�^���R�[���ł̃^�v��

GPU�R�[�h�ɂ́A `do_custom_call(..., void** buffers, ...)` �֐�������܂��B
���̏ꍇ `buffers` �́A���o�͂̊e���[�̃o�b�t�@����v�f�ɑΉ�����A*�U��*�̃f�o�C�X�|�C���^�����z�X�g�̔z��ł��B
�t���b�g���X�g�𐶐����邽�߂ɁA�p�����[�^�Əo�͂ɑ΂��Ĕ��������������Ȃ��A���ꂼ��ɂ��Ă��̌`����s���������ɑ������܂��B
��̓I�ɂ�:

```c++
// ��L�̃J�X�^���R�[���̂��߂́AGPU�J�X�^���R�[���֐��ւ� 
// `buffers` �p�����[�^�̃��C�A�E�g�B
buffers[0] == subbuf0
buffers[1] == subbuf1
buffers[2] == subbuf2
buffers[3] == subbuf3
buffers[4] == output_subbuf0
buffers[5] == output_subbuf1
```
