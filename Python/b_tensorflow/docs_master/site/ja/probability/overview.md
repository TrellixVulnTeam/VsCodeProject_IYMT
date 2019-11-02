# TensorFlow Probability


Note: �����̃h�L�������g�͎�����TensorFlow�R�~���j�e�B���|�󂵂����̂ł��B�R�~���j�e�B�ɂ��
�|���**�x�X�g�G�t�H�[�g**�ł��邽�߁A���̖|�󂪐��m�ł��邱�Ƃ�[�p��̌����h�L�������g](https://www.tensorflow.org/?hl=en)��
�ŐV�̏�Ԃ𔽉f�������̂ł��邱�Ƃ�ۏ؂��邱�Ƃ͂ł��܂���B
���̖|��̕i�������コ���邽�߂̂��ӌ����������̕��́AGitHub���|�W�g��[tensorflow/docs](https://github.com/tensorflow/docs)�Ƀv�����N�G�X�g�������肭�������B
\
�R�~���j�e�B�ɂ��|��⃌�r���[�ɎQ�����Ă�����������́A
[docs-ja@tensorflow.org ���[�����O���X�g](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)�ɂ��A�����������B  

TensorFlow Probability �� TensorFlow �ɂ�����m���I���_�Ɠ��v�I���͂̂��߂̃��C�u�����ł��B
TensorFlow �G�R�V�X�e���̈ꕔ�Ƃ��āATensorFlow Probability �͊m���I��@�Ƃ��܂��܂Ȏ�@��@�\�Ƃ̓�����񋟂��܂��B
���Ƃ��΁A�[�w�l�b�g���[�N��p�����m���I�Ȏ�@�A����������p�������z�Ɋ�Â����_�AGPU �̂悤�ȃn�[�h�E�F�A�������╪�U�����ɂ��傫�ȃf�[�^�Z�b�g�⃂�f���ɑ΂���X�P�[���r���e�B�Ȃǂł��B

TensorFlow Probability ���n�߂邽�߂ɂ́A[�C���X�g�[���K�C�h](./install) ��
[Python notebook �`���[�g���A��](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/)���Q�Ƃ��Ă��������B

## �R���|�[�l���g

��X�̊m���I�@�B�w�K�c�[���Q�͈ȉ��̂悤�ȍ\���ɂȂ��Ă��܂�:

### Layer 0: TensorFlow

*���l����*���ɁA`LinearOperator`
�N���X���\�ɂ���A�����I�ȉ��Z�̂��߂̓���̍\�� (�Ίp�A�჉���N) ���J���ł���悤�ɂ���s��t���[�Ȏ����B 
TensorFlow Probability �`�[���ɂ�胁���e�i���X����Ă��āATensorFlow �R�A�� [`tf.linalg`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/linalg) �̈ꕔ�ł��B

### Layer 1: �m���I�ȃu���b�N�̍\�z

* *Distributions* ([`tfp.distributions`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/distributions),
  [`tf.distributions`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/ops/distributions)):
  �o�b�`��[�u���[�h�L���X�e�B���O](https://docs.scipy.org/doc/numpy-1.14.0/user/basics.broadcasting.html)�̎d�g�݂������ꂽ�A�����̊m�����z�₻��Ɋ֘A���铝�v�ʂ̏���
* *Bijectors* ([`tfp.bijectors`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/bijectors)):
  �����_���ϐ��̉t�őg�ݗ��ĉ\�ȕϊ��B Bijectors �͕ϊ����ꂽ���z�̖L�x�ȃN���X��񋟂��܂��B����́A�ÓT�I��
  [�ΐ����K���z](https://en.wikipedia.org/wiki/Log-normal_distribution)����
  [masked autoregressive flows](https://arxiv.org/abs/1705.07057) �̂悤�Ȑ������ꂽ�[�w�w�K���f���ɂ܂ŋy�т܂��B

### Layer 2: ���f���\�z

*   *Edward2*
    ([`tfp.edward2`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/edward2)):
    �v���O�����Ƃ��ď_��Ȋm���I���f�����`���邽�߂̊m���I�v���O���~���O����
*   *Probabilistic layers*
    ([`tfp.layers`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/layers)):
    TensorFlow �� layers ���g�����āA����炪�\������֐��̕s�m�������o�͂ł���j���[�����l�b�g���[�N�w
*   *Trainable distributions*
    ([`tfp.trainable_distributions`](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/trainable_distributions)):
    �m�����z���o�͂���j���[�����l�b�g���[�N���\�z���邱�Ƃ��ȒP�ɂ���A1�� Tensor �ɂ��p�����[�^�����m�����z

### Layer 3: �m���I���_

*   *Markov chain Monte Carlo*
    ([`tfp.mcmc`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/mcmc)):
    �T���v�����O�ɂ��ϕ��ߎ��̂��߂̃A���S���Y��
    [�n�~���g�������e�J�����@](https://en.wikipedia.org/wiki/Hamiltonian_Monte_Carlo)�A
    �����_���E�H�[�N���g���|���X�E�w�C�X�e�B���O�@�A�J�X�^���J�ڃJ�[�l�����\�z���邱�Ƃ��ł���@�\���܂݂܂��B
*   *Variational Inference*
    ([`tfp.vi`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/vi)):
    �œK���ɂ��ϕ��ߎ��̂��߂̃A���S���Y��
*   *Optimizers*
    ([`tfp.optimizer`](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/optimizer)):
    TensorFlow Optimizers ���g�������A�m���I�œK�����W���[���B
    [Stochastic Gradient Langevin Dynamics](http://www.icml-2011.org/papers/398_icmlpaper.pdf) ���܂݂܂��B
*   *Monte Carlo*
    ([`tfp.monte_carlo`](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/python/monte_carlo)):
    �����e�J�����@��p�����c�[���Q

TensorFlow Probability �͊J�����ł��邽�߁A�C���^�t�F�[�X�͕ύX�����\��������܂��B

## �g�p��

�i�r�Q�[�V�����ɍڂ��Ă��� [Python notebook �`���[�g���A��](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/)
�ɉ����āA�������̃X�N���v�g�Ⴊ���p�ł��܂�:

* [Variational Autoencoders](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/vae.py)
  latent code �ƕϕ����_�ɂ��\���w�K
* [Vector-Quantized Autoencoder](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/vq_vae.py)
  �x�N�g���ʎq���ɂ�闣�U�\���w�K
* [�x�C�W�A���j���[�����l�b�g���[�N](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/bayesian_neural_network.py)
  �d�݂̕s�m�������o�͂���j���[�����l�b�g���[�N
* [�x�C�Y���W�X�e�B�b�N��A](https://github.com/tensorflow/probability/tree/master/tensorflow_probability/examples/logistic_regression.py)
  ��l���ނ̂��߂̃x�C�Y���_

## issue �̕�

�o�O�񍐂�@�\�v�]��
[TensorFlow Probability issue tracker](https://github.com/tensorflow/probability/issues) ���g�p���Ă��������B
