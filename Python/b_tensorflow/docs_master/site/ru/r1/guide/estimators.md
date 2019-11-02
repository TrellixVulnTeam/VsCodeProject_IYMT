# Estimators

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

�B �������} �t���{���}�u�~���u �}�� �����x�~�p�{���}�y�}���� `tf.estimator`, �r�������{���������r�~�u�r���} API TensorFlow,
�{�����������z �x�~�p���y���u�|���~�� �����������p�u�� ���������u���� �����x�t�p�~�y�� �}���t�u�|�u�z �}�p���y�~�~���s�� ���q�����u�~�y��.
Estimators �r�{�|�����p�u�� �r ���u�q�� ���|�u�t�������y�u �����u���p���y�y:

*   ���q�����u�~�y�u
*   �����u�~�{��
*   �����u�t���{�p�x�p�~�y�u
*   ���{���������� �}���t�u�|�y �~�p ���u���r�u��

�S�� �}���w�u���� �y�������|���x���r�p���� �|�y�q�� ���w�u �s�������r���u Estimators �y�|�y �~�p���y���p���� ���r���y
�����q�����r�u�~�~���u �t�|�� �����u�~�{�y. �B���u Estimators �����~���r�p�~�� �~�p �{�|�p�����u `tf.estimator.Estimator`.

�D�|�� �q�����������s�� ���x�~�p�{���}�|�u�~�y�� �����������q���z �x�p���������y���� [�y�~���u���p�{���y�r�~���u �������{�y ���� Estimator](../tutorials/estimators/linear.ipynb)
�r Google Colab. �X�����q�� ���x�~�p���� �� �{�p�w�t���z �����~�{���y�y �����t�����q�~�u�u ���}�������y �����p������ [�s�������r���u Estimators](premade_estimators.md).
�D�|�� ���x�~�p�{���}�|�u�~�y�� �� �t�y�x�p�z�~���} �������s�� API ���}�������y �~�p�� [�t���{�|�p�t �~�p arxiv.org](https://arxiv.org/abs/1708.02637).

�O�q���p���y �r�~�y�}�p�~�y�u: TensorFlow ���p�{�w�u �r�{�|�����p�u�� �r ���u�q�� �������p���u�r���y�z �{�|�p����
`Estimator` �r `tf.contrib.learn.Estimator`, �{�����������z �y�������|���x���r�p���� �~�u �������y��.


## �P���u�y�}�����u�����r�p Estimators

Estimators ���q�u�����u���y�r�p���� ���|�u�t�������y�u �����u�y�}�����u�����r�p:

*   �M���w�~�� �x�p�������{�p���� �}���t�u�|�y �~�p �����~���r�u Estimators �|���{�p�|���~�� �y�|�y �~�p ���p�������u�t�u�|�u�~�~���}
    ���u���r�u���u �q�u�x �y�x�}�u�~�u�~�y�z ���������{�������� �}���t�u�|�y. �A���|�u�u �����s��, ���� �}���w�u���� �x�p�������{�p���� �}���t�u�|�y
    �~�p CPU, GPU �y TPU �q�u�x �r�~�u���u�~�y�� �y�x�}�u�~�u�~�y�z �r �{���t
*   �R �����}�������� Estimators ���t���q�~�u�u �t�u�|�y�������� ���r���y�}�y �}���t�u�|���}�y �� �t�����s�y�}�y ���p�x���p�q�������y�{�p�}�y
*   �M���w�~�� ���p�x���p�q�p�����r�p���� �����r���u�}�u�~�~���u �}���t�u�|�y �� ���y���p�u�}���} �r�������{���������r�~�u�r���} �{���t���}. �P�������u �s���r������,
    �s�����p�x�t�� �|�u�s���u �����x�t�p�r�p���� �}���t�u�|�y �� Estimators, ���u�} �� �~�y�x�{���������r�~�u�r���} API TensorFlow
