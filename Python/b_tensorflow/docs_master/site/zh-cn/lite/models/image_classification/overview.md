# ����

<img src="../images/image.png" class="attempt-right">

�g�p���I�͌^����S�ہC��l�A���A���A�A���a�n�_�B

## �n

�@�ʑ����I�T�O�s�n���C�� <a href="#what_is_image_classification">�Y�������H</a>

���@���݈ڗp���g�p�����C��䦊ŉ�񋟓I <a href="#example_applications_and_guides">����p�a�w</a>�B

�@�ʎg�p Android �a iOS �V�O�I����C���қߏn���� TensorFlow Lite �ڌ��C�Ȓ��ډ���I�V�葜���͌^�y�����I�B

<a class="button button-primary" href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip">���V�葜���y</a>

���V��͌^�ݓI�ڍs�N���V�@�C�ȑ����͌^�C�ݐ��\�A�y���ȋy�͌^�̝Q���ŉ��I���t�_�B <a href="#choose_a_different_model">�s���͌^</a>�B

### ����p�a�w

��� Android �a iOS �����s�L�����I����p�C��𗹛��I�H�쌴���B

#### Android

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android">��Android����</a>

 [Android example guide](android.md) �ȗ���p�H�쌴���B

#### iOS

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/ios.md">��iOS����</a>

 [iOS example guide](ios.md) �ȗ���p�H�쌴���B

#### �B��

���ʓI�B�� Android ��������p�B

<img src="images/android_banana.png" alt="Screenshot of Android example" width="30%">

## �Y�������H

����w�I�꘢��p�����B��@�C��\�z�v�m�������o�����B

<img src="images/dog.png" alt="dog" width="50%">

���I�C��� _����_ �B�����͌^�I�ړI���e���B��@�C�꘢�͌^�\��p���O���I�����F�\�q�A�l�a��B

����񋟈�V�I�Ж͌^�C����o�ЊܗL�O���I�T���B�ȉ����꘢�o����F

<table style="width: 40%;">
  <thead>
    <tr>
      <th>��</th>
      <th>�T��</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>�\�q</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>�l</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td style="background-color: #fcb66d;">��</td>
      <td style="background-color: #fcb66d;">0.91</td>
    </tr>
  </tbody>
</table>

��o�C��\�œ����͌^�o�C�ЗL�k��T���\���I�������B

���ӁF�������\���З��o�I�y���T���C�󊎑��\����I�B���s�\���З��ۓI�ʒu���Җ��́B
�@�ʎ��v�З��ۓI���̋y�ʒu�C�g�p <a href="../object_detection/overview.md">����</a> �͌^�B

### �A�a���f

�ݒ��C�p���a���I __ ���꘢�����͌^�B�����꘢�T�O���I�����B���͌^�A�v�w����B

�\�����I�����i�ʏ�꘢���ȕS�I�Ёj�C�������͌^�A�\�w���V�I�А��ۑ����������I�^���B���I����� _���f_ �B

���s���f�C��Д���͌^���B�ڒ��C�͌^���o�����\�T���I���C���f�召� 0 �a 1 �V�B����I����͌^�C�����\�@�������F

<table style="width: 60%">
  <tr style="border-top: 0px;">
    <td style="width: 40%"><img src="images/dog.png" alt="dog"></td>
    <td style="width: 20%; font-size: 2em; vertical-align: middle; text-align: center;">��</td>
    <td style="width: 40%; vertical-align: middle; text-align: center;">[0.07, 0.02, 0.91]</td>
</table>

�o���I�������s�������I�꘢�B����I�o�a�O���C��\�ŏo�C���͌^���В��I�ۗL�k��T���������B

<table style="width: 40%;">
  <thead>
    <tr>
      <th></th>
      <th>�T��</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>�\�q</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>�l</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td style="background-color: #fcb66d;">��</td>
      <td style="background-color: #fcb66d;">0.91</td>
    </tr>
  </tbody>
</table>

�\���ӓ����T���I�a�i�\�q�C�l�a��I�T���j�� 1�B�������͌^�I��o�B�i�F<a href="https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax">Softmax</a>�j

### �͌Еs���I��

