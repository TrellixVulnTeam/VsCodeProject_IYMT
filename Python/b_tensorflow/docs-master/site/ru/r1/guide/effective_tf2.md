# �K�p�{ �y�������|���x���r�p���� TensorFlow 2.0?

Note: �B���� �y�~�������}�p���y�� �r �������} ���p�x�t�u�|�u ���u���u�r�u�t�u�~�p �� �����}�������� ���������{���s���r���������u�s��
Tensorflow �������q���u�����r�p �~�p ���q���u�����r�u�~�~���� �~�p���p�|�p��. �P�����{���|���{�� �������� ���u���u�r���t �~�u
���r�|���u������ �����y���y�p�|���~���}, �}�� �~�u �s�p���p�~���y�����u�} ������ ���~ �~�p 100% �p�{�{�����p���u�~ �y ���������r�u�������r���u��
[�����y���y�p�|���~���z �t���{���}�u�~���p���y�y �~�p �p�~�s�|�y�z���{���} ���x���{�u](https://www.tensorflow.org/?hl=en).
�E���|�y �� �r�p�� �u������ �����u�t�|���w�u�~�y�u �{�p�{ �y�������p�r�y���� �������� ���u���u�r���t, �}�� �q���t�u�} �����u�~�� ���p�t��
���r�y�t�u���� pull request �r [tensorflow/docs](https://github.com/tensorflow/docs)
���u�����x�y�������y�z GitHub. �E���|�y �r�� �������y���u �����}������ ���t�u�|�p���� �t���{���}�u�~���p���y�� ���� Tensorflow
�|�������u (���t�u�|�p���� ���p�} ���u���u�r���t �y�|�y �������r�u���y���� ���u���u�r���t �����t�s�������r�|�u�~�~���z �{�u�}-���� �t�����s�y�}),
�~�p���y���y���u �~�p�} �~�p
[docs-ru@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ru).

�B TensorFlow 2.0 �q���|�y ���t�u�|�p�~�� �~�u���{���|���{�� �y�x�}�u�~�u�~�y�z, �{�����������u �����x�r���|���� �r���u�} �����|���x���r�p���u�|���} TensorFlow 
���p�q�����p���� �q���|�u�u �������t���{���y�r�~��. �B TensorFlow 2.0 �q���|�y ���t�p�|�u�~��
[�~�u�~���w�~���u API](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md),
�������u�����r�������y�u �y �y�������|���x���u�}���u API �q���|�y ���������p�q�����p�~�� 
([���q���u�t�y�~�u�~�� RNN](https://github.com/tensorflow/community/blob/master/rfcs/20180920-unify-rnn-interface.md),
[�p ���p�{�w�u �������y�}�y�x�p��������](https://github.com/tensorflow/community/blob/master/rfcs/20181016-optimizer-unification.md)),
���|�������u�~�p �y�~���u�s���p���y�� �� ���p�q�����u�z �����u�t���z Python �r ���u�w�y�}�u
[Eager execution](https://www.tensorflow.org/guide/eager).

�B�� �}�~���s�y��
[�x�p���������p�� RFC](https://github.com/tensorflow/community/pulls?utf8=%E2%9C%93&q=is%3Apr)
���q�������~���|�y���� �����~���r�~���u �y�x�}�u�~�u�~�y��, �{�����������u �x�p�������~���� TensorFlow 2.0. �B �������} �t���{���}�u�~���u
�q���t�u�� �����{�p�x�p�~��, �{�p�{ �t���|�w�u�~ �r���s�|���t�u���� ���������u���� ���p�q������ �� �~���r���} TensorFlow 2.0.
�P���t���p�x���}�u�r�p�u������, ������ �r�� ���w�u �x�~�p�{���}�� �� TensorFlow 1.x.

## �K���p���{�y�z �����y�����{ �����~���r�~���� �y�x�}�u�~�u�~�y�z

### �X�y�����{�p API

�M�~���s�y�u API �q���|�y �|�y�q��
[���t�p�|�u�~��, �|�y�q�� ���u���u�}�u���u�~��](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md)
�r TF 2.0. �R�p�}���}�y �{�������~���}�y �y�x�}�u�~�u�~�y���}�y ���r�|���������� ���t�p�|�u�~�y�u `tf.app`, `tf.flags`, �p ���p�{�w�u
`tf.logging` �r �����|���x�� �~���r���z �q�y�q�|�y�����u�{�y �� �����{���������} �y�������t�~���} �{���t���}
[absl-py](https://github.com/abseil/abseil-py), ���u���u�}�u���u�~�y�u �������u�{�����r, �{�����������u �q���|�y �r
`tf.contrib`, �p ���p�{�w�u ���y�����{�p �����~���r�~���s�� �y�}�u�~�y `tf.*`: ���u�t�{�� �y�������|���x���u�}���u �����~�{���y�y 
�q���|�y ���q���u�t�y�~�u�~�� �r �����t�u�|���~���u �}���t���|�y, �~�p�����y�}�u�� `tf.math`. �N�u�{�����������u API �q���|�y �x�p�}�u�~�u�~��
�y�� 2.0 ���{�r�y�r�p�|�u�~���p�}�y - `tf.summary`, `tf.keras.metrics`, �y
`tf.keras.optimizers`. �R�p�}���z �������������z �����������q �p�r�����}�p���y���u���{�y ���u���u�y�}�u�~���r�p���� �r���u �����~�{���y�y -
������ �r���������|���x���r�p�������� [���{���y�������} �t�|�� ���q�~���r�|�u�~�y�� �t�� 2.0](upgrade.md).

### �@�{���y�r�~���z Eager execution

�B TensorFlow 1.X ���� �����|���x���r�p���u�|�� �����u�q���r�p�|������ �r�������~���� ���������y����
[�p�q�������p�{���~���u ���y�~���p�{���y���u���{���u �t�u���u�r��](https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D0%BE%D0%B5_%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE) (�s���p��) �����y �����}�����y API �r���x���r���r `tf.*`. �D�|�� �������s�� �q���|�� �~���w�~�� �r�������~����
�{���}���y�|�y�����r�p���� �t�u���u�r��, ���u���u�t�p�r�p�� �~�p�q���� �����|�����p�u�}���� �y �r�����t�����y�� ���u�~�x�������r �{ �r���x���r�� 
`session.run()`. TensorFlow 2.0 ���u���u���� �r�������|�~���u�� �r���u �����u���p���y�y �}�s�~���r�u�~�~�� (�������~��
���p�{ �w�u, �{�p�{ �y ���q�����~���z Python), �r���u �s���p���� �y ���u�����y�y ���u���u���� �q���t���� ���p�q�����p���� �{�p�{
�����p�~�t�p�����~���u �r�������|�~�u�~�y�u �����u���p���y�z.

�Q�p�~�����u �����q�����~���} �������t���{�����} eager execution �q���| �}�u�����t `tf.control_dependencies()`,
�{�����������z ���u���u���� �~�u �����u���q�u������, �y �r���u ���������{�y �{���t�p �q���t���� �y�������|�~���������� �r �������|�u�t���r�p���u�|���~���}
���������t�{�u, �������u�t�u�|�u�~�~���} `tf.function`. �R���������~�~�y�z �{���t �q���t�u�� �r�������|�~���������� �r 
�������u�t�u�|�u�~�~���} �u�}�� ���������t�{�u.

### �N�y�{�p�{�y�� �s�|���q�p�|���~���� ���u���u�}�u�~�~����

TensorFlow 1.X �r�~�������u�~�~�u �����|�p�s�p�|���� �~�p �s�|���q�p�|���~���u ���u���u�}�u�~�~���u. �K���s�t�p �r�� �r���x���r�p�|�y
`tf.Variable()`, ���� �����p ���u���u�}�u�~�~�p�� �����}�u���p�|�p���� �r �����p�~�t�p�����~���z �s���p�� �y �������p�r�p�|�p���� ���p�}
�t�p�w�u �u���|�y ���w�u �q���|�� �y�x�}�u�~�u�~�� �y�}��, �����y���r���u�~�~���u �������z ���u���u�}�u�~�~���z. �B�� �}���s�|�y �r���������p�~���r�y����
������ ���u���u�}�u�~�~���� `tf.Variable`, �~�� �����|���{�� �u���|�y ���u�q�u �q���|�� �y�x�r�u�����~�� �y�}��, �{�����������u �q���|��
�����y���r���u�~�� �u�z �����y �����x�t�p�~�y�y. �B ���u�x���|�����p���u �r���u �}�u���p�~�y�x�}�� �q���|�y �~�p�����p�r�|�u�~�� �~�p ����, �������q��
�����}������ �����|���x���r�p���u�|�� ���������{�p���� �y�}�� �y�� ���u���u�}�u�~�~���� �u���u ���p�x: `tf.get_global_step()`, 
`tf.global_variables_initializer()`, �������y�}�y�x�p��������, �{�����������u ���p�������y�����r�p�|�y
�s���p�t�y�u�~���� ���� �r���u�} ���q�����p�u�}���} ���u���}�u�~�~���} �y ���p�{ �t�p�|�u�u. �B TensorFlow 2.0 �����y �}�u���p�~�y�x�}�� �q���|�y
���������p�~�u�~�� ([�P�u���u�}�u�~�~���u 2.0 RFC](https://github.com/tensorflow/community/pull/11))
�r �����|���x�� �~���r���s��: ���|�u�t�y �x�p �������������~�y�u�} ���p�q�����y�� ���u���u�}�u�~�~����! �E���|�y �r�� �������u�����u���u `tf.Variable`
(�~�p�����y�}�u��, �u�z �q���t�u�� �����y���r���u�~�� �~���r���u �y�}��), ���� �����p���p�� �q���t�u�� ���t�p�|�u�~�p �y�x ���p�}�����y �r ���������t�{�u
���������u�����p garbage collection.

�S���u�q���r�p�~�y�u ���|�u�t�y���� �x�p ���u���u�}�u�~�~���}�y �����x�t�p�u�� �t�������|�~�y���u�|���~���� �~�p�s�����x�{�� �~�p �����|���x���r�p���u�|��,
�~�� �r ���|�����p�u �� ���q���u�{���p�}�y Keras (���}. �~�y�w�u), ������ �~�p�s�����x�{�p - �}�y�~�y�}�p�|���~�p��.

