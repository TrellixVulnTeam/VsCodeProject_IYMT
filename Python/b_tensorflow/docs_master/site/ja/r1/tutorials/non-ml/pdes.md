# �Δ���������

Note: �����̃h�L�������g�͎�����TensorFlow�R�~���j�e�B���|�󂵂����̂ł��B�R�~���j�e�B�ɂ��
�|���**�x�X�g�G�t�H�[�g**�ł��邽�߁A���̖|�󂪐��m�ł��邱�Ƃ�[�p��̌����h�L�������g](https://www.tensorflow.org/?hl=en)��
�ŐV�̏�Ԃ𔽉f�������̂ł��邱�Ƃ�ۏ؂��邱�Ƃ͂ł��܂���B
���̖|��̕i�������コ���邽�߂̂��ӌ����������̕��́AGitHub���|�W�g��[tensorflow/docs](https://github.com/tensorflow/docs)�Ƀv�����N�G�X�g�������肭�������B
\
�R�~���j�e�B�ɂ��|��⃌�r���[�ɎQ�����Ă�����������́A
[docs-ja@tensorflow.org ���[�����O���X�g](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)�ɂ��A�����������B

TensorFlow�͋@�B�w�K�����̂��̂ł͂���܂���B�����ł�[�Δ���������](
https://en.wikipedia.org/wiki/Partial_differential_equation)�̐U�镑����
�V�~�����[�g���邽�߂�TensorFlow���g����(��₠�肫�����)��������܂��B
�������̉J�����������ꍇ�ɂ����鐳���`�̒r�̕\�ʂ��V�~�����[�g���܂��B

## ��{�I�Ȑݒ�

�������̃C���|�[�g���K�v�ɂȂ�܂��B

```python
# �V�~�����[�V�����̂��߂Ƀ��C�u�������C���|�[�g
import tensorflow as tf
import numpy as np

# �����̂��߂ɃC���|�[�g
import PIL.Image
from io import BytesIO
from IPython.display import clear_output, Image, display
```

�ȉ��͉摜�Ƃ��Ēr�̕\�ʂ̏�Ԃ�\������֐��ł��B

```python
def DisplayArray(a, fmt='jpeg', rng=[0,1]):
  """�摜�Ƃ��Ĕz���\������"""
  a = (a - rng[0])/float(rng[1] - rng[0])*255
  a = np.uint8(np.clip(a, 0, 255))
  f = BytesIO()
  PIL.Image.fromarray(a).save(f, fmt)
  clear_output(wait = True)
  display(Image(data=f.getvalue()))
```

�����Ŏ������͗V��ŕ֗��ɑΘb�^TensorFlow�Z�b�V�������J�n���܂��B
���s�\��.py�t�@�C���ł�����s���Ă���ꍇ�́A
�ʏ�̃Z�b�V���������l�ɋ@�\���܂��B

```python
sess = tf.InteractiveSession()
```

## �v�Z�̕֋X�֐�


```python
def make_kernel(a):
  """�􍞂݃J�[�l����2�����z���ό`����"""
  a = np.asarray(a)
  a = a.reshape(list(a.shape) + [1,1])
  return tf.constant(a, dtype=1)

def simple_conv(x, k):
  """�ȗ������ꂽ2�����􍞂݉��Z"""
  x = tf.expand_dims(tf.expand_dims(x, 0), -1)
  y = tf.nn.depthwise_conv2d(x, k, [1, 1, 1, 1], padding='SAME')
  return y[0, :, :, 0]

def laplace(x):
  """�z���2�������v���V�A�����v�Z����"""
  laplace_k = make_kernel([[0.5, 1.0, 0.5],
                           [1.0, -6., 1.0],
                           [0.5, 1.0, 0.5]])
  return simple_conv(x, laplace_k)
```

## PDE�̒�`

�������̒r�͊��S500 x 500�̐����`�ŁA
���R�E�Ɍ�����قƂ�ǂ̒r�̃P�[�X�Ɠ��l�Ȃ��̂ƂȂ��Ă��܂��B

```python
N = 500
```

�����Ŏ������͒r�����A�����ɂ������̉J�����~�点�܂��B

```python
# �������� -- �������̉J����r�ɍ~�点��

# ���ׂĂ�0�Őݒ�
u_init = np.zeros([N, N], dtype=np.float32)
ut_init = np.zeros([N, N], dtype=np.float32)

# �������̉J���������_���ȃ|�C���g�Œr�ɍ~�点��
for n in range(40):
  a,b = np.random.randint(0, N, 2)
  u_init[a,b] = np.random.uniform()

DisplayArray(u_init, rng=[-0.1, 0.1])
```

![jpeg](https://www.tensorflow.org/images/pde_output_1.jpg)


����ł́A�����������̏ڍׂ��L�q���܂��傤�B


```python
# �p�����[�^:
# eps -- ���ԕ���\
# damping -- �g����
eps = tf.placeholder(tf.float32, shape=())
damping = tf.placeholder(tf.float32, shape=())

# �V�~�����[�V�����̏�Ԃ̂��߂̕ϐ��𐶐�����
U  = tf.Variable(u_init)
Ut = tf.Variable(ut_init)

# ���U������PDE�̍X�V���[��
U_ = U + eps * Ut
Ut_ = Ut + eps * (laplace(U) - damping * Ut)

# ��Ԃ��X�V���邽�߂̉��Z
step = tf.group(
  U.assign(U_),
  Ut.assign(Ut_))
```

## �V�~�����[�V�����̎��s

�������������낭�Ȃ�Ƃ���ł� -- �P����for���[�v�Ŏ��Ԃ�i�߂Ă݂܂��傤�B

```python
# ��Ԃ����������ŏ���������
tf.global_variables_initializer().run()

# PDE��1000�X�e�b�v���s
for i in range(1000):
  # �V�~�����[�V�����̃X�e�b�v���s
  step.run({eps: 0.03, damping: 0.04})
  DisplayArray(U.eval(), rng=[-0.1, 0.1])
```

![jpeg](https://www.tensorflow.org/images/pde_output_2.jpg)

���Ă�������! �����g�ł�!
