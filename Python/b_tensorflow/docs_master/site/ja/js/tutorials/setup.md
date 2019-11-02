# ����

Note: �����̃h�L�������g�͎�����TensorFlow�R�~���j�e�B���|�󂵂����̂ł��B�R�~���j�e�B�ɂ��
�|���**�x�X�g�G�t�H�[�g**�ł��邽�߁A���̖|�󂪐��m�ł��邱�Ƃ�[�p��̌����h�L�������g](https://www.tensorflow.org/?hl=en)��
�ŐV�̏�Ԃ𔽉f�������̂ł��邱�Ƃ�ۏ؂��邱�Ƃ͂ł��܂���B
���̖|��̕i�������コ���邽�߂̂��ӌ����������̕��́AGitHub���|�W�g��[tensorflow/docs](https://github.com/tensorflow/docs)�Ƀv�����N�G�X�g�������肭�������B
\
�R�~���j�e�B�ɂ��|��⃌�r���[�ɎQ�����Ă�����������́A
[docs-ja@tensorflow.org ���[�����O���X�g](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)�ɂ��A�����������B

## �u���E�U�̏���

�u���E�U�x�[�X�̃v���W�F�N�g��TensorFlow.js�𗘗p������@�͎��2����܂��B 

- [script�^�O](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_JavaScript_within_a_webpage)���g�p���� 
- [NPM](https://www.npmjs.com)����C���X�g�[�����A[Parcel](https://parceljs.org/)��[WebPack](https://webpack.js.org/)�A[Rollup](https://rollupjs.org/guide/en)�Ȃǂ̃r���h�c�[�����g�p����

�E�F�u�J���ɓ���݂��Ȃ�������Awebpack��parcel�Ȃǂ̃c�[���ɂ��ĕ��������Ƃ��Ȃ���΁A_script�^�O���g�p���邱�Ƃ��������߂��܂��B_�o�����L�x��������A���傫�ȃv���O�������������Ƃ��Ă���ꍇ�ɂ́A�r���h�c�[���̗��p�����݂鉿�l������ł��傤�B

### script�^�O����g�p����

�ȉ���script�^�O�����C����HTML�t�@�C���ɒǉ����Ă��������B

```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>
```

<section class="expandable">
  <h4 class="showalways">See code sample script tag setup</h4>
  <pre class="prettyprint">
// ���`��A���f�����`
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// �P���p�̖͋[�f�[�^�𐶐�
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// �f�[�^���g�p���ă��f�����P��
model.fit(xs, ys, {epochs: 10}).then(() => {
  // ���f�����g�p���ă��f�����������Ƃ̂Ȃ��f�[�^�|�C���g�𐄘_
  model.predict(tf.tensor2d([5], [1, 1])).print();
  // ���ʂ��m�F���邽�߂Ƀu���E�U��DevTools���J��
});
  </pre>
</section>

### NPM����C���X�g�[��

[npm cli](https://docs.npmjs.com/cli/npm)�c�[����[yarn](https://yarnpkg.com/en/)�̂ǂ���ł�TensorFlow.js���C���X�g�[���ł��܂��B

```
yarn add @tensorflow/tfjs
```

_�܂���_

```
npm install @tensorflow/tfjs
```

<section class="expandable">
  <h4 class="showalways">See sample code for installation via NPM</h4>
  <pre class="prettyprint">
import * as tf from '@tensorflow/tfjs';

// ���`��A���f�����`
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// �P���p�̖͋[�f�[�^�𐶐�
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// �f�[�^���g�p���ă��f�����P��
model.fit(xs, ys, {epochs: 10}).then(() => {
  // ���f�����g�p���ă��f�����������Ƃ̂Ȃ��f�[�^�|�C���g�𐄘_
  model.predict(tf.tensor2d([5], [1, 1])).print();
  // ���ʂ��m�F���邽�߂Ƀu���E�U��DevTools���J��
});
  </pre>
</section>


## Node.js�̏���

[npm cli](https://docs.npmjs.com/cli/npm)�c�[����[yarn](https://yarnpkg.com/en/)�̂ǂ���ł�TensorFlow.js���C���X�g�[���ł��܂��B

**�I�v�V����1:** �l�C�e�B�uC++�o�C���f�B���O�̕t������TensorFlow.js���C���X�g�[��

```
yarn add @tensorflow/tfjs-node
```

_�܂���_

```
npm install @tensorflow/tfjs-node
```

**�I�v�V����2:** (Linux�̂�)
�V�X�e����[CUDA support](https://www.tensorflow.org/install/install_linux#NVIDIARequirements)�̂���NVIDIAR
GPU������΁A��荂���p�t�H�[�}���X���������邽�߂�GPU�p�b�P�[�W���g�p

```
yarn add @tensorflow/tfjs-node-gpu
```

_�܂���_

```
npm install @tensorflow/tfjs-node-gpu
```

**�I�v�V����3:** �s���AJavaScript�o�[�W�������C���X�g�[���B�p�t�H�[�}���X�̊ϓ_����͍ł��x���I�����ł��B

```
yarn add @tensorflow/tfjs
```

_�܂���_

```
npm install @tensorflow/tfjs
```


<section class="expandable">
  <h4 class="showalways">See sample code for Node.js usage</h4>
  <pre class="prettyprint">
const tf = require('@tensorflow/tfjs');

// �I�v�V�����Ƃ��ăo�C���f�B���O��ǂݍ���
// GPU��œ��삷��ꍇ��'@tensorflow/tfjs-node-gpu'���g�p���Ă�������
require('@tensorflow/tfjs-node');

// �P���ȃ��f�����P��
const model = tf.sequential();
model.add(tf.layers.dense({units: 100, activation: 'relu', inputShape: [10]}));
model.add(tf.layers.dense({units: 1, activation: 'linear'}));
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

const xs = tf.randomNormal([100, 10]);
const ys = tf.randomNormal([100, 1]);

model.fit(xs, ys, {
  epochs: 100,
  callbacks: {
    onEpochEnd: (epoch, log) => console.log(`Epoch ${epoch}: loss = ${log.loss}`)
  }
});
  </pre>
</section>

### TypeScript

TypeScript���g�p���Ă��āA�v���W�F�N�g�Ō�����null�`�F�b�N���g�p���Ă����`tsconfig.json`�t�@�C����`skipLibCheck:
true`��ݒ肷��K�v������ł��傤�B�������Ȃ���΃R���p�C�����ɃG���[���������܂��B