### �U���~�{���y�y, �p �~�u ���u�����y�y

�B���x���r `session.run()` ���p�q�����p�| ���������y �{�p�{ �r���x���r �����~�{���y�y: �r�� �������u�t�u�|���|�y �r�r���t�~���u �t�p�~�~���u
�y �r���x���r�p�| �����~�{���y��, �����|�����p�� �~�p �r�������t�u ���u�x���|�����p����. �B TensorFlow 2.0, �r�� �}���w�u���u
�t�u�{�����y�����r�p���� �����~�{���y�� Python �����y �����}�����y `tf.function()`, �����}�u���y�r �u�v �{�p�{ JIT-�{���}���y�|�y�����u�}����,
�������q�� TensorFlow �x�p���������y�| �u�u �~�p ���t�~���} �u�t�y�~�����r�u�~�~���} �s���p���u
([�U���~�{���y�y 2.0 RFC](https://github.com/tensorflow/community/pull/20)). �^������
�}�u���p�~�y�x�} �����x�r���|���u�� TensorFlow 2.0 �����|�����y���� �r���u �����u�y�}�����u�����r�p ���u�w�y�}�p graph:

-   �P�����y�x�r���t�y���u�|���~��������: �����~�{���y�y �}���s���� �q������ �������y�}�y�x�y�����r�p�~�� (�������u���u�~�y�u ���x�|���r �s���p���p,
    ���|�y���~�y�u ���t���p �y ���p�{ �t�p�|�u�u)
-   �P�������p���y�r�~��������: �U���~�{���y�y �}���s���� �q������ ���{�����������y�����r�p�~��
    �y�|�y �y�}���������y�����r�p�~�� �����r�������~�� ([�R�������p�~�u�~�y�u �}���t�u�|�u�z 2.0 RFC](https://github.com/tensorflow/community/pull/34)),
    �����x�r���|���� �����|���x���r�p���u�|���} �y�������|���x���r�p���� �}���t���|���~���u �����~�{���y�y TensorFlow �y �t�u�|�y�������� �y�}�y.