���R�T���I�a������ 1�C�ߔ@�ʕЖv�L��͌^�o���C��A���s������I�C�\��I�{���s�v�L����I�T���B

��@�C���\�\�\�����꘢�͌Еs���I�ʁF

<table style="width: 40%;">
  <thead>
    <tr>
      <th></th>
      <th>�T��</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>�\�q</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>�l</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>��</td>
      <td>0.34</td>
    </tr>
  </tbody>
</table>

### �g�p�a����

��񋟓I���`���͌^���k�L�p�B�����w���ŗL�\�\���I�^�꘢�B���͌^��p�� 1000 ���B�����I��\�F<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip">�͌^��</a>

�@�ʑz�v�͌^�V�I�F<a href="#customize_model">����͌^</a>.

�ȉ��g�p�ė�C�їp�s���I�͌^�F

<ul>
  <li>�З��I�꘢�������ۓI�a�ʒu�i�F<a href="../object_detection/overview.md">����</a>�j</li>
  <li>���I���C��@��̗^�w�i�i�F<a href="../segmentation/overview.md">����</a>�j</li>
</ul>


���V��͌^�ݓI�ڍs�N���V�@�C�ȑ����͌^�C�ݐ��\�A�y���ȋy�͌^�̝Q���ŉ��I���t�_�B�F<a href="#choose_a_different_model">�s���͌^</a>�B

## �s���͌^

��I <a href="../../guide/hosted_models.md">�͌^��\</a> ���L�������͌^���B
�ݛ��I���\�A�y���a�͌^�̔V�s�t�C�ȗ��œI�͌^�B

### ���\

�䍪���ݓ��I�d���������C�꘢�͌^�s���f���ԓI���t�ʐ��\�B�z�Z�C�͌^�z���B

���v�I���\��r���I�p�B�p���C���\�\���d�v�B�����v�݉��ꐧ���V�O�y���͈�i��@�F���f�p�K���� 33 ms �˔\���f 30 fps �I���j�B

��ʉ��IMobileNet �͌^�I���\� 3.7 ms �� 80.3 ms�B

### �y��

�䍪���͌^�������I�����t�ʏy�x�B��@�C�꘢�y�� 60% �I�͌^���ϗL 60% �I�\������ЁB

��I <a href="../../guide/hosted_models.md">�͌^��\</a> �� Top-1 �a Top-5 �y�������BTop-1 ���w�͌^�o���I�T���ō��I���BTop-5 ���w�͌^�o���I�T���ݑO�ܓI���B

��ʉ��I MobileNet �͌^�I�y��� 64.4% �� 89.9%�B

### ��

����͌^�I�̈������\�a�y�����B�̉\�ځi�\�e�p�I���́j���ҍd���i�p���\���L���I�j�k�d�v�B

��ʉ��I MobileNet �͌^�I�y��� 0.5 Mb �� 3.4 Mb�B

### �͌^

<a href="../../guide/hosted_models.md">�͌^��\</a> ���I�͌^�L�s���I�C���͌^���Ȋŏo�C��@�C�� MobileNet�AInception ���ґ����I�B

�͌^�I�e���I���\�A�y���a�́B��񋟓I�͌^�s���p���I�����I�C�Ӗ����Ȓʉ�񋟓I�����䍱�͌^�C���ō��I�p�I�B

���ӁF��񋟓I�����͌^�ڎ�I���ڐ��s���B�L���͌^�������ݕ�������B��@�CMobilenet_V1_1.0_224 �͌^�ڎ� 224x224 ���f�I���B<br /><br />
���L�͌^�s�v�������f�L�O���F�ʓ��i�A�A�j�B�ʉ��I�͌^�����ʓ����v 1 �����C���_�͌^�����ʓ����v 4 �����B<br /><br />
��I <a href="android.md">Android</a> �a <a href="ios.md">iOS</a> ��{�W�����@�����S�ڐ������������͌^���v�I�i���B

## ����͌^

��񋟓I�͌^��p�� 1000 ���B�����I��\�F<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip">�͌^��</a>�B

�\�g�p _�ڊw_ �Z����(re-train)�꘢�͌^�C�ȐV�I�B��@�\�Ĉ꘢�͌^���敪�s���i�I�C�s�ǌ��n��������v�L�B�������ړI�C�I���V�s���v��ЁB

�w�@���ڊw�F<a href="https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android/#0">�p TensorFlow �ԙ�</a> codelab�B