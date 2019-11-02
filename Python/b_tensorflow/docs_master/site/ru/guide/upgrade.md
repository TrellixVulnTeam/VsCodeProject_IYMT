# �O�q�~���r�y���u �{���t �t�� TensorFlow 2.0

TensorFlow 2.0 �r�{�|�����p�u�� �}�~���s�� �y�x�}�u�~�u�~�y�z API, ���p�{�y�� �{�p�{ �y�x�}�u�~�u�~�y�u ���������t�{�p
�p���s���}�u�~�����r, ���u���u�y�}�u�~���r�p�~�y�u ���y�}�r���|���r �y �y�x�}�u�~�u�~�y�u �x�~�p���u�~�y�z ���� ���}���|���p�~�y��
���p���p�}�u�������r. �B�������|�~�u�~�y�u �����y�� �}���t�y���y�{�p���y�z �r�������~���� �������}�y���u�|���~�� �y �����t�r�u���w�u�~��
�����y�q�{�p�}. �D�|�� �����������u�~�y�� �y�x�}�u�~�u�~�y�z �y �{�p�{ �}���w�~�� �q���|�u�u ���|�p�r�~���s�� ���u���u�����t�p �~�p TF 2.0,
�{���}�p�~�t�p TensorFlow �����x�t�p�|�p �����y�|�y���� `tf_upgrade_v2`, �����}���s�p�������� ���u���u�z���y ����
�������p���u�r���u�s�� �{���t�p �{ �~���r���}�� API.

�T���y�|�y���p `tf_upgrade_v2` �t���q�p�r�|���u������ �p�r�����}�p���y���u���{�y �� `pip install` TF 2.0. �O�~�p
�����{�����y�� ���������u���� ���q�~���r�|�u�~�y�� �x�p �����u�� �����u���q���p�x���r�p�~�y�� �������u�����r�������y�� ���{���y�������r
TensorFlow 1.x Python �r TensorFlow 2.0.

�R�{���y���� ���q�~���r�|�u�~�y�� �p�r�����}�p���y�x�y�����u�� �}�p�{���y�}���} �r���x�}���w�~���s��, �~�� �r���u �u���u �u������
���y�~���p�{���y���u���{�y�u �y �����y�|�y�����y���u���{�y�u �y�x�}�u�~�u�~�y��, �{�����������u �~�u �}���s���� �q������ �r�������|�~�u�~��
���{���y�������}.

## �M���t���|�� �����r�}�u�����y�}�������y

�N�u�{�����������u ���y�}�r���|�� API �~�u �}���s���� �q������ ���q�~���r�|�u�~�� ������������ �� �����}�������� �x�p�}�u�~�� ���������{�y.
�X�����q�� �s�p���p�~���y�����r�p���� �����t�t�u���w�{�� �r�p���u�s�� �{���t�p �r TensorFlow 2.0, ���{���y���� ���q�~���r�|�u�~�y��
�r�{�|�����p�u�� �r ���u�q�� �}���t���|�� `compat.v1`. �^������ �}���t���|�� �x�p�}�u�~���u�� TF 1.x ���y�}�r���|��
�~�p�����t���q�y�u `tf.foo` �y�� ���{�r�y�r�p�|�u�~���p�}�y `tf.compat.v1.foo`. �V������ �}���t���|��
�����r�}�u�����y�}�������y ����������, �}�� ���u�{���}�u�~�t���u�} �r�p�} �r�������~���� �r�����y���p���� �x�p�}�u�~�� �y ���u���u�~�u�����y �y��
�~�p �~���r���u API �r �������������p�~�����r�u �y�}�u�~ `tf. *` �r�}�u������ �������������p�~�����r�p �y�}�u�~ `tf.compat.v1.
*`.