```python
# TensorFlow 1.X
outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# TensorFlow 2.0
outputs = f(input)
```

�R �~���r���z �r���x�}���w�~���������� ������������ �y�������|���x���r�p���� �r�}�u�����u �{���t Python �y TensorFlow, �}�� ���w�y�t�p�u�}
������ �����|���x���r�p���u�|�y �r���������|���x���������� �r���u�}�y �����u�y�}�����u�����r�p�}�y �r�����p�x�y���u�|���~�������y ���x���{�p Python.
�N�� ���������p���y�r�~���z TensorFlow �r�������|�~���u�� �����u���p���y�y �r ���{�����w�u�~�y�y �q�u�x �y�~���u�������u���p�������p Python -
�~�p �}���q�y�|���~���� �����������z�����r�p��, C++ �y JavaScript. �X�����q�� �����}������ �����|���x���r�p���u�|���} �|�u�s�{�� ���u���u���y���p����
���r���z �{���t �����y �y�������|���x���r�p�~�y�y �~���r���z `@tf.function`, �y�������|���x���z [AutoGraph](autograph.ipynb)
�t�|�� �{���~�r�u�����p���y�y �{���t�p Python �r �y�� ���{�r�y�r�p�|�u�~���� TensorFlow:

*   `print` -> `tf.print`
*   `assert` -> `tf.Assert`
*   `for`/`while` -> `tf.while_loop` (�����t�t�u���w�y�r�p�������� `break` �y `continue`)
*   `if` -> `tf.cond`
*   `for _ in dataset` -> `dataset.reduce`

AutoGraph �����t�t�u���w�y�r�p�u�� �r�|���w�u�~�~���u �����~�{���y�y �r ���������t�{�u �r�������|�~�u�~�y�� �������s���p�}�}��, ������
�t�u�|�p�u�� �r���x�}���w�~���} �������y�x�r���t�y���u�|���~�� �y �������~�� �r�~�u�t�������� �{���}���|�u�{���~���u �������s���p�}�}��
�}�p���y�~�~���s�� ���q�����u�~�y��, �~�p�����y�}�u�� ���p�{�y�u �{�p�{ �������|�u�t���r�p���u�|���~���u �}���t�u�|�y, ���q�����u�~�y�u ��
�����t�{���u���|�u�~�y�u�}, �����q�����r�u�~�~���u ���y�{�|�� ���q�����u�~�y�� �y �}�~���s�y�u �t�����s�y�u.

## �Q�u�{���}�u�~�t�p���y�y �y �y�t�y���}�� TensorFlow 2.0

### �Q�u���p�{�������y�~�s �{���t�p �~�p �}�p�|���u �����~�{���y�y

�X�p������ �y�������|���x���u�}���z ���p�q�|���~ �y�������|���x���r�p�~�y�� �r TensorFlow 1.X ���p�q�����p�| ���� �����y�~���y����
kitchen sink ("�{�������~�~���z ���p�{���r�y�~��"), �{���s�t�p �q���p �r���|���w�u�~�p �����r���{�����~�������� �r���u�� �r���x�}���w�~���� �r�����y���|�u�~�y�z,
�p �x�p���u�} �r���q���p�~�~���u ���u�~�x������ �r�����y���|���|�y���� �� �����}�������� `session.run()`. �B TensorFlow 2.0
�����|���x���r�p���u�|�y �t���|�w�~�� ���p�}�y ���p�x�q�y�r�p���� �{���t �~�p �q���|�u�u �}�u�|�{�y�u �����~�{���y�y �y �r���x���r�p���� �{�p�w�t����
�{���s�t�p ������ �~�u���q�����t�y�}��. �N�u���q���x�p���u�|���~�� �t�u�{�����y�����r�p���� �{�p�w�t���� �y�x �����y�� �~�u�q���|�����y�� �����~�{���y�z
�� `tf.function`; �y�������|���x���z `tf.function` �t�|�� �t�u�{�����y�����r�p�~�y�� �����|���{�� �r�������{���������r�~�u�r����
�r�����y���|�u�~�y�z - �~�p�����y�}�u��, ���t�y�~ ���p�s ���q�����u�~�y�� �y�|�y �������}���s�� �����������t�p �t�|�� �}���t�u�|�y.

### �I�������|���x���z ���|���y �y �}���t�u�|�y Keras �t�|�� �������p�r�|�u�~�y�� ���u���u�}�u�~�~���}�y

�M���t�u�|�y �y ���|���y Keras �����u�t�|�p�s�p���� �y�������|���x���r�p���� ���t���q�~���u ���r���z�����r�� `.variables`, �{�����������u
���u�{�������y�r�~�� �����q�y���p�u�� �r���u �x�p�r�y���y�}���u ���u���u�}�u�~�~���u. �^���� �x�~�p���y���u�|���~�� ���q�|�u�s���p�u�� �|���{�p�|���~���u �������p�r�|�u�~�y�u
���u���u�}�u�~�~���}�y.

�R���p�r�~�y���u:

```python
def dense(x, W, b):
  return tf.nn.sigmoid(tf.matmul(x, W) + b)

@tf.function
def multilayer_perceptron(x, w0, b0, w1, b1, w2, b2 ...):
  x = dense(x, w0, b0)
  x = dense(x, w1, b1)
  x = dense(x, w2, b2)
  ...

# �N�p�} �r���u ���p�r�~�� �����y�t�u������ �������p�r�|������ w_i �y b_i, ���p�{ �{�p�{ �y�� �������}�� �������u�t�u�|���������� �~�u �r �{���t�u.
```

�B�u�����y�� �� �y�������|���x���r�p�~�y�u�} Keras:

```python
# �K�p�w�t���z ���|���z �}���w�u�� �q������ �r���x�r�p�~ �� ���y�s�~�p���������z ���p�r�~���z linear(x)
layers = [tf.keras.layers.Dense(hidden_size, activation=tf.nn.sigmoid) for _ in range(n)]
perceptron = tf.keras.Sequential(layers)

# layers[3].variables => returns [w3, b3]
# perceptron.variables => returns [w0, b0, ...]
```

�M���t�u�|�y �y ���|���y Keras �~�p���|�u�t���������� �y�x `tf.train.Checkpointable` �y �y�~���u�s���y������������ ��
`@tf.function`, ������ �t�u�|�p�u�� �r���x�}���w�~���} ���������p�~�y���� �y�|�y �~�u���������u�t�����r�u�~�~�� ���{�����������y�����r�p����
���������p�~�u�~�~���u �}���t�u�|�y �y�x ���q���u�{�����r Keras. �N�u���q���x�p���u�|���~�� �y�������|���x���r�p���� �}�u�����t `.fit()` �y�x
Keras API �t�|�� �����y�� �y�~���u�s���p���y�z.

�B���� �����y�}�u�� transfer learning (���u���u�~�����p ���q�����u�~�y��), �{�����������z �t�u�}���~�������y�����u�� �{�p�{ �|�u�s�{��
�����q���p���� �����t�}�~���w�u�����r�� �~�u���q�����t�y�}���� ���u���u�}�u�~�~���� �� �����}�������� Keras. �P���u�t�����|���w�y�}, �}�� ���q�����p�u�}
���p�x�r�u���r�|�u�~�~���� (multi-head) �}���t�u�|�� �� ���q���y�} �{�����~�u�} (trunk):