*   �R�p�}�y Estimators �������������u�~�� �~�p `tf.keras.layers`, �{�����������u �����������p���� �~�p���������z�{�� �}���t�u�|�y
    �����t ���u�q��
*   Estimators ������������ �s���p��
*   Estimators ���q�u�����u���y�r�p���� �������������z ���p�������u�t�u�|�u�~�~���z ���y�{�| ���q�����u�~�y��, �{�����������z �{���~�������|�y�����u��
    �{�p�{ �y �{���s�t�p:

    *   ���������y���� �s���p��
    *   �y�~�y���y�p�|�y�x�y�����r�p���� ���u���u�}�u�~�~���u
    *   �x�p�s�����w�p���� �t�p�~�~���u
    *   ���q���p�q�p�����r�p���� �y���{�|�����u�~�y��
    *   �����x�t�p�r�p���� �{���~�������|���~���u �������{�y �y �r���������p�~�p�r�|�y�r�p�������� �����y �~�u���t�p���~���� �����������{�p��
    *   ���������p�~������ �����p���y�����y�{�� �r TensorBoard

�P���y �~�p���y���p�~�y�y �����y�|���w�u�~�y�� �� Estimators ���� �t���|�w�u�~ �����t�u�|������ �x�p�s�����x�{�� �r�����t�~���� �t�p�~�~����
���� ���p�}���z �}���t�u�|�y. �^���� ���p�x�t�u�|�u�~�y�u �����������p�u�� ���{�����u���y�}�u�~���� �� ���p�x�~���}�y �~�p�q�����p�}�y �t�p�~�~����.


## �C�������r���u Estimators

�C�������r���u Estimators �����x�r���|������ ���u�q�u ���p�q�����p���� �~�p �q���|�u�u �r�������{���} �������r�~�u, ���� �����p�r�~�u�~�y��
�� �q�p�x���r���} API TensorFlow. �S�u�q�u �q���|�����u �~�u �~���w�~�� �r���|�~���r�p�������� �� �������������u�~�y�y �r�����y���|�y���u�|���~���s��
�s���p���p �y�|�y ���u�����y���� ���q�����u�~�y��, �������{���|���{�� Estimators ���p�}�y �t�u�|�p���� �x�p ���u�q�� �r���� ���p�q������.
�S�p�{�y�} ���q���p�x���} Estimators ���p�}�y �����x�t�p���� �y �������p�r�|������ ���q���u�{���p�}�y `tf.Graph` �y 
`tf.Session`. �A���|�u�u �����s��, �s�������r���u Estimators �����x�r���|������ ���u�q�u ���{�����u���y�}�u�~���y�����r�p���� �� 
���p�x�~���}�y �p�����y���u�{�������p�}�y �� �}�y�~�y�}�p�|���~���}�y �y�x�}�u�~�u�~�y���}�y �y�������t�~���s�� �{���t�p. �N�p�����y�}�u��,
`tf.estimator.DNNClassifier` - ������ �s�������r���z �{�|�p���� Estimator, �{�����������z ���q�����p�u��
�{�|�p�����y���y�{�p���y�y �}���t�u�|�y �~�p �����~���r�u �~�u�z�����~�~���z ���u���y �������}���s�� ���p���������������p�~�u�~�y��, �{���������p�� 
�����������y�� �y�x *Dense* ���|���u�r.


### �R�������{�������p �������s���p�}�} �� �s�������r���}�y Estimators

�P�����s���p�}�}�p TensorFlow �~�p �����~���r�u �s�������r���� Estimators ���q�����~�� �����������y�� �y�x ���|�u�t�������y��
���u�������u�� ���p�s���r:

1.  **�N�p���y���p�~�y�u ���t�~���z �y�|�y �q���|�u�u �����~�{���y�z �t�|�� �x�p�s�����x�{�y �t�p���p���u���p**. �N�p�����y�}�u��,
    �����x�t�p�t�y�} �����~�{���y�� �t�|�� �y�}���������p �����u�~�y�����r�����~���s�� ���u���p �y �r���������� �����~�{���y�� �t�|��
    �y�}���������p �������r�u�������~���s�� ���u���p �t�p�~�~����. �K�p�w�t�p�� �����~�{���y�� �t�|�� �x�p�s�����x�{�y �t�p���p���u���p
    �t���|�w�~�p �r���x�r���p���p���� �t�r�p ���q���u�{���p:

    *   ���|���r�p����, �r �{�����������} �{�|�����y ���r�|���������� �y�}�u�~�p�}�y ���p���p�}�u�������r, �p �x�~�p���u�~�y��
        ���r�|���������� ���u�~�x�����p�}�y (�y�|�y *SparseTensors*), �����t�u���w�p���y�u ���������r�u�������r�������y�u
        �t�p�~�~���u ���p���p�}�u�������r
    *   ���u�~�x����, �����t�u���w�p���y�z ���t�~�� �y�|�y �q���|�u�u �}�u�����{

    �N�p�����y�}�u��, �r �{���t�u �~�y�w�u �����{�p�x�p�~ �����y�}�u�� �����~���r�~���s�� ���{�u�|�u���p �t�|�� �����~�{���y�y �r�r���t�p
    �t�p�~�~����:

```python
        def input_fn(dataset):
           ...  # �}�p�~�y�����|�y�����u�� �t�p���p���u�����}, �y�x�r�|�u�{�p�� ���|���r�p���� ���p���p�}�u�������r �y �}�u���{�y
           return feature_dict, label
```

�R�}�������y �����t�����q�~�u�u �r �����p�����u [�H�p�s�����x�{�p �t�p�~�~���� �y �t�p���p���u�����r](../guide/datasets.md)

2.  **�O�����u�t�u�|�u�~�y�u �{���|���~���{ ���p���p�}�u�������r.** �K�p�w�t�p�� �{���|���~�{�p `tf.feature_column`
    �������u�t�u�|���u�� �y�}�� ���p���p�}�u�����p, �u�s�� ���y�� �y �|���q���� �����u�t�r�p���y���u�|���~���� ���q���p�q�����{��
    �r�����t�~���� �t�p�~�~����. �N�p�����y�}�u��, �r ���|�u�t�������u�} �����y�}�u���u �{���t�p �}�� �����x�t�p�t�y�} �����y
    �{���|���~�{�y ���p���p�}�u�������r, �r �{������������ �q���t���� �����p�~�y�������� �t�p�~�~���u �r �������}�p���u ���u�|����
    ���y���u�| �y�|�y ���y���u�| �� ���|�p�r�p�����u�z �x�p���������z. �P�u���r���u �t�r�u �{���|���~�{�y ���p���p�}�u�������r �q���t����
    ������������ �y�t�u�~���y���y���y�����r�p���� �y�}�� �y ���y�� ���p���p�}�u�����p. �S���u������ �{���|���~�{�p ���p���p�}�u�������r ���{�p�x���r�p�u��
    �~�p �|���}�q�t��-�r�����p�w�u�~�y�u, �{�����������u �q���t���� �r���x���r�p�������� �t�|�� �����u�~�{�y �~�u���q���p�q�����p�~�~����
    �t�p�~�~����:

```python
# �O�����u�t�u�|�y�} �����y ���y���|���r���� �{���|���~�{�y ���p���p�}�u�������r.
population = tf.feature_column.numeric_column('population')
crime_rate = tf.feature_column.numeric_column('crime_rate')
median_education = tf.feature_column.numeric_column('median_education',
                       normalizer_fn=lambda x: x - global_education_mean)
```

3.  **�T�{�p�w�u�} �����t�����t�����y�z �s�������r���z Estimator.**  �N�p�����y�}�u�� ���p�{ �}�� ���{�p�w�u�}
    �s�������r���z Estimator �t�|�� ���u���u�~�y�� �}���t�u�|�y `�|�y�~�u�z�~���s�� �{�|�p�����y���y�{�p�������p`:

```python
# �T�{�p�x���r�p�u�} estimator, ���u���u�t�p�u�} �{���|���~�{�y ���p���p�}�u�������r.
estimator = tf.estimator.LinearClassifier(
    feature_columns=[population, crime_rate, median_education],
)
```

4.  **�B���x���r �}�u�����t�p ���q�����u�~�y��, �����u�~�{�y �y�|�y �����u�t���{�p�x�p�~�y��**
    �N�p�����y�}�u��, �r���u Estimators �y�}�u���� �}�u�����t `train` �t�|�� �~�p���p�|�p ���q�����u�~�y�� �}���t�u�|�y:

