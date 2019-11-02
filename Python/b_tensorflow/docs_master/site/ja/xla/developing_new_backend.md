# �V����XLA�̃o�b�N�G���h�J��

Note: �����̃h�L�������g�͎�����TensorFlow�R�~���j�e�B���|�󂵂����̂ł��B�R�~���j�e�B�ɂ��
�|���**�x�X�g�G�t�H�[�g**�ł��邽�߁A���̖|�󂪐��m�ł��邱�Ƃ�[�p��̌����h�L�������g](https://www.tensorflow.org/?hl=en)��
�ŐV�̏�Ԃ𔽉f�������̂ł��邱�Ƃ�ۏ؂��邱�Ƃ͂ł��܂���B
���̖|��̕i�������コ���邽�߂̂��ӌ����������̕��́AGitHub���|�W�g��[tensorflow/docs](https://github.com/tensorflow/docs)�Ƀv�����N�G�X�g�������肭�������B
\
�R�~���j�e�B�ɂ��|��⃌�r���[�ɎQ�����Ă�����������́A
[docs-ja@tensorflow.org ���[�����O���X�g](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)�ɂ��A�����������B

�{�\���K�C�h�́A�����I�ȕ��@��TensorFlow���n�[�h�E�F�A�ɗe�ՂɑΉ����������ƍl���Ă���A�A�[���[�A�_�v�^�[�̂��߂̂��̂ł��B
�{�K�C�h��1��1���J�ɐ����������̂ł͂Ȃ��ALLVM�ABazel�ATensorFlow�̒m����O��Ƃ��Ă��܂��B

XLA�́A�V�����A�[�L�e�N�`����A�N�Z�����[�^���ATensorFlow�̃O���t����������o�b�N�G���h���������邽�߂̒��ۓI�ȃC���^�[�t�F�[�X��񋟂��܂��B
XLA�ւ̑Ή��́A�V�����n�[�h�E�F�A�����Ɋ����̂��ׂĂ�TensorFlow�̃I�y���[�V��������������̂Ɣ�ׂāA�͂邩�ɊȌ��ŃX�P�[���u���ł��B


�����̂قƂ�ǂ́A�ȉ��̃V�i���I�̂�����1�ɕ��ނ���܂��B

1. LLVM�̃o�b�N�G���h�����݂��邩���Ȃ����ɂ�����炸�A������XLA�ŃT�|�[�g����Ă��Ȃ�������CPU�A�[�L�e�N�`��
2. LLVM�̃o�b�N�G���h�����݂���ACPU�ł͂Ȃ��n�[�h�E�F�A
3. LLVM�̃o�b�N�G���h�����݂��Ȃ��ACPU�ł͂Ȃ��n�[�h�E�F�A

Note: LLVM�̃o�b�N�G���h�Ƃ́A�����Ƀ����[�X���ꂽLLVM�̃o�b�N�G���h�A�܂��͊�Ɠ��ŊJ�����ꂽ�J�X�^�}�C�Y��LLVM�̃o�b�N�G���h�̂��Ƃ��w���܂��B


## �V�i���I1: ������XLA�ŃT�|�[�g����Ă��Ȃ�������CPU�A�[�L�e�N�`��

���̃V�i���I�̏ꍇ�A������ [XLA CPU�o�b�N�G���h](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/cpu) �����邱�Ƃ���n�߂Ă��������B
XLA��CPU�o�b�N�G���h�Ԃ̎�ȈႢ�́ALLVM�ɂ���Đ��������R�[�h�ł��邱�Ƃ���AXLA�ł�LLVM���g���ĈقȂ�CPU��TensorFlow�ɊȒP�ɑΉ��ł��܂��B
Google�́Ax64��ARM64�̃A�[�L�e�N�`���ɑ΂���XLA���������Ă��܂��B

�����n�[�h�E�F�A��Ƃ��n�[�h�E�F�A������LLVM�̃o�b�N�G���h�����ꍇ�A�r���h���ꂽLLVM�̃o�b�N�G���h��XLA�ɐڑ����邱�Ƃ͊ȒP�ł��B
JIT���[�h�ł́AXLA��CPU�o�b�N�G���h�̓z�X�g����CPU�̃R�[�h�𐶐����܂��B
Ahead-Of-Time�R���p�C���ł́A[`xla::AotCompilationOptions`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/compiler.h) ���ΏۂƂ���A�[�L�e�N�`���ɑ΂��Đݒ肷��LLVM Triple��񋟂��܂��B

����������LLVM�̃o�b�N�G���h���Ȃ��Ă��R�[�h�����킪�Ⴄ�`�ő��݂���Ȃ�΁A������CPU�o�b�N�G���h�̑啔�����ė��p�ł���\��������܂��B


## �V�i���I2: LLVM�̃o�b�N�G���h�����݂���ACPU�ł͂Ȃ��n�[�h�E�F�A

LLVM IR���o�͂�������� [`xla::CPUCompiler`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/cpu/cpu_compiler.cc) �� [`xla::GPUCompiler`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/gpu/nvptx_compiler.cc) �N���X���x�[�X�Ƃ��āA�V���� [`xla::Compiler`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/compiler.h) �̎�������邱�Ƃ��\�ł��B
�n�[�h�E�F�A�̐����ɂ��LLVM IR�̐������@�͈قȂ�܂����A�����̃R�[�h�͊����̃o�b�N�G���h�Ƌ��L�ł���ł��傤�B

�悢�Q�l��́AXLA�� [GPU�o�b�N�G���h](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/gpu) �ł��B
GPU�̃o�b�N�G���h��CPU�Ƃ͈قȂ�ISA���^�[�Q�b�g�Ƃ��邽�߁AGPU�h���C���ŗL�ȃR�[�h�̐������@�ɂȂ�܂��B
�ق��̎�ނ̃n�[�h�E�F�A�A���Ƃ��΁i�A�b�v�X�g���[����LLVM�̃o�b�N�G���h�����jHexagon�̂悤��DSP�́ALLVM IR�̐����̂����݂��ė��p���邱�Ƃ��ł��܂����A�ق��̕����͌ŗL�̂��̂ɂȂ�ł��傤


## �V�i���I3: LLVM�̃o�b�N�G���h�����݂��Ȃ��ACPU�ł͂Ȃ��n�[�h�E�F�A

LLVM�𗘗p�ł��Ȃ��ꍇ�A�Ώۂ̃n�[�h�E�F�A�����ɐV�����o�b�N�G���h���������邱�Ƃ��ŗǂ̑I�����ƂȂ�܂��B
���̑I�����́A����ȘJ�͂�K�v�Ƃ��܂��B
�������Ȃ���΂Ȃ�Ȃ��N���X�͎��Ɏ����Ƃ���ł��B

* [StreamExecutor](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/stream_executor/stream_executor.h): �����̃f�o�C�X�ł́A`StreamExecutor` �̂��ׂẴ��\�b�h���K�v�ɂȂ邱�Ƃ͂���܂���B�ڍׂ͊����� `StreamExecutor` �̎��������Ă��������B
* [xla::Compiler](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/compiler.h): �{�N���X�́AHLO Computation���� `xla::Executable` �ւ̃R���p�C���������B�����܂��B
* [xla::Executable](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/executable.h): �{�N���X�́A�R���p�C���ς݂�Computation���v���b�g�t�H�[����Ŏ��s���邽�߂Ɏg�p����܂��B
* [xla::TransferManager](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/transfer_manager.h): �{�N���X�́A�^����ꂽ�f�o�C�X�������̃n���h������XLA�̃��e�����f�[�^���\�z���邽�߂́A�v���b�g�t�H�[�����L�̂����݂�񋟂��邱�Ƃ��\�ɂ��܂��B����������΁A�z�X�g����f�o�C�X�܂��͂��̔��΂̃f�[�^�]���������B�����܂��B