```python
trunk = tf.keras.Sequential([...])
head1 = tf.keras.Sequential([...])
head2 = tf.keras.Sequential([...])

path1 = tf.keras.Sequential([trunk, head1])
path2 = tf.keras.Sequential([trunk, head2])

# �O�q�����p�u�} �~�p �����~���r�~���} �t�p���p���u���u:
for x, y in main_dataset:
  with tf.GradientTape() as tape:
    prediction = path1(x)
    loss = loss_fn_head1(prediction, y)
  # �O�t�~���r���u�}�u�~�~�� �������y�}�y�x�y�����u�} �{�����u�~�� �y �r�u���p ���u���r���z �r�u���r�y:
  gradients = tape.gradients(loss, path1.variables)
  optimizer.apply_gradients(gradients, path1.variables)

# �N�p�������p�y�r�p�u�} �r���������� �r�u���r��, �����r�������~�� �y�������|���x���� �{�����u�~��:
for x, y in small_dataset:
  with tf.GradientTape() as tape:
    prediction = path2(x)
    loss = loss_fn_head2(prediction, y)
  # �O�����y�}�y�x�y�����u�} �r�u���p �����|���{�� �r���������z �r�u���r�y, �q�u�x �r�u�����r �{�����~��:
  gradients = tape.gradients(loss, head2.variables)
  optimizer.apply_gradients(gradients, head2.variables)

# 
# �M���w�u�} ���������p�~�y���� �r�����y���|�u�~�y�� �{�����~��, �������q�� �t�����s�y�u ���p�{�w�u �}���s�|�y �y�} �r���������|���x���r�p��������.
tf.saved_model.save(trunk, output_path)
```

