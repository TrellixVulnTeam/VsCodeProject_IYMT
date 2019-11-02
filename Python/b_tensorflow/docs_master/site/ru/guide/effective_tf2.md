# �^�����u�{���y�r�~���z TensorFlow 2.0

�B TensorFlow 2.0 ���t�u�|�p�~ �����t �y�x�}�u�~�u�~�y�z �t�u�|�p�����y�� �����|���x���r�p���u�|�u�z TensorFlow �q���|�u�u
�������t���{���y�r�~���}�y. TensorFlow 2.0 ���t�p�|�y�|
[�y�x�q���������~���u API](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md),
�������|�u ���u�s�� API �����p�|�y �q���|�u�u �����s�|�p�����r�p�~�~���}�y
([Unified RNNs](https://github.com/tensorflow/community/blob/master/rfcs/20180920-unify-rnn-interface.md),
[Unified Optimizers](https://github.com/tensorflow/community/blob/master/rfcs/20181016-optimizer-unification.md)),
�y �|�������u �y�~���u�s���y�����r�p�|���� �� Python runtime, ��
[Eager execution](https://www.tensorflow.org/guide/eager).

�M�~���s�y�u
[RFCs](https://github.com/tensorflow/community/pulls?utf8=%E2%9C%93&q=is%3Apr)
���q�������~�y�|�y �y�x�}�u�~�u�~�y�� �{�����������u �r�����|�y �r TensorFlow 2.0. �^���� �����{���r���t�����r��
�����u�t�����p�r�|���u�� �r�x�s�|���t �~�p �{���� �{�p�{ �t���|�w�~�p �r���s�|���t�u���� ���p�x���p�q�����{�p �r TensorFlow 2.0.
�P���u�t�����|�p�s�p�u������, ������ �r�� �x�~�p�{���}�� �� TensorFlow 1.x.

## �K���������{�p�� �r���t�u���w�{�p �����~���r�~���� �y�x�}�u�~�u�~�y�z

### �O���y�����{�p API

�M�~���s�� API �|�y�q��
[���t�p�|�u�~�� �|�y�q�� ���u���u�}�u���u�~��](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md)
�r TF 2.0. �N�u�{�����������u �y�x �����~���r�~���� �y�x�}�u�~�u�~�y�z �r�{�|�����p���� ���t�p�|�u�~�y�u `tf.app`,
`tf.flags`, �y `tf.logging` �r �����|���x��
[absl-py](https://github.com/abseil/abseil-py) �{�����������z ���u�z���p�� �� �����{���������}
�y�������t�~���} �{���t���}, ���u���u�~���� �������u�{�����r �{�����������u �~�p�����t�y�|�y���� �r `tf.contrib`, �y �����y�����{�y
�����~���r�~���s�� �������������p�~�����r�p �y�}�u�~ `tf.*` �������u�} ���u���u�}�u���u�~�y�� ���u�t�{�� �y�������|���x���u�}���� �����~�{���y�z
�r �����t���p�{�u���� �~�p�����t���q�y�u `tf.math`. �N�u���{���������u API �q���|�y �x�p�}�u���u�~�� ���r���y�}�y
���{�r�y�r�p�|�u�~���p�}�y 2.0 - `tf.summary`, `tf.keras.metrics`, �y `tf.keras.optimizers`.
�N�p�y�q���|�u�u �������������} �����������q���} �p�r�����}�p���y���u���{�y �����y�}�u�~�y���� �����y ���u���u�y�}�u�~���r�p�~�y�� ���r�|���u������
�y�������|���x���r�p�~�y�u [���{���y�����p ���q�~���r�|�u�~�y�� v2](upgrade.md).

### Eager execution

�B TensorFlow 1.X ���� �����|���x���r�p���u�|�u�z �����u�q���r�p�|������ �r�������~���� �����q�y���p����
[�p�q�������p�{���~���u ���y�~���p�{���y���u���{���u �t�u���u�r��](https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D0%BE%D0%B5_%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE)
(�s���p��) �r�������|�~���� `tf.*` API �x�p����������. �H�p���u�} �����|���x���r�p���u�|�y �t���|�w�~�� �r�������~����
���{���}���y�|�y�����r�p���� �p�q�������p�{���~���u ���y�~���p�{���y���u���{���u �t�u���u�r�� �������u�} ���u���u�t�p���y �}�~���w�u�����r�p
�r�������t�~���� �y �r�����t�~���� ���u�~�x�������r �r �r���x���r `session.run()`. TensorFlow 2.0 �r�������|�~���u������
�����p�x�� �w�u (�{�p�{ ������ ���q�����~�� �t�u�|�p�u�� Python) �y �r 2.0, �s���p���� �y ���u�����y�y �t���|�w�~��
���p�����}�p�����y�r�p�������� �{�p�{ �t�u���p�|�y ���u�p�|�y�x�p���y�y.

�O�t�~�y�} �x�p�}�u���~���} �����q�����~���} �������t���{�����} eager execution ���r�|���u������ ����, ������
`tf.control_dependencies()` �q���|�u�u �~�u �����u�q���u������, ���p�{ �{�p�{ �r���u ���������{�y �{���t�p
�r�������|�~���������� ���� �����u���u�t�y (�r �����u�t�u�|�p�� `tf.function`, �{���t �� �����q�����~���}�y �������u�{���p�}�y
�r�������|�~���u������ �r �����} ���������t�{�u �r �{�����������} ���~ �~�p���y���p�~).

### �N�u�� �q���|�����u �s�|���q�p�|���r

TensorFlow 1.X �x�s�p���y���u�|���~�� �x�p�r�y���u�| ���� �~�u���r�~���� �s�|���q�p�|���~���� �������������p�~�����r �y�}�u�~. �K���s�t�p
�r�� �r���x���r�p�|�y `tf.Variable()`, ���~�p �����}�u���p�|�p���� �r �s���p�� ���� ���}���|���p�~�y��, �y ���~�p
�������p�r�p�|�p���� ���p�} �t�p�w�u �u���|�y �r�� �������u�����|�y track ���u���u�}�u�~�~���z Python ���{�p�x���r�p�r���u�z �~�p
�~�u�s��. �B�� �}���w�u���u �x�p���u�} �r���������p�~���r�y���� ���� `tf.Variable`, �~�� �����|���{�� �u���|�y �r�� �x�~�p�|�y �y�}��
�� �{�����������} ���~�p �q���|�p �����x�t�p�~�p. �^���� �q���|�� ���|���w�~�� ���t�u�|�p���� �u���|�y �r�� �~�u �{���~�������|�y�����r�p�|�y
�����x�t�p�~�y�u ���u���u�}�u�~�~����. �B ���u�x���|�����p���u �������s��, ���p�x�}�~���w�p�|�y���� �r���u �r�y�t�� �}�u���p�~�y�x�}���r
�������p�r���y�u���� �����}������ �����|���x���r�p���u�|���} ���~���r�p �~�p�z���y �y�� ���u���u�}�u�~�~���u, �p �t�|�� �����u�z�}�r�����{���r -
�~�p�z���y �����x�t�p�~�~���u �����|���x���r�p���u�|���}�y ���u���u�}�u�~�~���u: �O�q�|�p�����y ���u���u�}�u�~�~����, �s�|���q�p�|���~���u
�{���|�|�u�{���y�y, �}�u�����t�� �����}�����~�y�{�y ���p�{�y�u �{�p�{ `tf.get_global_step()`,
`tf.global_variables_initializer()`, �������y�}�y�x�p�������� �~�u���r�~�� �r�����y���|�������y�u �s���p�t�y�u�~����
���� �r���u�} ���q�����p�u�}���} ���u���u�}�u�~�~���}, �y ��.�t. TensorFlow 2.0 ���������p�~���u�� �r���u �����y �}�u���p�~�y�x�}��
([Variables 2.0 RFC](https://github.com/tensorflow/community/pull/11)) �r �����|���x��
�}�u���p�~�y�x�}�p ���� ���}���|���p�~�y��: �O�����|�u�w�y�r�p�z���u ���r���y ���u���u�}�u�~�~���u! �E���|�y �r�� �������u�����|�y ���|�u�t
`tf.Variable`, ���~ �q���t�u�� �����y���u�~ ���q�������y�{���} �}���������p.

