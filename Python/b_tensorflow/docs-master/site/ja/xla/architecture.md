# XLA �T�v

<div style="width:50%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:50%" src="https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/compiler/xla/g3doc/images/xlalogo.png">
</div>

Note: XLA�͌��݊J�����ł��邽�߁A����̏󋵂Ń������g�p�ʂ̑���␫�\�̈����������N�����ꍇ������܂��B

Note: �����̃h�L�������g�͎�����TensorFlow�R�~���j�e�B���|�󂵂����̂ł��B�R�~���j�e�B�ɂ��
�|���**�x�X�g�G�t�H�[�g**�ł��邽�߁A���̖|�󂪐��m�ł��邱�Ƃ�[�p��̌����h�L�������g](https://www.tensorflow.org/?hl=en)��
�ŐV�̏�Ԃ𔽉f�������̂ł��邱�Ƃ�ۏ؂��邱�Ƃ͂ł��܂���B
���̖|��̕i�������コ���邽�߂̂��ӌ����������̕��́AGitHub���|�W�g��[tensorflow/docs](https://github.com/tensorflow/docs)�Ƀv�����N�G�X�g�������肭�������B
\
�R�~���j�e�B�ɂ��|��⃌�r���[�ɎQ�����Ă�����������́A
[docs-ja@tensorflow.org ���[�����O���X�g](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)�ɂ��A�����������B

XLA(Accelerated Linear Algebra)�͐��`�㐔�̉��Z�ɓ��������R���p�C���ŁAXLA���g�����Ƃ�TensorFlow�̉��Z���œK�����A�������g�p�ʁA���\�A�T�[�o�⃂�o�C�����ł̈ڐA���̖ʂł̉��P�����҂ł��܂��B���݂̂Ƃ���A�قƂ�ǂ̃��[�U�ɂƂ���XLA���g�����Ƃɂ��傫�ȉ��b�͓����Ȃ���������܂��񂪁A[just-in-time (JIT) �R���p�C���@�\](https://www.tensorflow.org/xla/jit) �� [ahead-of-time (AOT) �R���p�C���@�\](https://www.tensorflow.org/xla/tfcompile) ��ʂ��āA�����I��XLA���g���Ă��������̂͊��}�ł��B�������A�V���ȃn�[�h�E�G�A�A�N�Z�����[�^�̊J���҂ɂ��ẮAXLA�������Ă݂邱�Ƃ��������߂��܂��B

XLA�͎����I�ȃt���[�����[�N�ł���A���݊����ɊJ������Ă��܂��B�����̃I�y���[�V�����̃Z�}���e�B�N�X���ς�邱�Ƃ͂قƂ�ǂȂ��Ǝv���܂����A�d�v�ȃ��[�X�P�[�X�ɑΉ����邽�߂ɐV���ȃI�y���[�V�������ǉ�����邱�Ƃ�����܂��BXLA�`�[���́AGitHub��ʂ����R�~���j�e�B�ւ̍v����A�s�����Ă���@�\�Ɋւ���t�B�[�h�o�b�N�����}���܂��B


## �Ȃ�XLA���J���������H

TensorFlow�ƘA�g����XLA���J�������ړI�͂���������܂��B

* **���s���x�̌���**: �T�u�O���t���R���p�C�����ATensorFlow�����^�C���̃I�[�o�w�b�h���팸���邱�ƂŁA�y�ʂȃI�y���[�V�����̎��s���Ԃ�Z�k���܂��B�܂��A�����I�y���[�V�������������邱�ƂŁA�������̃I�[�o�w�b�h���팸���܂��B����ɁA���m�̃e���\���̌`��ɓ������邱�ƂŁA���ϋɓI�ɒ萔��ݍ��݂��ł���悤�ɂ��܂��B
* **�������g�p�ʂ̉��P**: �������g�p�ʂ̉�͂ƃX�P�W���[�����O�ɂ���āA�I�y���[�V�����̒��ԃf�[�^��ێ�����̈���팸���܂��B
* **�Ǝ��I�y���[�V�����ւ̈ˑ��x�팸**: �����I�Ɍ������ꂽ�჌�x���ȃI�y���[�V�����̐��\�����コ���A�l��ɂ��Ǝ��I�y���[�V�����Ɠ����̐��\�𓾂���悤�ɂ��邱�ƂŁA�Ǝ��I�y���[�V�������쐬����K�v���������Ȃ�܂��B
* **���o�C�����ł̃f�B�X�N��L�X�y�[�X�팸**: �T�u�O���t��AOT�R���p�C�����A���̃A�v���P�[�V�����ɒ��ڃ����N�\�ȃI�u�W�F�N�g�ƃw�b�_���o�͂��邱�ƂŁATensorFlow�̃����^�C�����폜���܂��B����ɂ���āA���o�C���ł̐��_���̃f�B�X�N��L�X�y�[�X�����Ⴂ�ɍ팸�ł��܂��B
* **�ڐA���̌���**: TensorFlow�̃v���O�����̑啔�����C�����邱�ƂȂ��A�V�����n�[�h�E�F�A�����̃o�b�N�G���h���������Ƃ��e�ՂɂȂ�܂��B����́ATensorFlow�̃v���O���������������ĐV�����n�[�h�E�F�A�����̃I�y���[�V�������������Ƃ͑S���قȂ���̂ł��B


## XLA�͂ǂ̂悤�ɓ����̂��H

XLA�̓��͂ƂȂ錾��́A"HLO IR"�܂��͒P��HLO(High Level Optimizer)�ƌĂ΂�܂��BHLO�̃Z�}���e�B�N�X�́A[Operation Semantics](https://www.tensorflow.org/xla/operation_semantics) �ɋL�ڂ���Ă��܂��BHLO�́A�R���p�C���ň��� [���ԕ\��](https://ja.wikipedia.org/wiki/%E4%B8%AD%E9%96%93%E8%A1%A8%E7%8F%BE) �ƍl����Ƃ킩��₷����������܂���B

XLA��HLO�Œ�`���ꂽ�O���t("Computations")���A�l�X�ȃn�[�h�E�F�A�A�[�L�e�N�`���̎��s�R�[�h�ɃR���p�C�����܂��B[Developing a new backend for XLA](https://www.tensorflow.org/xla/developing_new_backend) �ɋL�ڂ���Ă���悤�ɁAXLA��V���ȃn�[�h�E�F�A�œ��삳���邱�Ƃ��e�Ղł���Ƃ����_�ŁAXLA�̓��W���[��������Ă���ƌ����܂��B[CPU (x86-64�AARM64) �����̏���](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/cpu) �� [NVIDIA GPU�����̏���](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/gpu) �́ATensorFlow�̃��C���̃\�[�X�R�[�h�c���[����Q�Ƃ��邱�Ƃ��ł��܂��B

���Ɏ����}�́AXLA�̓����ōs���Ă���R���p�C�������������Ă��܂��B

![](https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/compiler/xla/g3doc/images/how-does-xla-work.png)

XLA�́A[CSE](https://ja.wikipedia.org/wiki/%E5%85%B1%E9%80%9A%E9%83%A8%E5%88%86%E5%BC%8F%E9%99%A4%E5%8E%BB) ��I�y���[�V���������A�v�Z���̃��������蓖�ĉ�͂Ƃ������A�^�[�Q�b�g�Ɉˑ����Ȃ��œK�����͂��s���܂��B

�^�[�Q�b�g�Ɉˑ����Ȃ��œK�������̌�AXLA��HLO computation���o�b�N�G���h�ɓ]�����܂��B�o�b�N�G���h�ł́A�^�[�Q�b�g�ŗL�̏����l������HLO���x���ł̍œK�����s���܂��B�Ⴆ�΁A�o�b�N�G���h��XLA GPU�ł���ꍇ�A���GPU�̃v���O���~���O���f���ɓK�����I�y���[�V�����̌����ɉ����Acomputation�𕡐��̃X�g���[���֕������Ċ��蓖�Ă���@�����肵�܂��B����Ƀo�b�N�G���h�́A�I�y���[�V�����̏W���p�^�[�����A�œK�����ꂽ���C�u�����Ăяo���ƈ�v���邩�m�F���܂��B

���ɁA�^�[�Q�b�g�ŗL�̃R�[�h�𐶐����܂��BXLA�ɕt������CPU��GPU�̃o�b�N�G���h�́Alow-level IR�Ƃ��� [LLVM](http://llvm.org/) ���̗p���A�œK����R�[�h������LLVM���g���čs���܂��B�����̃o�b�N�G���h�́AXLA��HLO computation��\�����邽�߂Ɍ����I��LLVM IR���o�͂��ALLVM���g����LLVM IR����l�C�e�B�u�R�[�h�𐶐����܂��B

���݁AGPU�̃o�b�N�G���h��LLVM NVPTX�̃o�b�N�G���h�o�R��NVIDIA GPU���T�|�[�g���ACPU�̃o�b�N�G���h�͕�����CPU��ISA���T�|�[�g���Ă��܂��B


## �T�|�[�g����v���b�g�t�H�[��

XLA�́Ax86-64��NVIDIA GPU������ [JIT�R���p�C���@�\](https://www.tensorflow.org/xla/jit) ���Ax86-64��ARM������ [AOT�R���p�C���@�\](https://www.tensorflow.org/xla/tfcompile) ���T�|�[�g���Ă��܂��B