### �O�q���u�t�y�~�u�~�y�u tf.data.Datasets �y @tf.function

�P���y ���q�����u�~�y�y �}���t�u�|�y �~�p �t�p�~�~����, �{�����������u �~�p�����t�������� �r ���p�}�����y, �y�������|���x���z �����p�~�t�p�����~���z
�y���u���p������ Python. �B �������p�|���~���� ���|�����p���� `tf.data.Dataset` ���r�|���u������ �|�������y�} �����������q���}
�t�|�� ���������{�p �����u�~�y�����r�����~���� �t�p�~�~���� �� �t�y���{�p. �D�p���p���u���� ���r�|����������
[�y���u���y�����u�}���}�y (�~�u �y���u���p�������p�}�y)](https://docs.python.org/3/glossary.html#term-iterable),
�y ���p�q�����p���� ���p�{ �w�u, �{�p�{ �y �t�����s�y�u �y���u���p�������� Python �r ���u�w�y�}�u Eager. �B�� �}���w�u���u �~�p�y�q���|�u�u
�����|�~�� �y�������|���x���r�p���� �p���y�~�������~�~���u �r���x�}���w�~�������y prefetch �y stream �����y �����}�����y
`tf.function()`, �{���������p�� �x�p�}�u�~���u�� �y���u���p���y�y Python �y�� ���{�r�y�r�p�|�u�~���p�}�y �����u���p���y�z �s���p�����r
���������u�t�����r���} AutoGraph.

