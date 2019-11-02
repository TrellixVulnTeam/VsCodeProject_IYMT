# AOT�R���p�C���̗��p

## tfcompile�Ƃ́H

`tfcompile` �́ATensorFlow�̃O���t�����s�R�[�h�֎��O��(AOT)�R���p�C�����邽�߂̕W���c�[���ł��B
�S�̂̃o�C�i���T�C�Y�����炷���Ƃɉ����āA�������̎��s���I�[�o�w�b�h�𖳂������Ƃ��ł��܂��B
`tfcompile` �̓T�^�I�Ȏg�����́A���_�p�̌v�Z�O���t�����o�C���f�o�C�X�����̎��s�R�[�h�փR���p�C�����邱�Ƃł��B

TensorFlow�̃O���t�́A�ʏ�TensorFlow�̃����^�C���ɂ���Ď��s����܂��B
����́A�O���t�̊e�m�[�h�����s���邱�ƂɂȂ邽�߁A���s���I�[�o�w�b�h�������܂��B
TensorFlow�̃O���t�⃉���^�C���̃R�[�h���K�v�ɂȂ邽�߁A�S�̂̃o�C�i���T�C�Y���傫���Ȃ�܂��B
`tfcompile` ����Đ����������s�R�[�h�́ATensorFlow�̃����^�C�����g�킸�A���ۂɌv�Z�Ŏg�p����J�[�l���݂̂Ɉˑ����܂��B

�R���p�C���́AXLA�t���[�����[�N�̏�ɍ���Ă��܂��B
TensorFlow��XLA�t���[�����[�N���Ȃ��R�[�h�́A[tensorflow/compiler](https://www.tensorflow.org/code/tensorflow/compiler/) �ɑ��݂��܂��B


## tfcompile�͉������邩�H

`tfcompile` �́ATensorFlow�̊T�O�ł���feed��fetch�ɂ���Č`�����T�u�O���t���󂯎��A�T�u�O���t�𖞂����t�@���N�V�����𐶐����܂��B
`feeds` �̓t�@���N�V�����̓��͈����A`fetches` �̓t�@���N�V�����̏o�͈����ł��B
���荞�񂾌��ʂ̃T�u�O���t�́APlaceholder��Variable�m�[�h���܂߂邱�Ƃ��ł��Ȃ����߁A���ׂĂ̓��͂�feed�ɂ���Ďw�肳���K�v������܂��B
���ׂĂ�Placerholder��Variable�́Afeed�Ƃ��Ďw�肳���̂͋��ʂł���A�ŏI�I�ȃT�u�O���t�͂����̃m�[�h����؊܂݂܂���B
�������ꂽ�t�@���N�V�����́A�t�@���N�V�����̃V�O�l�`�����G�N�X�|�[�g����w�b�_�t�@�C���ƁA�������܂ރI�u�W�F�N�g�t�@�C������Ȃ� `cc_library` �Ƃ��ăp�b�P�[�W������܂��B
���[�U�[�́A�������ꂽ�t�@���N�V������K�؂ɌĂяo���R�[�h�������܂��B


## tfcompile�̗��p

���̃Z�N�V�����ł́A`tfcompile` ���g����TensorFlow�̃T�u�O���t������s�\�o�C�i���𐶐����邽�߂́A�����x���̃X�e�b�v���ڂ����q�ׂ܂��B
�X�e�b�v�́A�ȉ�����Ȃ�܂��B

* �X�e�b�v1: �R���p�C������T�u�O���t���\������
* �X�e�b�v2: �T�u�O���t���R���p�C�����邽�߂� `tf_library` �r���h�}�N���𗘗p����
* �X�e�b�v3: �T�u�O���t���Ăяo���R�[�h������
* �X�e�b�v4: �ŏI�I�ȃo�C�i�����쐬����


### �X�e�b�v1: �R���p�C������T�u�O���t���\������

�������ꂽ�t�@���N�V�����̓��͂���яo�͈����ɑ�������Afeed��fetch�����߂܂��B
�����āA[`tensorflow.tf2xla.Config`](https://www.tensorflow.org/code/tensorflow/compiler/tf2xla/tf2xla.proto) �� `feeds` ����� `fetches` ��ݒ肵�܂��B

```textproto
# �efeed�́A�������ꂽ�t�@���N�V�����ɂ�������͂̈ʒu�w������ł��B
# �G���g���̏����Ɠ��͈����̏����͈�v���܂��B
# ������ "x_hold" �� "y_hold" �́A�O���t��ɒ�`���ꂽPlaceholder�m�[�h�̖��O���w���܂��B
feed {
  id { node_name: "x_hold" }
  shape {
    dim { size: 2 }
    dim { size: 3 }
  }
}
feed {
  id { node_name: "y_hold" }
  shape {
    dim { size: 3 }
    dim { size: 2 }
  }
}

# �efetch�́A�������ꂽ�t�@���N�V�����ɂ�����o�͂̈ʒu�w������ł��B
# �G���g���̏����Əo�͈����̏����͈�v���܂��B
# ������ "x_y_prod" �́A�O���t��ɒ�`���ꂽMatmul�m�[�h�̖��O���w���܂��B
fetch {
  id { node_name: "x_y_prod" }
}
```


### �X�e�b�v2: �T�u�O���t���R���p�C�����邽�߂�tf_library�r���h�}�N���𗘗p����

���̃X�e�b�v�ł́A`tf_library` �r���h�}�N���𗘗p���āA�O���t�� `cc_library` �ɕϊ����܂��B
`cc_library` �́A�O���t���琶�����ꂽ�R�[�h���܂񂾃I�u�W�F�N�g�t�@�C���ƁA�������ꂽ�R�[�h�ɃA�N�Z�X���邽�߂̃w�b�_�t�@�C������\������܂��B
`tf_library` �́ATensorFlow�̃O���t�����s�R�[�h�ɃR���p�C�����邽�߂� `tfcompile` �𗘗p���Ă��܂��B

```build
load("//tensorflow/compiler/aot:tfcompile.bzl", "tf_library")

# �O���t�����s�R�[�h�ɃR���p�C�����邽�߂ɁAtf_library�}�N�����g�p���܂��B
tf_library(
    # name�́A�ȉ��̃r���h���[���𐶐����邽�߂Ɏg�p���܂��B
    # <name>           : cc_library�́A�������ꂽ�w�b�_�ƃI�u�W�F�N�g�t�@�C�����p�b�P�[�W�����܂��B
    # <name>_test      : cc_test�́A�ȒP�ȃe�X�g�ƃx���`�}�[�N���܂݂܂��B
    # <name>_benchmark : cc_binary�́A�ŏ����̈ˑ��֌W�����X�^���h�A�����ȃx���`�}�[�N���܂݁A
    #                    ���o�C���f�o�C�X�Ŏ��s�ł��܂��B
    name = "test_graph_tfmatmul",
    # cpp_class�ɂ́A���O��Ԃ��܂ސ������C++�̃N���X�����w�肵�܂��B
    # �N���X�́A�^����ꂽ���O��ԁA�������O��Ԃ��^�����Ă��Ȃ��ꍇ�̓O���[�o���Ȗ��O��Ԃɐ�������܂��B
    cpp_class = "foo::bar::MatMulComp",
    # graph�ɂ́A���͂ƂȂ�GraphDef���w�肵�܂����A�f�t�H���g�ł̓o�C�i���t�H�[�}�b�g�����҂��Ă��܂��B
    # �e�L�X�g�t�H�[�}�b�g���g�p����ꍇ�A�ڔ��� '.pbtex' ���g���Ă��������B
    # ���͂�feed�Əo�͂�fetch���܂񂾂��̓��̓O���t����A�T�u�O���t����������܂��B
    # Placeholder��Variable��Operation�́A���̃T�u�O���t�ɂ͑��݂��܂���B
    graph = "test_graph_tfmatmul.pb",
    # config�ɂ́A���͂ƂȂ�Config���w�肵�܂����A�f�t�H���g�ł̓o�C�i���t�H�[�}�b�g�����҂��Ă��܂��B
    # �e�L�X�g�t�H�[�}�b�g���g�p����ꍇ�A�ڔ��� '.pbtex' ���g���Ă��������B
    # ����͑O�̃X�e�b�v�ɂ����āAfeed��fetch���w�肵���Ƃ���ɂȂ�܂��B
    config = "test_graph_tfmatmul.config.pbtxt",
)
```

> ���̗�Ŏg�p����GraphDef (test_graph_tfmatmul.pb)�𐶐����邽�߂ɂ́A--out_dir�t���O���g���ďo�͏ꏊ���w�肵����Ԃ� [make_test_graphs.py](https://www.tensorflow.org/code/tensorflow/compiler/aot/tests/make_test_graphs.py) �����s���Ă��������B

�T�^�I�ȃO���t�Ƃ��āA�w�K���Ɋw�K�����d�݂�\������ [`Variables`](https://www.tensorflow.org/guide/variables) ���܂񂾂��̂�����܂����A`tfcompile` �� `Variables` ���܂񂾃T�u�O���t���R���p�C���ł��܂���B
�c�[�� [freeze_graph.py](https://www.tensorflow.org/code/tensorflow/python/tools/freeze_graph.py) �́A�`�F�b�N�|�C���g�t�@�C���ɕۑ����ꂽ�l���g���āAVariables��萔�ɕϊ����܂��B
`tf_library` �}�N���͕֋X��A���̃c�[�������s���� `freeze_checkpoint` �������T�|�[�g���܂��B
[tensorflow/compiler/aot/tests/BUILD](https://www.tensorflow.org/code/tensorflow/compiler/aot/tests/BUILD) �ɂ́A��葽���̗Ⴊ����܂��B

> �R���p�C�����ꂽ�T�u�O���t�Ɍ��ꂽ�萔�́A���ڐ��������R�[�h�փR���p�C������܂��B�������ꂽ�t�@���N�V�����ɒ萔��n�����߂ɂ́A�������R���p�C�����Ă��܂��̂ł͂Ȃ��A�P��feed�Ƃ��ēn���܂��B

`tf_library` �r���h�}�N���Ɋւ���ڍׂ́A[tfcompile.bzl](https://www.tensorflow.org/code/tensorflow/compiler/aot/tfcompile.bzl) ���Q�Ƃ��Ă��������B

��{�ƂȂ� `tfcompile` �c�[���̏ڍׂɂ��ẮA[tfcompile_main.cc](https://www.tensorflow.org/code/tensorflow/compiler/aot/tfcompile_main.cc) ���Q�Ƃ��Ă��������B


### �X�e�b�v3: �T�u�O���t���Ăяo���R�[�h������

���̃X�e�b�v�ł́A�������ꂽ�R�[�h���Ăяo�����߂ɁA�O�X�e�b�v�ɂ����� `tf_library` �r���h�}�N���ɂ���Đ������ꂽ�w�b�_�t�@�C��(`test_graph_tfmatmul.h`) ���g���܂��B
�w�b�_�t�@�C���́A�r���h�p�b�P�[�W�Ƃ��Ȃ��� `bazel-genfiles` �ɔz�u����A`tf_library` �r���h�}�N���ɐݒ肳�ꂽname�A�g���r���[�g�Ɋ�Â��Ė�������܂��B
���Ƃ��΁A`test_graph_tfmatmul` �̂��߂ɐ��������w�b�_�́A`test_graph_tfmatmul.h` �ɂȂ�ł��傤�B
�ȉ��́A�������ꂽ���̂Ɋւ���ȗ��łł��B
`bazel-genfiles` �ɐ������ꂽ�t�@�C���́A�𗧂t���I�ȃR�����g���܂݂܂��B

```c++
namespace foo {
namespace bar {

// MatMulComp�́A���O��TensorFlow�̃O���t�Ƃ��Ďw�肳�ꂽ�v�Z��\�����A
// ���s�R�[�h�փR���p�C������܂����B
class MatMulComp {
 public:
  // AllocMode�́A�o�b�t�@�̊��蓖�ă��[�h�𐧌䂵�܂��B
  enum class AllocMode {
    ARGS_RESULTS_AND_TEMPS,  // �����ƌ��ʁA�����Ĉꎞ�I�Ɏg�p����o�b�t�@�����蓖�Ă܂��B
    RESULTS_AND_TEMPS_ONLY,  // ���ʂƈꎞ�I�Ɏg�p����o�b�t�@�݂̂����蓖�Ă܂��B
  };

  MatMulComp(AllocMode mode = AllocMode::ARGS_RESULTS_AND_TEMPS);
  ~MatMulComp();

  // �����̃o�b�t�@������͂�ǂݍ���Ōv�Z�����s���A�o�͌��ʂ��o�b�t�@�ɏ������݂܂��B
  // �������ɂ�true��Ԃ��A���s���ɂ�false��Ԃ��܂��B
  bool Run();

  // ���̓o�b�t�@���Ǘ����郁�\�b�h�ł��B�o�b�t�@�́A�s�D��̃f�[�^�����ƂȂ�܂��B
  // ���ꂼ��̈ʒu�w������̂��߂̃��\�b�h�Q������܂��B
  void** args();

  void set_arg0_data(float* data);
  float* arg0_data();
  float& arg0(size_t dim0, size_t dim1);

  void set_arg1_data(float* data);
  float* arg1_data();
  float& arg1(size_t dim0, size_t dim1);

  // �o�̓o�b�t�@���Ǘ����郁�\�b�h�ł��B�o�b�t�@�́A�s�D��̃f�[�^�����ƂȂ�܂��B
  // Run�̌Ăяo���������������ƂɌĂԕK�v������܂��B
  // ���ꂼ��̈ʒu�w�茋�ʂ̂��߂̃��\�b�h�Q������܂��B
  void** results();


  float* result0_data();
  float& result0(size_t dim0, size_t dim1);
};

}  // end namespace bar
}  // end namespace foo
```

�������ꂽC++�N���X�́A`tf_library` �}�N���� `cpp_class` �Ɏw�肵���Ƃ���A���O��� `foo::bar` �ɂ����� `MatMulComp` �ɂȂ�܂��B
�������ꂽ���ׂẴN���X�́A�����ƌ��ʂ̂��߂̃o�b�t�@���������\�b�h���قȂ�݂̂ŁA���Ȃ�API�������܂��B
�����̃��\�b�h�́A`tf_library` �}�N���̈����ł��� `feed` �� `fetch` �Ɏw�肷��o�b�t�@�̐���^�ɂ���ĈႢ���������܂��B

�������ꂽ�N���X�ł́A3�̃o�b�t�@���Ǘ�����܂��B
`args` �͓��́A`results` �͏o�́A`temps` �͌v�Z�����s���邽�߂ɓ����ŗ��p����ꎞ�I�ȃo�b�t�@��\���Ă��܂��B
�f�t�H���g�ł́A�������ꂽ�N���X�̂��ꂼ��̃C���X�^���X�́A�����̂��ׂẴo�b�t�@���m�ۂ��ĊǗ����܂��B
�R���X�g���N�^�̈��� `AllocMode` �͂��̐U�镑����ς��邽�߂Ɏg�����Ƃ��ł��܂��B
���ׂẴo�b�t�@�́A64�o�C�g�̋��E�ɃA���C�����g����Ă��܂��B

�������ꂽC++�N���X�́AXLA�ɂ���Đ������ꂽ�჌�x���̃R�[�h��P�Ƀ��b�p����N���X�ł��B

`tfcompile_test.cc` �����Ƃɐ������ꂽ�t�@���N�V�������Ăяo����F

```c++
#define EIGEN_USE_THREADS
#define EIGEN_USE_CUSTOM_THREAD_POOL

#include <iostream>
#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "tensorflow/compiler/aot/tests/test_graph_tfmatmul.h" // ���������

int main(int argc, char** argv) {
  Eigen::ThreadPool tp(2);  // �K�v�ɉ������X���b�h�v�[���̃T�C�Y
  Eigen::ThreadPoolDevice device(&tp, tp.NumThreads());


  foo::bar::MatMulComp matmul;
  matmul.set_thread_pool(&device);

  // ������ݒ肵�A�v�Z�����s����
  const float args[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
  std::copy(args + 0, args + 6, matmul.arg0_data());
  std::copy(args + 6, args + 12, matmul.arg1_data());
  matmul.Run();

  // ���ʂ��m�F����
  if (matmul.result0(0, 0) == 58) {
    std::cout << "Success" << std::endl;
  } else {
    std::cout << "Failed. Expected value 58 at 0,0. Got:"
              << matmul.result0(0, 0) << std::endl;
  }

  return 0;
}
```


### �X�e�b�v4: �ŏI�I�ȃo�C�i�������

���̃X�e�b�v�ł́A�X�e�b�v2�ɂ����� `tf_library` �ɂ���Đ������ꂽ���C�u�����ƁA�X�e�b�v3�ŏ������R�[�h��g�ݍ��킹�čŏI�I�ȃo�C�i�������܂��B
�ȉ��́A`bazel` BUILD�t�@�C���̗�ł��B

```build
# ���Ȃ��̃o�C�i���������N�����
# //tensorflow/compiler/aot/tests/BUILD���Q��
load("//tensorflow/compiler/aot:tfcompile.bzl", "tf_library")

# �X�e�b�v2�ɂ�����tf_library�̌Ăяo���Ƃ��Ȃ�
tf_library(
    name = "test_graph_tfmatmul",
    ...
)

# tf_library�ɂ���Đ������ꂽ���s�R�[�h�́A���Ȃ��̃R�[�h�փ����N���邱�Ƃ��ł��܂�
cc_binary(
    name = "my_binary",
    srcs = [
        "my_code.cc",  # �������ꂽ�w�b�_�ɃA�N�Z�X���邽�߂ɁAtest_graph_tfmatmul.h���C���N���[�h���܂�
    ],
    deps = [
        ":test_graph_tfmatmul",  # �������ꂽ�I�u�W�F�N�g�t�@�C���փ����N���܂�
        "//third_party/eigen3",
    ],
    linkopts = [
          "-lpthread",
    ]
)
```
