# ����a��

TensorFlow.js�L�H�약��F��aNode.js�B�s������L�k���s���I�z�u�C����I���e�������I�p�B

�݊핽���CTensorFlow.js���x���ځC��x���䎮�B�R�V�L�k�����CTensorFlow.js�񋟓IWebGL API�\��������I���z�u�B

��Node.js�����CTensorFlow.js���x�����ڎg�pTensorFlow API�C��x���X���ICPU���B

## [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#environments)��

���꘢�pTensorFlow.js�I�����s�C���L�I�z�u��̋��B����܈꘢�S�ǓIbackend�C�ȋy�ꍱ�Ȑ��T��TensorFlow.js�����I�B

### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#backends)Backends

TensorFlow.js�x�������s���Ibackend�C�p���ʓI���a���w����B�C����s���L�꘢backend�����B�啔���CTensorFlow.js������O�����g�p�ŉ��Ibackend�B���g�C���R���v�m���C�@�����m���O���ݎg�p�I����backend�C�ȋy�@���ݕs��backend�V�؁B

���ʖ��ߗp���擖�O���g�p�Ibackend
```js
console.log(tf.getBackend());
```

���ʖ��ߗp�����backend
```js
tf.setBackend(�ecpu�f);
console.log(tf.getBackend());
```

#### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#webgl-backend)WebGL backend

WebGL backend�C�́gwebgl�h�C���݊핽���ő�I�꘢backend�B����CPU backend�v��100�{�B�����������CTensor����WebGL���ۑ��I�C���w�Z�����WebGL shader���ʁB

���ʐ��ݎg�p��backend���v����I�ꍱ�m�B

##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#avoid-blocking-the-ui-thread)��Ƒj��UI��
���p�꘢����C�@tf.matMul(a,b)�C�ԉ�tf.Tensor��ԉ�C�R���阩�@�Z�s��芮���B�Ӗ����ԉ�tf.Tensor�����꘢�w���Z�I�啿�B���p`x.data()`��`x.array()`�C���L���Z�����˔\�擞�B�����ݎZ�����C��Ƒj��UI���C���v�g�p�Ŗ{�I`x.data()`�a`x.array()`�C���s�����Ŗ{�I`x.dataSync()`�a`x.arraySync()`�B
##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#memory-management)�����Ǘ�

�ꉺ�C�ݎg�pWebGL backend�C���v���Ǘ������B����Tensor�IWebGL���C�s����I���W�����������B

�pdispose()����tf.Tensor��p�I����

```js
const a = tf.tensor([[1,2], [3,4]]);
a.dispose();
```

�ݗp���C����v�c�������썇�N���B���꘢���L���ʓI���p�C�R�@��������p�I�����C���@�g������BTensorFlow.js��tf.tidy()���@���������ԉ�s�Ď��v�Itf.Tensor�C�A�D�������s�@�C�{�n�ʓs��퐴����B

```js
const a = tf.tensor([[1, 2], [3, 4]]);
const y = tf.tidy(() => {
  const result = a.square().log().neg();
  return result;
});
```

>���ӁF������WebGL���i�@Node.js TensorFlow backend��CPU backend�j�L���񝾊����C�ݍ������g�pdispose()��tidy()�v�L����p�B��C��p�ʏ���񝾓I�������X�D�I���\�B

##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#precision)���x

�݈ځCWebGL���x��16�ʕ��_������B�R���C�啔������w�͌^�s�p32�ʕ��_�Iweight�aactivation�I�B�R��16�ʕ��_�������\�\��[0.000000059605�C 65504]��䗁C���c�͌^�ڐA���ځC������x�B���v�ێ��Ȗ͌^���Iweight�aactivation�s�v���o��䗁B
##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#shader-compilation--texture-uploads)Shader& texture ��
TensorFlow.js��GPU���sWebGL�Ishader�����B�R����shader���L�ݔ�p�ˉ��C��lazy-compile�B����CPU��I��������C�v�������BTensorFlow.js����D�Ishader�C�����ėp�L��shape�C�����o�Itensor�\���k���BTensorFlow.js�I�p��ʉ���g�p���I����C������񎟍s����k���B

TensorFlow.js��ctf.Tensor������WebGL���B���꘢tf.Tensor�팚�@�C�s��헧���㓞GPU�C����������p���˘�B�@�ʘ�tf.Tensor���񎟎g�p�C�R���ߍ�GPU���C�����ȝ{����B�݈꘢�T�^�I����w�͌^���C�Ӗ���weight�ݑ�ꎟ���C��񎟏A����k���B

�@�ʊ�]������ꎟ�I���\�C�䐄䦖͌^�s�C���꘢�L��shape�I��Tensor�B
��@:
```js
const model = await tf.loadLayersModel(modelUrl);
// �g�p�^�������͌^
const warmupResult = model.predict(tf.zeros(inputShape));
warmupResult.dataSync();
warmupResult.dispose();

// ��񎟍s predict() �I�󏫉�X������
const result = model.predict(userData);
```

#### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#nodejs-tensorflow-backend)Node.js TensorFlow backend

��Node.js TensorFlow backend���C���gnode�h,��TensorFlow�IC��API��p����������B����s�\�g�p����I�d�������́C�@CUDA�B

�ݘ�backend���C�aWebGL backend��C������ԉ�`tf.Tensor`�B�R���C�^WebGL backend�s���I���C������tensor�ԉ�C�Z�ߊ����B�Ӗ���`tf.matMul(a,b)`�p��j��UI���B

�����C�@�ʍݐ������g�p�����@�C���v�ݍH������p�C���s������B

�X����Node.js�I�M���C�ő������B
#### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#cpu-backend)CPU backend

��backend�����\�ō��Ibackend�C�R�����œI�B���L����s��vanilla JavaScript���C�����k���L��s���C�󊎉�j��UI���B

��backend�L�p�C���Ґ��p��WebGL�s�\�g�p�I�B

### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#flags)Flags

TensorFlow.js�L�꓅���C�\���Ęa�C�ې����O�����I�ŉ��z�u�B���啔���������g�p�C�����L�ꍱ�S�ǉȔ�API�T���B

-   `tf.enableProdMode():`  �p���͎��B����{�͌^�CNaN�C�ȋy�����Z����C�����񍂐��\�B
-   `tf.enableDebugMode()`: �p�͎��B�����I���u��o������C�s���\�M���C�@����footprint�a���j�s�B���ӏ���~��p�s�C�s�ݐ������g�p�B

���F���@�ݒ����I�őO�ʗp�C�����e���L�I�����B����I�����C�v�L���Idisable���@�B

���F���L�ݍT����stf.ENV.features�B�s�ǖv�L�I��API�i�s���v�l�Ŗ{���e�j�C�Ȏg�ptf.ENV.set�������C���������������f�B