�I�x-�x�p �������p���u�r�p�~�y�� �}���t���|�u�z TensorFlow 2.x (�~�p�����y�}�u��, `tf.flags` �y`tf.contrib`)
�~�u�{�����������u �y�x�}�u�~�u�~�y�� �~�u �}���s���� �q������ �������p�q�����p�~�� �������u�} ���u���u�{�|�����u�~�y�� �~�p `compat.v1`.
�O�q�~���r�|�u�~�y�u �������s�� �{���t�p �}���w�u�� ���������u�q���r�p���� �y�������|���x���r�p�~�y�� �t�������|�~�y���u�|���~���z �q�y�q�|�y�����u�{�y
(�~�p�����y�}�u��, ��absl.flags��) �y�|�y ���u���u�{�|�����u�~�y�� �~�p ���p�{�u�� �r
[tenorflow / addons](http://www.github.com/tensorflow/addons).

## �R�{���y���� ���q�~���r�|�u�~�y��

�X�����q�� �{���~�r�u�����y�����r�p���� �r�p�� �{���t �y�x TensorFlow 1.x �r TensorFlow 2.x, ���|�u�t���z���u
���|�u�t�������y�} �y�~���������{���y���}:

### �H�p���������y���u ���{���y���� �y�x ���p�{�u���p pip

�R���u���r�p �� `pip install` �������p�~���r�y���u ���p�{�u�� `tensorflow==2.0.0-beta0` �y�|�y
`tensorflow-gpu==2.0.0-beta0`.

�P���y�}�u���p�~�y�u: `tf_upgrade_v2` �������p�~�p�r�|�y�r�p�u������ �p�r�����}�p���y���u���{�y �t�|�� TensorFlow 1.13 �y
�r�����u (�r�{�|�����p�� �~�����~���u ���q�����{�y TF 2.0).

�R�{���y���� ���q�~���r�|�u�~�y�� �}���w�u�� �q������ �x�p�������u�~ �~�p ���t�~���} ���p�z�|�u Python:

```sh
tf_upgrade_v2 --infile tensorfoo.py --outfile tensorfoo-upgraded.py
```

�R�{���y���� �r���r�u�t�u�� �����y�q�{�y �u���|�y ���~ �~�u ���}���w�u�� �~�p�z���y �y�������p�r�|�u�~�y�u �t�|�� �{���t�p. �B�� ���p�{�w�u
�}���w�u���u �x�p���������y���� �u�s�� �~�p �t�u���u�r�u �{�p���p�|���s���r:

```
# ���q�~���r�y���u ���p�z�|�� .py �y ���{�����y�����z���u �r���u �������p�|���~���u ���p�z�|�� �r outtree
tf_upgrade_v2 --intree coolcode --outtree coolcode-upgraded

# ���q�~���r�|�u�~�y�u �����|���{�� .py ���p�z�|���r
tf_upgrade_v2 --intree coolcode --outtree coolcode-upgraded --copyotherfiles False
```

## �D�u���p�|���~���z �������u��

�R�{���y���� ���p�{�w�u �������q���p�u�� �����y�����{ �t�u���p�|���~���� �y�x�}�u�~�u�~�y�z, �~�p�����y�}�u��:

```
'tensorflow/tools/compatibility/testdata/test_file_v1_12.py' Line 65
--------------------------------------------------------------------------------

Added keyword 'input' to reordered function 'tf.argmax'
Renamed keyword argument from 'dimension' to 'axis'

    Old:         tf.argmax([[1, 3, 2]], dimension=0))
                                        ~~~~~~~~~~
    New:         tf.argmax(input=[[1, 3, 2]], axis=0))

```

�B���� �����p �y�~�������}�p���y�� �t���q�p�r�|���u������ �r ���p�z�|`report.txt`, �{�����������z �q���t�u�� ���{�����������y�����r�p�~ �r
�r�p���� ���u�{�������� ���p���{��. �P�����|�u �r�������|�~�u�~�y�� `tf_upgrade_v2` �y ���{�����������p �r�p���u�s��
���q�~���r�|�u�~�~���s�� ���{���y�����p, �r�� �}���w�u���u �x�p���������y���� �}���t�u�|�� �y ���q�u�t�y��������, ������ ���u�x���|�����p��
�p�~�p�|���s�y���u�~ TF 1.x.

## �P���u�t�������u���u�w�u�~�y��

-   �N�u ���q�~���r�|���z���u ���p�����y �r�p���u�s�� �{���t�p �r�������~���� �t�� �x�p�������{�p �������s�� ���{���y�����p. �B
    ���p�����~�������y, �����~�{���y�y, �����}�u�~���r���y�u ���������t���{ �p���s���}�u�~�����r, ���p�{�y�u �{�p�{ `tf.argmax` �y�|�y
    `tf.batch_to_space` �r���~���t���� ���{���y���� �~�u�����p�r�y�|���~�� �t���q�p�r�y���� �y�}�u�~�p �p���s���}�u�~�����r,
    ������ �����y�r�u�t�u�� �{ �����y�q�{�p�} �r �������u�����r�������u�} �{���t�u.

-   �R�{���y���� �����u�t�����|�p�s�p�u�� ������ `tensorflow` �y�}���������y�����r�p�~ �� �y�������|���x���r�p�~�y�u�} `import
    tensorflow as tf`.

-   �^������ ���{���y���� �~�u �}�u�~���u�� �p���s���}�u�~����. �B�}�u������ �������s�� ���{���y���� �t���q�p�r�|���u�� �{�|�����y
    �p���s���}�u�~�����r �{ �����~�{���y���}, �� �{������������ �y�x�}�u�~�y������ ���������t���{ �p���s���}�u�~�����r.

-   �P�����r�u�������u [tf2up.ml](http://tf2up.ml) �t�|�� ���t���q�~���s�� �y�~���������}�u�~���p ���q�~���r�|�u�~�y��
    ���p�z�|���r �r �������}�p���p�� Jupyter Notebook �y Python �r ���u�����x�y�������y�y GitHub.

�X�����q�� �������q���y���� ���q �����y�q�{�p�� �r ���{���y�����u ���q�~���r�|�u�~�y�� �y�|�y ���������p�r�y���� �x�p�������� �~�p
�t���q�p�r�|�u�~�y�u �~���r���� �����~�{���y�z, ���������p�r�����u �������q���u�~�y�u ���q �����y�q�{�u �~�p
[GitHub](https://github.com/tensorflow/tensorflow/issues). �I �u���|�y �r�� ���u�����y�����u���u
TensorFlow 2.0, �}�� �������y�} �����|�����p���� ���q �������}! �P���y�����u�t�y�~���z���u���� �{ �������q���u�����r��
[TF 2.0 Testing](https://groups.google.com/a/tensorflow.org/forum/#!forum/testing)
�y ���������p�r�|���z���u �r������������ �y ���q�����w�t�u�~�y�� �~�p ���p�z��
[testing@tensorflow.org](mailto:testing@tensorflow.org).