```python
@tf.function
def train(model, dataset, optimizer):
  for x, y in dataset:
    with tf.GradientTape() as tape:
      prediction = model(x)
      loss = loss_fn(prediction, y)
    gradients = tape.gradients(loss, model.variables)
    optimizer.apply_gradients(gradients, model.variables)
```

�E���|�y �r�� �y�������|���x���u���u �}�u�����t `.fit()` �y�x Keras API, ���� �r�p�} �~�u �����y�t�u������
�r���|�~���r�p�������� ���q �y���u���p���y�y �t�p���p���u���p.

```python
model.compile(optimizer=optimizer, loss=loss_fn)
model.fit(dataset)
```

### �B���������|���x���z���u���� �����u�}�y�����u�����r�p�}�y AutoGraph �� ���������t�{���} �r�������|�~�u�~�y�� Python

AutoGraph ���q�u�����u���y�r�p�u�� �����������q �{���~�r�u�����p���y�y �x�p�r�y���y�}���s�� ���� �t�p�~�~���� ���������t�{�p
�r�������|�~�u�~�y�� �r �u�s�� ���{�r�y�r�p�|�u�~���� �r ���u�w�y�}�u graph, �~�p�����y�}�u�� `tf.cond` �y `tf.while_loop`.

�E�t�y�~�����r�u�~�~���u �}�u������, �s�t�u �������r�|���u������ �x�p�r�y���y�}���z ���� �t�p�~�~���� ���������t���{ �r�������|�~�u�~�y�� ������
�������|�u�t���r�p���u�|���~���u �}���t�u�|�y. `tf.keras.layers.RNN` �y�������|���x���u�� ���|�u�}�u�~�� RNN, �����x�r���|����
�r�p�} ���p�x�r�u���~������ �����r������ �����p���y���u���{�y �y�|�y �t�y�~�p�}�y���u���{�y. �D�|�� �����y�}�u���p, �r�� �}���w�u���u
�y�������|���x���r�p���� �t�y�~�p�}�y���u���{���u ���p�x�r�u�������r�p�~�y�u:

```python
class DynamicRNN(tf.keras.Model):

  def __init__(self, rnn_cell):
    super(DynamicRNN, self).__init__(self)
    self.cell = rnn_cell

  def call(self, input_data):
    # [�q�p����, �r���u�}��, ���p���p�}�u������] -> [�r���u�}��, �q�p����, ���p���p�}�u������]
    input_data = tf.transpose(input_data, [1, 0, 2])
    outputs = tf.TensorArray(tf.float32, input_data.shape[0])
    state = self.cell.zero_state(input_data.shape[1], dtype=tf.float32)
    for i in tf.range(input_data.shape[0]):
      output, state = self.cell(input_data[i], state)
      outputs = outputs.write(i, output)
    return tf.transpose(outputs.stack(), [1, 0, 2]), state
```

�D�|�� �q���|�u�u �t�u���p�|���~���s�� �����y���p�~�y�u �r���x�}���w�~�������u�z AutoGraph ���x�~�p�{���}�����u���� ��
[�����{���r���t�����r���}](./autograph.ipynb).

