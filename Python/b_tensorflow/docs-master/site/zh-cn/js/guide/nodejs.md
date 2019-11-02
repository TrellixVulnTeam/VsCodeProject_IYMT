# Node ���I TensorFlow.js

## TensorFlow CPU

TensorFlow CPU ��C�Ȉ@���������F


```js
import * as tf from '@tensorflow/tfjs-node'
```


��������� TensorFlow.js �C���I�͏��R TensorFlow C �񐧕���������� CPU ��s�BCPU ��I TensorFlow �g�p�d�����������������I���㐔�Z�B

������p���x�� TensorFlow �I Linux�CWindows �a Mac ����B

> ���ӁF�v�L�K�v��'@tensorflow/tfjs'���ҏ����Y�����I package.json �������C���R Node �ړ��I�B


## TensorFlow GPU

TensorFlow GPU ��C�Ȉ@���������F


```js
import * as tf from '@tensorflow/tfjs-node-gpu'
```

�^ CPU ���C���I�͏��R TensorFlow C �񐧕��������C�A�������g�p CUDA �� GPU ��s�ʎZ�C�������\�s�� Linux ����B��䑴����ȉ������꘢���ʁB

> ���ӁF������ڑO�p�� CUDA�B�ݖ{���ĔV�O�C���v�ݗL NVIDIA �I�I�������� CUDA�B

> ���ӁF�v�L�K�v��'@tensorflow/tfjs'�������Y�����I package.json �������C���R Node �ړ��I�B


## ���� CPU

�g�p���� CPU �s TensorFlow.js �Ŗ{�C�Ȉ@���������F


```js
import * as tf from '@tensorflow/tfjs'
```

����^�݊풆�g�p�I��B�ݘ���C���p���� CPU ��Ȍ��� JavaScript �s�B����䑴��������C�����s���v TensorFlow �񐧕����C�A�����x�v�������B

�R��������s�˘� TensorFlow�C�������p���x�� Node.js �I�X���C���s�� Linux�CWindows �a Mac����B


## �����l���f

Node.js Bindings  TensorFlow.js �񋟗��꘢���n�s����I�@�[�B�Ӗ������p�꘢����C��@ `tf.matMul(a, b)`�C�����j�ǎ�����������슮���B

�����C���O Bindings ��퍇�r�{�a�C�B�@�ʗv�ݗp�����i�@�FWeb ����j���g�pNode.js Bindings�C�u�꘢�H��񈽒u�ꍱ�H����C�ȕ֓I TensorFlow.js ��s��j�~����B


## APIs

��U�ݏ�ʓI�C��������� tf �@�C���L���ʓI TensorFlow.js �����s���o�ݓ��I�͏�B

### tf.browser

�ݕ��ʓI TensorFlow.js ��C`tf.browser.*` �����󒆓I�������� Node.js ���s�p�C�����g�p�����I API�B

�ڑO�C�L�@�� API�F

*   tf.browser.fromPixels
*   tf.browser.toPixels

### tf.node

�L�� Node.js ��񋟗��꘢���� `tf.node` �I������C������ܗ����� Node �I API�B

TensorBoard ���꘢���� Node.js API �I�d�v��q�B

���꘢���I(summaries)�o��Node.js�ITensorBoard���I�ė�

```js
const model = tf.sequential();
model.add(tf.layers.dense({units: 1}));
model.compile({
  loss: 'meanSquaredError',
  optimizer: 'sgd',
  metrics: ['MAE']
});


// �������ړI�����ꍱ��������B
const xs = tf.randomUniform([10000, 200]);
const ys = tf.randomUniform([10000, 1]);
const valXs = tf.randomUniform([1000, 200]);
const valYs = tf.randomUniform([1000, 1]);


// �n�͌^���B
await model.fit(xs, ys, {
  epochs: 100,
  validationData: [valXs, valYs],
   // �ݗ��Y�� tensorBoard ��B
  callbacks: tf.node.tensorBoard('/tmp/fit_logs_1')
});
```
