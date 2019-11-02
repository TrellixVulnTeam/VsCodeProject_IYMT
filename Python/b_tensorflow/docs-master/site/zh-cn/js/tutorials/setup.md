# ����

## �����

�݊��I�ڒ���TensorFlow.js�L�ȉ���v���@

-   �g�p
    [�r�{(script tags)](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_JavaScript_within_a_webpage)�B
-   ��[NPM](https://www.npmjs.com)�����󊎎g�p[Parcel](https://parceljs.org/),
    [WebPack](https://webpack.js.org/)����
    [Rollup](https://rollupjs.org/guide/en)�I���H��B

�@�ʕs�n��Web�C���Ҙ�����webpack��parcel���H��C_�䌚�g�p�r�{(script
tags)_�B�@�ʕx���z�v�ʍX��I�����C�ߎg�p���H��s�T���\�X�����B

### �g�p�r�{(script tags)

���ȉ��r�{�Y�����I��HTML�������F


```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script>
```

�L�r�{�I�u�C�Q�㎦��F

<section class="expandable">
  <h4 class="showalways">See code sample script tag setup</h4>
  <pre class="prettyprint">
//��꘢����͌^�B
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// �����ꍱ��������
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// �g�p�����͌^
model.fit(xs, ys, {epochs: 10}).then(() => {
// �ݖ͌^�����œ��I�����_��g�p�͌^�s����

  model.predict(tf.tensor2d([5], [1, 1])).print();
  // �Ŋ�H��ŏo
});
  </pre>
</section>

### ��NPM����

�Ȏg�p
[npm cli](https://docs.npmjs.com/cli/npm)�H���[yarn](https://yarnpkg.com/en/)����TensorFlow.js�B

```
yarn add @tensorflow/tfjs
```

_����_

```
npm install @tensorflow/tfjs
```

<section class="expandable">
  <h4 class="showalways">See sample code for installation via NPM</h4>
  <pre class="prettyprint">
import * as tf from '@tensorflow/tfjs';

//��꘢����͌^�B
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// �����ꍱ��������
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// �g�p�����͌^
model.fit(xs, ys, {epochs: 10}).then(() => {
  // �ݖ͌^�����œ��I�����_��g�p�͌^�s����
  model.predict(tf.tensor2d([5], [1, 1])).print();
  //  �Ŋ�H��ŏo
});
  </pre>
</section>


## Node.js ����

�Ȏg�p
[npm cli](https://docs.npmjs.com/cli/npm)�H���[yarn](https://yarnpkg.com/en/)����TensorFlow.js�B

**1:** �����L����C++��ITensorFlow.js�B

```
yarn add @tensorflow/tfjs-node
```

_����_

```
npm install @tensorflow/tfjs-node
```

**2:**
�i��Linux�j�@�ʓI�n��L[�x��CUDA](https://www.tensorflow.org/install/install_linux#NVIDIARequirements)�INVIDIARGPU�C�g�pGPU��ȓ��X���I���\�B

```
yarn add @tensorflow/tfjs-node-gpu
```

_or_

```
npm install @tensorflow/tfjs-node-gpu
```

**3:** ����JavaScript�Ŗ{�C�����\���ʍŖ��I�B

```
yarn add @tensorflow/tfjs
```

_or_

```
npm install @tensorflow/tfjs
```

<section class="expandable">
  <h4 class="showalways">See sample code for Node.js usage</h4>
  <pre class="prettyprint">
const tf = require('@tensorflow/tfjs');

// ����F
// �@�ʎg�pGPU�s�C�g�p'@tensorflow/tfjs-node-gpu'
require('@tensorflow/tfjs-node');

// �꘢�͌^:
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

���g�pTypeScript�C�@�ʓI�ڎg�p�i�I��C���ҍݒ��������C�\���v�ݓI`tsconfig.json`�������u`skipLibCheck�Ftrue`�B