### �I�������|���x���z���u tf.metrics �t�|�� ���q�����p �t�p�~�~���� �y tf.summary �t�|�� �|���s���r

�D�|�� �x�p���y���y �|���s���r, �y�������|���x���z���u `tf.summary.(scalar|histogram|...)`. �E���|�y �y�������|���x���r�p����
�t�p�~�~���u �}�u�����t�� �����t�u�|���~��, ���� ���~�y �~�u �q���t���� �~�y���u�s�� �t�u�|�p����; ���u�x���|�����p���� �t���|�w�~�� �q������
���u���u�~�p�����p�r�|�u�~�� �{ ���������r�u�������r�������u�}�� file writer, �����y �����}�����y �{���~���u�{�����~���s�� �}�u�~�u�t�w�u���p
(������ �����x�r���|�y�� �r�p�} �y�x�q�u�w�p���� �x�p���y���y �|���s���r �r file writer).

```python
summary_writer = tf.summary.create_file_writer('/tmp/summaries')
with summary_writer.as_default():
  tf.summary.scalar('loss', 0.1, step=42)
```

�X�����q�� �����q���p���� �t�p�~�~���u ���u���u�t �x�p���y������ �r �|���s, �y�������|���x���z���u `tf.metrics`. �M�u�����y�{�y
���������p�~������ ���r���u �������������~�y�u; ���~�y �~�p�{�p���|�y�r�p���� �x�~�p���u�~�y�� �y �r���x�r���p���p���� �����q�y���p���u�|���~���z 
���u�x���|�����p��, �{���s�t�p �r�� �r���x���r�p�u���u �}�u�����t `.result()`. �X�����q�� �����y�����y���� �r���u �x�~�p���u�~�y�� 
�y�������|���x���z���u �}�u�����t `.reset_states()`.

```python
def train(model, optimizer, dataset, log_freq=10):
  avg_loss = tf.keras.metrics.Mean(name='loss', dtype=tf.float32)
  for images, labels in dataset:
    loss = train_step(model, optimizer, images, labels)
    avg_loss.update_state(loss)
    if tf.equal(optimizer.iterations % log_freq, 0):
      tf.summary.scalar('loss', avg_loss.result(), step=optimizer.iterations)
      avg_loss.reset_states()

def test(model, test_x, test_y, step_num):
  loss = loss_fn(model(test_x), test_y)
  tf.summary.scalar('loss', loss, step=step_num)

train_summary_writer = tf.summary.create_file_writer('/tmp/summaries/train')
test_summary_writer = tf.summary.create_file_writer('/tmp/summaries/test')

with train_summary_writer.as_default():
  train(model, optimizer, dataset)

with test_summary_writer.as_default():
  test(model, test_x, test_y, optimizer.iterations)
```

�T�{�p�x�p�r ���p���{�� �� ���u�x���|�����p�}�y �r TensorBoard (`tensorboard --logdir
/tmp/summaries`), �r�� �}���w�u���u �r�y�x���p�|�y�x�y�����r�p���� �����|�����u�~�~���u �r �����t�u ���q�����u�~�y��
�t�p�~�~���u �~�p �s���p���y�{�p��.


