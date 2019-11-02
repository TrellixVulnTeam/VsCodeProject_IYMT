# �}���f���u���W��

Note: �����̃h�L�������g�͎�����TensorFlow�R�~���j�e�B���|�󂵂����̂ł��B�R�~���j�e�B�ɂ��
�|���**�x�X�g�G�t�H�[�g**�ł��邽�߁A���̖|�󂪐��m�ł��邱�Ƃ�[�p��̌����h�L�������g](https://www.tensorflow.org/?hl=en)��
�ŐV�̏�Ԃ𔽉f�������̂ł��邱�Ƃ�ۏ؂��邱�Ƃ͂ł��܂���B
���̖|��̕i�������コ���邽�߂̂��ӌ����������̕��́AGitHub���|�W�g��[tensorflow/docs](https://github.com/tensorflow/docs)�Ƀv�����N�G�X�g�������肭�������B
\
�R�~���j�e�B�ɂ��|��⃌�r���[�ɎQ�����Ă�����������́A
[docs-ja@tensorflow.org ���[�����O���X�g](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)�ɂ��A�����������B

[�}���f���u���W��](https://en.wikipedia.org/wiki/Mandelbrot_set)�̉�����
�@�B�w�K�Ƃ͉��̊֌W������܂��񂪁A
��ʓI�Ȑ��w�ɑ΂���TensorFlow���g���ʔ�����Ƃ��Ė𗧂��܂��B
���ۂɂ͉����̔��ɒP���Ȏ����ł����A���̗�͗v�_�������Ă��܂��B
�i�ŏI�I�ɂ͂��������摜�𐶐����邽�߂ɂ����ƕ��G�Ȏ�����
�񋟂��邱�ƂɂȂ邩������܂���B�j

## ��{�I�Ȑݒ�

�n�߂ɂ������C���|�[�g���K�v�ł��B

```python
# �V�~�����[�V�����̂��߂Ƀ��C�u�������C���|�[�g
import tensorflow as tf
import numpy as np

# �����̂��߂ɃC���|�[�g
import PIL.Image
from io import BytesIO
from IPython.display import Image, display
```

���x�́A�����񐔂��󂯎���Ď��ۂɉ摜��\������֐����`���܂��B

```python
def DisplayFractal(a, fmt='jpeg'):
  """�F�ʖL���ȃt���N�^���̉摜�Ƃ���
     �����񐔂̔z���\�����܂�"""
  a_cyclic = (6.28*a/20.0).reshape(list(a.shape)+[1])
  img = np.concatenate([10+20*np.cos(a_cyclic),
                        30+50*np.sin(a_cyclic),
                        155-80*np.cos(a_cyclic)], 2)
  img[a==a.max()] = 0
  a = img
  a = np.uint8(np.clip(a, 0, 255))
  f = BytesIO()
  PIL.Image.fromarray(a).save(f, fmt)
  display(Image(data=f.getvalue()))
```

## �Z�b�V�����ƕϐ��̏�����

���ۂɎ������߂ɁA�������͂悭�Θb�^�Z�b�V�������g���܂����A
�ʏ�̃Z�b�V�����ł����l�ɂ��܂������܂��B

```python
sess = tf.InteractiveSession()
```

NumPy��TensorFlow�����R�ɑg�ݍ��킹�邱�Ƃ��ł��ĕ֗��ł��B

```python
# Use NumPy to create a 2D array of complex numbers

Y, X = np.mgrid[-1.3:1.3:0.005, -2:1:0.005]
Z = X+1j*Y
```

����ł́ATensorFlow�̃e���\���̒�`�Ə����������܂��B

```python
xs = tf.constant(Z.astype(np.complex64))
zs = tf.Variable(xs)
ns = tf.Variable(tf.zeros_like(xs, tf.float32))
```

TensorFlow�ł̓e���\���̎g�p���邽�߂ɖ����I�ɏ���������K�v������܂��B

```python
tf.global_variables_initializer().run()
```

## �v�Z�̒�`�Ǝ��s

����ł́A�ǉ��̌v�Z���L�q���܂�...

```python
# �V����z�̒l���v�Z���܂� z: z^2 + x
zs_ = zs*zs + xs

# �V�����l�͔��U���Ă��邩�H
not_diverged = tf.abs(zs_) < 4

# zs�Ɣ����񐔂��X�V���鉉�Z
#
# ����: �V����zs�̒l�����U���Ă��Ă�zs���X�V�������Ă���I����͑�ϖ��ʂł���I
#       �����P���ł͂Ȃ��Ȃ邪�A��������s������ǂ����@�͂���
#
step = tf.group(
  zs.assign(zs_),
  ns.assign_add(tf.cast(not_diverged, tf.float32))
  )
```

... ������200�X�e�b�v���s���܂��B

```python
for i in range(200): step.run()
```

���ʂ����Ă݂܂��傤�B

```python
DisplayFractal(ns.eval())
```

![jpeg](https://www.tensorflow.org/images/mandelbrot_output.jpg)

�Ȃ��Ȃ������Ȃ��ł��ˁI