```python
# `input_fn` - �����~�{���y��, �����x�t�p�~�~�p�� �r ���p�}���} ���u���r���} ���p�s�u
estimator.train(input_fn=my_training_set, steps=2000)
```

### �P���u�y�}�����u�����r�p �y�������|���x���r�p�~�y�� �s�������r���� Estimators

�B �s�������r���� Estimators �y�������|���x���������� �|�������y�u �����p�{���y�{�y, �{�����������u ���q�u�����u���y�r�p����
���|�u�t�������y�u �����u�y�}�����u�����r�p:

*   �L�������y�u �����p�{���y�{�y �t�|�� �������u�t�u�|�u�~�y�� �{�p�{�y�u ���p�����y �r�����y���|�y���u�|���~���s�� �s���p���p
    �x�p�������{�p���� ���~�p���p�|�p, �p ���p�{�w�u �������p���u�s�y�y �t�|�� ���q�����u�~�y�� �~�p ���t�~���} �����������z�����r�u
    �y�|�y ���u�|���} �{�|�p�����u���u
*   �R���p�~�t�p�����y�x�y�����r�p�~�~�p�� �����p�{���y�{�p �r�u�t�u�~�y�� �|���s���r �y �����|�����u�~�y�� �����|�u�x�~���z �����p���y�����y�{�y

�E���|�y ���� �~�u �����q�y���p�u�������� �y�������|���x���r�p���� �s�������r���u Estimators, ���� �����s�t�p ���u�q�u
�����y�t�u������ ���{�p�x���r�p���� �r���u �~�u���q�����t�y�}���u ���p���p�}�u������ ���p�}���}��.


## �R���q�����r�u�~�~���u Estimators

�`�t�����} �{�p�w�t���s�� Estimator, �s�������r���s�� �y�|�y �~�p���y���p�~�~���s�� �� �~���|��, ���r�|���u������
**�����~�{���y�� �}���t�u�|�y**, �{���������p�� �����u�t�����p�r�|���u�� �y�x ���u�q�� �}�u�����t �t�|�� �������������u�~�y��
�s���p���p �t�|�� ���q�����u�~�y��, �����u�~�{�y �y �����u�t���{�p�x�p�~�y�z. �K���s�t�p ���� �y�������|���x���u���� �s�������r���z
Estimator, �{����-���� ���w�u �~�p���y���p�| �����~�{���y�� �}���t�u�|�y �t�|�� ���u�q��. �B �����} ���|�����p�u,
�{���s�t�p ���� �����|�p�s�p�u�������� �~�p ���r���z �����q�����r�u�~�~���z Estimator, ���� �t���|�w�u�~ ���p�}
�~�p���y���p���� ������ �����~�{���y��. �A���|�u�u �����t�����q�~�� �� �����}, �{�p�{ �~�p���y���p���� �����~�{���y�� �}���t�u�|�y
���� �}���w�u���� ���x�~�p���� �r �����p�����u [�N�p���y���p�~�y�u �����q�����r�u�~�~���� Estimators](../guide/custom_estimators.md)


## �Q�u�{���}�u�~�t���u�}���z �����t ���p�q������

�M�� ���u�{���}�u�~�t���u�} ���|�u�t�������y�z ���������t���{ �����x�t�p�~�y�� �}���t�u�|�y �� �����}�������� Estimators:

1.  �P���u�t�����|���w�y�}, ������ �u������ �s�������r���z Estimator, �y �}�� �y�������|���x���u�} �u�s�� �t�|��
    �������������u�~�y�� �~�p���u�z �}���t�u�|�y, �p ���p�{�w�u �y�������|���x���u�} ���u�x���|�����p���� �����u�~�{�y �t�|�� 
    �������}�y�����r�p�~�y�� �����p�|���~�~���z �}���t�u�|�y
2.  �R���x�t�p�u�} �y ���u�����y�����u�} ���������u���� �x�p�s�����x�{�y �t�p�~�~����, �������r�u�����u�} ���u�|�������~�������� �y
    �~�p�t�u�w�~�������� �~�p���y�� �t�p�~�~���� �� �s�������r���} Estimator
3.  �E���|�y �u������ �t�����s�y�u �����t�����t�����y�u �p�|�����u���~�p���y�r��, �����s�t�p ���{�����u���y�}�u�~���y�����u�} �� �~�y�}�y
    �t�|�� �����y���{�p Estimator, �{�����������z �����{�p�w�u�� �|�������y�u ���u�x���|�����p����
4.  �B���x�}���w�~�� ���������u�q���u������ ���|�������y���� �~�p���� �}���t�u�|�� �����y �����}�����y �����x�t�p�~�y�� �~�p���u�s��
    �����q�����r�u�~�~���s�� Estimator.


## �R���x�t�p�~�y�u Estimators �y�x �}���t�u�|�u�z Keras 

�S�� �}���w�u���� �{���~�r�u�����y�����r�p���� ���w�u �y�}�u�����y�u���� �� ���u�q�� �}���t�u�|�y Keras �r Estimators. �^���� �����x�r���|�y��
���u�q�u �y�������|���x���r�p���� �r���u �����u�y�}�����u�����r�p Estimators �t�|�� �t�p�~�~���z �}���t�u�|�y, �~�p�����y�}�u��, �t�|�� ���p�������u�t�u�|�u�~�~���s��
���q�����u�~�y��. �B���x���r�y �����~�{���y�� `tf.keras.estimator.model_to_estimator` �{�p�{ �r �����y�}�u���u �~�y�w�u:

```python
# �R���x�t�p�u�} �}���t�u�|�� Inception v3 �r Keras:
keras_inception_v3 = tf.keras.applications.inception_v3.InceptionV3(weights=None)

# �K���}���y�|�y�����u�} �}���t�u�|�� �� �������y�}�y�x�p���������}, �����~�{���y�u�z �������u���� �y �}�u�����y�{�p�}�y ���q�����u�~�y�� ���� �r���q������.
keras_inception_v3.compile(optimizer=tf.keras.optimizers.SGD(lr=0.0001, momentum=0.9),
                          loss='categorical_crossentropy',
                          metric='accuracy')

# �R���x�t�p�u�} Estimator �y�x ���{���}���y�|�y�����r�p�~�~���z �}���t�u�|�y Keras. �O�q���p���y �r�~�y�}�p�~�y�u, ������ �y�x�~�p���p�|���~���u
# �������������~�y�u �}���t�u�|�y Keras ���������p�~���u������ �����y �����x�t�p�~�y�y Estimator.
est_inception_v3 = tf.keras.estimator.model_to_estimator(keras_model=keras_inception_v3)

# �S�u���u���� �}�� �}���w�u�} �y�������|���x���r�p���� �����|�����u�~�~���z Estimator �{�p�{ �|���q���z �t�����s���z.
# �D�|�� �~�p���p�|�p �r���������p�~���r�y�} �r�r���t�~���u �y�}�� (�y�|�y �y�}�u�~�p) �}���t�u�|�y Keras, �������q�� �}�� �}���s�|�y �y�������|���x���r�p���� �y��
# �{�p�{ �y�}�u�~�p �{���|���~���{ ���p���p�}�u�������r �����~�{���y�y �r�r���t�p �t�p�~�~���� Estimator:
keras_inception_v3.input_names  # �r���r���t�y��: ['input_1']

# �K�p�{ �����|���{�� �}�� �����|�����y�} �r�r���t�~���u �y�}�u�~�p, �}�� �}���w�u�} �����x�t�p���� �����~�{���y�� �r�r���t�p �t�p�~�~����, �~�p�����y�}�u��,
# �t�|�� �r�����t�p �t�p�~�~���� �r �������}�p���u NumPy ndarray:
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"input_1": train_data},
    y=train_labels,
    num_epochs=1,
    shuffle=False)

# �D�|�� ���q�����u�~�y�� �r���x���r�p�u�} �����~�{���y�� `train` �����|�����u�~�~���s�� �~�p�}�y Estimator:
est_inception_v3.train(input_fn=train_input_fn, steps=2000)
```

�O�q���p���y �r�~�y�}�p�~�y�u, ������ �y�}�u�~�p �{���|���~���{ ���p���p�}�u�������r �y �}�u�����{ Esitmator �}�� �����|�����y�|�y
�y�x ���������r�u�������r�������u�z �}���t�u�|�y Keras. �N�p�����y�}�u��, �y�}�u�~�p �r�r���t�~���� �{�|�����u�z �t�|�� `train_input_fn`
�r�����u �}���s���� �q������ �����|�����u�~�� �y�x `keras_inception_v3.input_names`, �y ���p�{�y�} �w�u ���q���p�x���}
�����u�t���{�p�x�p�~�~���u �y�}�u�~�p �}���s���� �q������ �����|�����u�~�� �y�x `keras_inception_v3.output_names`.

�P���t�����q�~�u�u ���}�������y �t���{���}�u�~���p���y�� �r �����p�����u `tf.keras.estimator.model_to_estimator`.
