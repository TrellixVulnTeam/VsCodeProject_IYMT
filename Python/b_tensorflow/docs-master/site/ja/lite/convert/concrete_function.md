# ��ۊ֐��̐���

TensorFlow 2.0 ���f���� TensorFlow Lite �ɕϊ�����ɂ́A���f������ۊ֐� (concrete function) �Ƃ��ăG�N�X�|�[�g����K�v������܂��B ���̃h�L�������g�ł́A��ۊ֐��Ƃ͉����A�����̃��f������ǂ̂悤�ɋ�ۊ֐��𐶐����邩�A�ɂ��ĊT�����܂��B

[TOC]

## �w�i

TensorFlow 2.0 �ł́AEager Execution ���f�t�H���g�ŃI���ɂȂ��Ă��܂��B TensorFlow �ɂ����� Eager Execution �Ƃ́A�O���t���쐬�����ɃI�y���[�V�����𑦎��]�����閽�ߌ^�v���O���~���O���̂��Ƃł��B�e�I�y���[�V�����́A��Ŏ��s���邽�߂Ɍv�Z�O���t���\�z����̂ł͂Ȃ��A��̓I�Ȓl��Ԃ��܂��B Eager Execution �Ɋւ���ڍׂȃK�C�h��[������](https://github.com/tensorflow/docs/blob/master/site/en/guide/eager.ipynb)�ɂ���܂��B

Eager Execution �Ŗ��ߓI�Ɏ��s����ƊJ���ƃf�o�b�O�����Θb�I�ɂȂ�܂����A�f�o�C�X�ւ̃f�v���C�͂ł��Ȃ��Ȃ�܂��B `tf.function` API �̓��f�����O���t�Ƃ��ĕۑ����邱�Ƃ��\�ɂ��܂��B ����� TensorFlow2.0 �� TensorFlow Lite �����s���邽�߂ɕK�v�ł��B `tf.function` �f�R���[�^�Ń��b�v���ꂽ�I�y���[�V�����͂��ׂăO���t�Ƃ��ăG�N�X�|�[�g�ł���̂ŁA TensorFlow Lite FlatBuffer �t�H�[�}�b�g�ɕϊ��ł��܂��B

## �p��

���̕����ł͎��̗p����g�p���܂��B

*   **�V�O�l�`��** - ��A�̃I�y���[�V�����̓��͂Əo��.
*   **��ۊ֐�**  - �P��̃V�O�l�`�������O���t.
*   **�����֐�**  -  �������̋�ۊ֐��O���t��1�̊֐����ɃJ�v�Z�������� Python �̌Ăяo���\�I�u�W�F�N�g.

## ���@�_

���̏͂ł́A��ۊ֐����G�N�X�|�[�g������@��������܂��B

### �֐��� `tf.function` �f�R�[���[�^��t�^����

�֐��� `tf.function` �f�R���[�^��t�^����ƁA���̊֐��̃I�y���[�V�������܂� *�����֐�* ����������܂��B `tf.function` �̃f�R���[�^���t�����Ă��Ȃ��I�y���[�V�����͂��ׂ� Eager Execution �ŕ]������܂��B �ȉ��̗�� `tf.function` �̎g�����������Ă��܂��B

```python
@tf.function
def pow(x):
  return x ** 2
```

```python
tf.function(lambda x : x ** 2)
```

### �ۑ��������I�u�W�F�N�g�𐶐�����

`tf.function` �́A` tf.Module` �I�u�W�F�N�g�̈ꕔ�Ƃ��ĕۑ����邱�Ƃ��ł��܂��B ���̍ہA�ϐ��� `tf.Module` ���ň�x������`�����ׂ��ł��B �ȉ��̗�� `Checkpoint` ��h������N���X���쐬���邽�߂�2�̈قȂ�A�v���[�`�������Ă��܂��B

```python
class BasicModel(tf.Module):

  def __init__(self):
    self.const = None

  @tf.function
  def pow(self, x):
    if self.const is None:
      self.const = tf.Variable(2.)
    return x ** self.const

root = BasicModel()
```

```python
root = tf.Module()
root.const = tf.Variable(2.)
root.pow = tf.function(lambda x : x ** root.const)
```

### ��ۊ֐����G�N�X�|�[�g����

��ۊ֐��́ATensorFlow Lite ���f���ɕϊ�������ASavedModel �ɃG�N�X�|�[�g������ł���O���t���`���܂��B
�����֐������ۊ֐����G�N�X�|�[�g����ɂ́A�V�O�l�`�����`����K�v������܂��B
�V�O�l�`���͎��̂悤�ɂ��Ē�`�ł��܂��B

*   `tf.function` �� ` input_signature` �p�����[�^���`���܂��B
*   `tf.TensorSpec` �� ` get_concrete_function` �ɓn���܂�: ��) `tf.TensorSpec(shape=[1], dtype = tf.float32)`
*   �T���v���̓��̓e���\���� `get_concrete_function` �ɓn���܂�: ��) `tf.constant(1., shape=[1])`

���̗�� `tf.function` �� ` input_signature` �p�����[�^���`������@�������Ă��܂��B

```python
class BasicModel(tf.Module):

  def __init__(self):
    self.const = None

  @tf.function(input_signature=[tf.TensorSpec(shape=[1], dtype=tf.float32)])
  def pow(self, x):
    if self.const is None:
      self.const = tf.Variable(2.)
    return x ** self.const

# tf.Module �I�u�W�F�N�g�𐶐�
root = BasicModel()

# ��ۊ֐����擾
concrete_func = root.pow.get_concrete_function()
```

�ȉ��̗�ł́A�T���v���̓��̓e���\���� `get_concrete_function` �ɓn���Ă��܂��B

```python
# tf.Module �I�u�W�F�N�g�𐶐�
root = tf.Module()
root.const = tf.Variable(2.)
root.pow = tf.function(lambda x : x ** root.const)

# ��ۊ֐����擾
input_data = tf.constant(1., shape=[1])
concrete_func = root.pow.get_concrete_function(input_data)
```

## �v���O������

```python
import tensorflow as tf

# tf.Module �I�u�W�F�N�g��������
root = tf.Module()

# �ϐ�����x�����C���X�^���X������
root.var = None

# ���Z�����O�Ɍv�Z����Ȃ��悤�Ɋ֐����`
@tf.function
def exported_function(x):
  # �ϐ��͈�x������`�ł��܂��B�ϐ��͊֐����Œ�`�ł��܂����A�֐��O�̎Q�Ƃ��܂߂�K�v������܂��B
  if root.var is None:
    root.var = tf.Variable(tf.random.uniform([2, 2]))
  root.const = tf.constant([[37.0, -23.0], [1.0, 4.0]])
  root.mult = tf.matmul(root.const, root.var)
  return root.mult * x

# tf.Module�I�u�W�F�N�g�̈ꕔ�Ƃ��Ċ֐���ۑ�
root.func = exported_function

# ��ۊ֐����擾
concrete_func = root.func.get_concrete_function(
  tf.TensorSpec([1, 1], tf.float32))
```

## �悭���鎿��

### ��ۊ֐��� SavedModel �Ƃ��ĕۑ�����ɂ͂ǂ�����΂����ł����H

TensorFlow Lite �ɕϊ�����O�� TensorFlow ���f����ۑ��������ꍇ�́A SavedModel �Ƃ��ĕۑ�����K�v������܂��B
��ۊ֐����擾�������Ƃ� `tf.saved_model.save` ���Ăяo�����ƂŃ��f����ۑ��ł��܂��B��q�̗�̏ꍇ�A�ȉ��̂悤�ɂ��ĕۑ��ł��܂��B

```python
tf.saved_model.save(root, export_dir, concrete_func)
```

SavedModel �̎g�p���@�̏ڍׂɂ��ẮA[SavedModel �K�C�h](https://github.com/tensorflow/docs/blob/master/site/en/guide/saved_model.ipynb) ���Q�Ƃ��Ă��������B


### SavedModel �����ۊ֐��𓾂�ɂ͂ǂ�����΂����ł����H

SavedModel ���̊e�ے��֐��́A�V�O�l�`���L�[�ɂ���Ď��ʂł��܂��B
�f�t�H���g�̃V�O�l�`���L�[�� `tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY` �ł��B�ȉ��̗�́A���f�������ۊ֐����擾������@�������Ă��܂��B

```python
model = tf.saved_model.load(export_dir)
concrete_func = model.signatures[
  tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
```

### `tf.Keras` ���f�������ۊ֐��𓾂�ɂ͂ǂ������炢���ł����H

���@��2����܂�:

1.  ���f���� SavedModel �Ƃ��ĕۑ����܂��B�ۑ��������ɋ�ۊ֐������������̂ŁA��q�̗v�̂Ń��f�������[�h���ċ�ۊ֐����擾���邱�Ƃ��ł��܂��B
2.  ���L�̂悤�Ƀ��f���� `tf.function` �Ń��b�v���܂��B


```python
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x=[-1, 0, 1, 2, 3, 4], y=[-3, -1, 1, 3, 5, 7], epochs=50)

# ��ۊ֐��� Keras ���f������擾
run_model = tf.function(lambda x : model(x))

# ��ۊ֐���ۑ�
concrete_func = run_model.get_concrete_function(
    tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))
```