�S���u�q���r�p�~�y�u �������|�u�w�y�r�p���� �}�������� �����x�t�p�u�� �t�������|�~�y���u�|���~���� ���p�q������ �t�|�� �����|���x���r�p���u�|��,
�~�� �� ���q���u�{���p�}�y Keras (���}. �~�y�w�u), �~�p�s�����x�{�p �}�y�~�y�}�y�x�y�����r�p�~�p.

### �U���~�{���y�y, �~�u ���u�����y�y

�B���x���r `session.run()` ���������y ���������w �~�p �r���x���r �����~�{���y�y: �B�� �������u�t�u�|���u���u �r�r���t�~���u
�t�p�~�~���u, �����~�{���y�� �r���x���r�p�u������ �y �r�� �����|�����p�u���u �~�p�q���� ���u�x���|�����p�����r. �B TensorFlow 2.0,
�r�� �}���w�u���u �t�u�{�����y�����r�p���� �����~�{���y�� Python �y�������|���x���� `tf.function()` �������q�� �����}�u���y����
�u�u �t�|�� JIT �{���}���y�|�����y�y ���p�{ ������ TensorFlow �r�������|�~���u�� �u�s�� �{�p�{ �u�t�y�~���z �s���p��
([Functions 2.0 RFC](https://github.com/tensorflow/community/pull/20)). �^������
�}�u���p�~�y�x�} �����x�r���|���u�� TensorFlow 2.0 �����|�����y���� �r���u �����u�y�}�����u�����r�p ���u�w�y�}�p �s���p���p:

-   �P�����y�x�r���t�y���u�|���~��������: �����~�{���y�� �}���w�u�� �q������ �������y�}�y�x�y�����r�p�~�p (node pruning, kernel
    fusion, etc.)
-   �P�������p���y�r�~��������: �����~�{���y�� �}���w�u�� �q������ ���{�����������y�����r�p�~�p / ���u�y�}���������y�����r�p�~�p
    ([RFC SavedModel 2.0](https://github.com/tensorflow/community/pull/34), ������
    �����x�r���|���u�� �����|���x���r�p���u�|���} �����r�������~�� �y�������|���x���r�p���� �y �t�u�|�y�������� �}���t���|���~���}�y
    �����~�{���y���}�y TensorFlow.

```python
# TensorFlow 1.X
outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# TensorFlow 2.0
outputs = f(input)
```

�A�|�p�s���t�p���� �r���x�}���w�~�������y ���r���q���t�~�� ���u���u�}�u�w�p���� �{���t Python �y TensorFlow �����|���x���r�p���u�|�y
�}���s���� �r���������|���x���r�p�������� �����u�y�}�����u�����r�p�}�y �r�����p�x�y���u�|���~�������y Python. �N�� ���u���u�~�����y�}���z
TensorFlow �r�������|�~���u������ �r �{���~���u�{�����p��, ���p�{�y�� �{�p�{ mobile, C ++ �y JavaScript �q�u�x
�y�~���u�������u���p�������p Python. �X�����q�� �����|���x���r�p���u�|���} �~�u �~���w�~�� �q���|�� ���u���u���y�����r�p���� ���r���z �{���t
�����y �t���q�p�r�|�u�~�y�y `@ tf.function`, [AutoGraph](function.ipynb) �����u���q���p�x���u��
�����t�}�~���w�u�����r�� Python �{���~���������y������ �u�s�� �r ���{�r�y�r�p�|�u�~���p�� TensorFlow:

*   `for`/`while` -> `tf.while_loop` (`break` and `continue` are supported)
*   `if` -> `tf.cond`
*   `for _ in dataset` -> `dataset.reduce`

AutoGraph �����t�t�u���w�y�r�p�u�� �������y�x�r���|���~���u �r�|���w�u�~�y�� control flow, ������ �t�u�|�p�u�� �r���x�}���w�~���}
�������u�{���y�r�~�� �y �{���p���{�� ���u�p�|�y�x���r�p���� �}�~���s�y�u ���|���w�~���u �������s���p�}�}�� �}�p���y�~�~���s�� ���q�����u�~�y��,
���p�{�y�u �{�p�{ ���u�{�{�����u�~���~���u �}���t�u�|�y, ���q�����u�~�y�u �� �����t�{���u���|�u�~�y�u�}, �����|���x���r�p���u�|�����{�y�u ���y�{�|��
���q�����u�~�y�� �y �}�~���s���u �t�����s���u.

## �Q�u�{���}�u�~�t�p���y�y ���p���p�{���u���~���u �t�|�� TensorFlow 2.0

### �Q�u���p�{�����������u �r�p�� �{���t �r �}�u�~�����y�u �����~�{���y�y

�O�q�����~���z �����|���x���r�p���u�|�����{�y�z ���p�����u���~ �r TensorFlow 1.X �q���|�p �������p���u�s�y�� "kitchen
sink"(�{�������~�~�p�� �}���z�{�p), �s�t�u �����u�t�r�p���y���u�|���~�� �r���{�|�p�t���r�p�|������ ���q���u�t�y�~�u�~�y�u �r���u��
�r���x�}���w�~���� �r�����y���|�u�~�y�z, �p ���������} �r���q���p�~�~���u ���u�~�x������ �����u�~�y�r�p�|�y���� �� `session.run()`. �B
TensorFlow 2.0, �����|���x���r�p���u�|���} �~�u���q�����t�y�}�� �������u���p�{�������y���� ���r���z �{���t �r �}�u�~�����y�u
�����~�{���y�y �{�����������u �r���x���r�p�������� ���� �}�u���u �~�u���q�����t�y�}�������y. �B ���q���u�}, �~�u ���q���x�p���u�|���~��
�t�u�{�����y�����r�p���� �{�p�w�t���� �y�x �����y�� �����~�{���y�z �� `tf.function`; �y�������|���x���z���u `tf.function`
�����|���{�� �t�|�� �t�u�{�����y�����r�p�~�y�� �r�������{���������r�~�u�r���� �r�����y���|�u�~�y�z - �~�p�����y�}�u��, ���t�y�~ ���p�s
���q�����u�~�y�� �y�|�y �����������t �r���u���u�t �r �r�p���u�z �}���t�u�|�y.

### �I�������|���x���z���u ���|���y �y �}���t�u�|�y Keras �t�|�� �������p�r�|�u�~�y�� ���u���u�}�u�~�~���}�y


Keras models and layers offer the convenient `variables` and
`trainable_variables` properties, which recursively gather up all dependent
variables. This makes it easy to manage variables locally to where they are
being used.

�M���t�u�|�y �y ���|���y Keras �����u�t�|�p�s�p���� ���t���q�~���u ���r���z�����r�p `variables` �y
`trainable_variables`, �{�����������u ���u�{�������y�r�~�� �����q�y���p���� �r���u �x�p�r�y���y�}���u ���u���u�}�u�~�~���u. �^����
���q�|�u�s���p�u�� �|���{�p�|���~���u �������p�r�|�u�~�y�u ���u���u�}�u�~�~���}�y �r �����} �}�u�����u, �s�t�u ���~�y �y�������|���x���r�p�|�y����.

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

# �B�p�} �~�u���q�����t�y�}�� �������p�r�|������ w_i and b_i, �p �y�� ���p�x�}�u���~�������y �������u�t�u�|�u�~�� �t�p�|�u�{�� ���� �{���t�p.
```

�� �r�u�����y�u�z Keras:

```python
# �K�p�w�t���z ���|���z �}���w�u�� �q������ �r���x�r�p�~ �� ���y�s�~�p���������z ���{�r�y�r�p�|�u�~���~���z linear(x)
layers = [tf.keras.layers.Dense(hidden_size, activation=tf.nn.sigmoid) for _ in range(n)]
perceptron = tf.keras.Sequential(layers)

# layers[3].trainable_variables => returns [w3, b3]
# perceptron.trainable_variables => returns [w0, b0, ...]
```

�R�|���y/�}���t�u�|�y Keras �~�p���|�u�t���������� ���� `tf.train.Checkpointable` �y �y�~���u�s���y�����r�p�~��
�� `@ tf.function`, ������ �����x�r���|���u�� �~�p�������}���� �������r�u�������� �y�|�y ���{�����������y�����r�p����
SavedModels �y�x ���q���u�{�����r Keras. �B�p�} �~�u ���q���x�p���u�|���~�� �y�������|���x���r�p���� Keras
`.fit ()` API �������q�� �r���������|���x���r�p�������� �����y�}�y �y�~���u�s���p���y���}�y.

�B���� �����y�}�u�� transfer learning, �{�����������z �t�u�}���~�������y�����u��, �{�p�{ Keras ���q�|�u�s���p�u��
���q���� �����t�}�~���w�u�����r�p ���u�|�u�r�p�~���~���� ���u���u�}�u�~�~����. �D�����������y�}, �r�� ���q�����p�u���u multi-headed
model with a shared trunk:

```python
trunk = tf.keras.Sequential([...])
head1 = tf.keras.Sequential([...])
head2 = tf.keras.Sequential([...])

path1 = tf.keras.Sequential([trunk, head1])
path2 = tf.keras.Sequential([trunk, head2])

# �O�q�����u�~�y�u �~�p ���u���r�y���~���� �t�p�~�~����
for x, y in main_dataset:
  with tf.GradientTape() as tape:
    prediction = path1(x)
    loss = loss_fn_head1(prediction, y)
  # �O�t�~���r���u�}�u�~�~�p�� �������y�}�y�x�p���y�� �r�u�����r trunk �y head1.
  gradients = tape.gradient(loss, path1.trainable_variables)
  optimizer.apply_gradients(zip(gradients, path1.trainable_variables))

# �S���~�{�p�� �~�p���������z�{�p �r���������z head, ���u���u�y�������|���x���r�p�~�y�u trunk
for x, y in small_dataset:
  with tf.GradientTape() as tape:
    prediction = path2(x)
    loss = loss_fn_head2(prediction, y)
  # �O�����y�}�y�x�y������������ �����|���{�� �r�u���p head2, �~�u �r�u���p trunk
  gradients = tape.gradient(loss, head2.trainable_variables)
  optimizer.apply_gradients(zip(gradients, head2.trainable_variables))

# �B�� �}���w�u���u �������q�|�y�{���r�p���� �����|���{�� �r�����y���|�u�~�y�� trunk �������q�� �t�����s�y�u �|���t�y �}���s�|�y �y�}�y �r���������|���x���r�p��������.
tf.saved_model.save(trunk, output_path)
```

### �K���}�q�y�~�y�����z���u tf.data.Datasets �y @tf.function

�P���y �y���u���p���y�y ���� �����u�~�y�����r�����~���} �t�p�~�~���}, �{�����������u �����}�u���p�������� �r ���p�}������, ���r���q���t�~��
�y�������|���x���z���u ���u�s���|�����~���� �y���u���p���y�� Python. �I�~�p���u, `tf.data.Dataset` - �|�������y�z �����������q
�t�|�� ���u���u�t�p���y �����u�~�y�����r�����~���� �t�p�~�~���� �� �t�y���{�p. �D�p�~�~���u ���r�|����������
[iterables (�~�u iterators)](https://docs.python.org/3/glossary.html#term-iterable),
�y ���p�q�����p���� ���p�{ �w�u, �{�p�{ �y �t�����s�y�u Python iterables �r ���u�w�y�}�u Eager. �B�� �}���w�u���u
�����|�~���������� �y�������|���x���r�p���� ���r���z�����r�p dataset async prefetching/streaming �����p�{���r�p�r
���r���z �{���t �r `tf.function ()`, �{���������p�� �x�p�}�u�~���u�� �y���u���p���y�� Python ���{�r�y�r�p�|�u�~���~���}
�s���p�����} �����u���p���y�y �y�������|���x�������y�} AutoGraph.

```python
@tf.function
def train(model, dataset, optimizer):
  for x, y in dataset:
    with tf.GradientTape() as tape:
      prediction = model(x)
      loss = loss_fn(prediction, y)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

If you use the Keras `.fit()` API, you won't have to worry about dataset
iteration.

```python
model.compile(optimizer=optimizer, loss=loss_fn)
model.fit(dataset)
```

### �B���������|���x���z���u���� �����u�y�}�����u�����r�p�}�y AutoGraph �� Python control flow

AutoGraph �����u�t�������p�r�|���u�� �����������q �����u���q���p�x���r�p�~�y�� �x�p�r�y�������u�s�� ���� �t�p�~�~���� control flow
�r ���{�r�y�r�p�|�u�~�����z ���u�w�y�} �s���p���p, �~�p�����y�}�u�� `tf.cond` �y `tf.while_loop`.

�O�t�~�� ���q�����~���u �}�u������, �s�t�u �������r�|���u������ �x�p�r�y�������y�z ���� �t�p�~�~���� control flow �~�p�����t�y������
sequence models. `tf.keras.layers.RNN` ���q�����p���y�r�p�u�� �����u�z�{�� RNN, �����x�r���|���� �r�p�}
�����p���y���u���{�y �y�|�y �t�y�~�p�}�y���u���{�y ���p�x�r�u���~������ recurrence. �N�p�����y�}�u��, �r�� �}���w�u��
���u���u�������u�t�u�|�y���� �t�y�~�p�}�y���u���{���� ���p�x�r�u�����{�� ���|�u�t�������y�} ���q���p�x���}:

```python
class DynamicRNN(tf.keras.Model):

  def __init__(self, rnn_cell):
    super(DynamicRNN, self).__init__(self)
    self.cell = rnn_cell

  def call(self, input_data):
    # [batch, time, features] -> [time, batch, features]
    input_data = tf.transpose(input_data, [1, 0, 2])
    outputs = tf.TensorArray(tf.float32, input_data.shape[0])
    state = self.cell.zero_state(input_data.shape[1], dtype=tf.float32)
    for i in tf.range(input_data.shape[0]):
      output, state = self.cell(input_data[i], state)
      outputs = outputs.write(i, output)
    return tf.transpose(outputs.stack(), [1, 0, 2]), state
```

�D�|�� �q���|�u�u �����t�����q�~���s�� ���q�x�����p ���r���z�����r AutoGraph, ���}�������y
[�����{���r���t�����r��](./function.ipynb).

### tf.metrics �p�s�s���u�s�y�����u�� �t�p�~�~���u and tf.summary �r�u�t�u�� �y�� �|���s

�D�|�� �|���s�p summaries �y�������|���x���z���u `tf.summary. (Scalar | histogram | ...)` �y
���u���u�~�p�����p�r�����u �u�s�� �~�p writer �y�������|���x���� context manager. (�E���|�y �r�� �����������y���u context
manager, �~�y���u�s�� ���|�����y������.) �B �����|�y���y�u ���� TF 1.x, summaries ���������p�r�|����������
�~�u���������u�t�����r�u�~�~�� writer; ���p�} �~�u�� �����t�u�|���~���z �����u���p���y�y "merge" �y �����t�u�|���~���s�� �r���x���r�p
`add_summary()`, ������ ���x�~�p���p�u��, ������ �x�~�p���u�~�y�u `step` �t���|�w�~�� �q������ ���{�p�x�p�~�� �~�p �}�u�����u
�r���x���r�p.

```python
summary_writer = tf.summary.create_file_writer('/tmp/summaries')
with summary_writer.as_default():
  tf.summary.scalar('loss', 0.1, step=42)
```

�X�����q�� ���q���u�t�y�~�y���� �t�p�~�~���u ���u���u�t �y�� �x�p���y������ �r �r�y�t�u summaries, �y�������|���x���z���u
`tf.metrics`. �M�u�����y�{�p ���r�|���������� stateful: ���~�y �~�p�{�p���|�y�r�p���� �x�~�p���u�~�y�� �y �r���x�r���p���p����
�����r���{�����~���z ���u�x���|�����p��, �{���s�t�p �r�� �r���x���r�y���u `.result()`. �O���y�����y���u �~�p�{�����|�u�~�~���u
�x�~�p���u�~�y�� �� �����}�������� `.reset_states ()`.

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

�B�y�x���p�|�y�x�y�����z���u ���s�u�~�u���y�����r�p�~�~���u ���u�x���|�����p���� �~�p�����p�r�y�r TensorBoard �r �t�y���u�{�������y�z ��
summary log:

```
tensorboard --logdir /tmp/summaries
```
