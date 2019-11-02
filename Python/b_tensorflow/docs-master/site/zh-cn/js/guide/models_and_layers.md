# �͌^�a

����w���C�꘢ _model_ ���꘢�L��[�Q��](https://developers.google.com/machine-learning/glossary/#parameter)�I�����B�������������o�B�ʑ��I���C�������\�����a�o�V�I�n�B��ʍݐ����W��͌^�����ŉ��Q���B�D�I�͌^�Ȑ��I����������z�����I�o�B

TensorFlow.js�L������w�I���@�F

1.  �p Layers API�i�p _layers_ �����͌^�j
2.  �p Core API�i��[�Z�q�C��@ `tf.matMul()`��`tf.add()`���j�������͌^

�����p��API�FLayers API�������͌^�B�R�@�C���W���@���pCore API�����������I�͌^�B

## �pLayers API���͌^

Layers API�L�������͌^�F��ꐥ�� _sequential_ �͌^�C��񐥌� _functional_ �͌^�B���ʒi���͌^�������B

### �g�psequential model

�ŏ�I�͌^��<code>[Sequential](https://js.tensorflow.org/api/0.15.1/#class:Sequential)</code>�͌^�BSequential�͌^��㤓I��I�݈�N�B�ȏ����v�I���ʍ݈꘢��\���C�R�@����\��<code>[sequential()](https://js.tensorflow.org/api/0.15.1/#sequential)</code> �����I���F

```js
const model = tf.sequential({
 layers: [
   tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}),
   tf.layers.dense({units: 10, activation: 'softmax'}),
 ]
});
```

���p `add()` ���@�F

```js
const model = tf.sequential();
model.add(tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}));
model.add(tf.layers.dense({units: 10, activation: 'softmax'}));
```

> ���ӁF�͌^�I�����v�g���`��h�Q���i`inputShape`�j�B�s�v�݁g���^��h�����batch size�i�᎟�召�j�B��v���͌^���꘢�`��`[B, 784]`�I�ʁi`B`���C��batch size�j�C�����v���g���^��h`[784]`�B

�Ȓ�`model.layers`���g�p�͌^���I��B��@�C�ȗp`model.inputLayers`�a`model.outputLayers`���p���a�o�B

### �g�pfunctional model

���Ȓ�`tf.model()`����`LayersModel`�B`tf.model()`�a`tf.sequential()`�I��v��C�ȗp`tf.model()`�����C����I�Z�B

�ȉ�����i�@���p`tf.model()` API �����a�㕶�����͌^�I��q�F

```js
// �papply()���@���C�ӎZ
const input = tf.input({shape: [784]});
const dense1 = tf.layers.dense({units: 32, activation: 'relu'}).apply(input);
const dense2 = tf.layers.dense({units: 10, activation: 'softmax'}).apply(dense1);
const model = tf.model({inputs: input, outputs: dense2});
```

��݈�p`apply()`�����I�o��{�I���B`apply()`�ԉ�꘢`SymbolicTensor`�i�����ʁC�A�s��ܔC�����j

�s����sequential model�g�p`inputShape`������I���C��p`tf.input()`���I`SymbolicTensor`����I��

�@�ʌ�`apply()`���꘢���ʁC����s�Z��Ԉ꘢���ʁF

```js
const t = tf.tensor([-2, 1, 0, 5]);
const o = tf.layers.activation({activation: 'relu'}).apply(t);
o.print(); // [0, 1, 0, 5]
```

�������p���ƈ�󛀓I�o�B

�asequential model��C�Ȓ�`model.layers`���g�p�͌^���I��B��@�C�ȗp`model.inputLayers`�a`model.outputLayers`���p���a�o�B

## 

Sequential model�afunctional model�s����`LayersModel`�B�g�p`LayersModels`�X���ցF���v������`��C��p��I�`�󗈖͌^�I���B`LayersModel`��Z�͌^�����L�ʓI�`��B�m���ʓI�`��@�C�͌^�A�Ȏ����������v�I�Q���B��ȗp�`��M�������f���I���ۑ��݌��e�B

## �͌^

�g�p`model.summary()`�Ȏ��k���͌^�I�d�v�M���C��F

*   ��I�����a�^
*   ��I�o�`��
*   ��I�d����
*   ��I��
*   �꘢�͌^�L�I�Q���ʁC�a�s�Q����

�p�O�ʒ�I�͌^������q�C��ȍݖ��ߍs�������ȉ��M���F

<table>
  <tr>
   <td>Layer (type)
   </td>
   <td>Output shape
   </td>
   <td>Param #
   </td>
  </tr>
  <tr>
   <td>dense_Dense1 (Dense)
   </td>
   <td>[null,32]
   </td>
   <td>25120
   </td>
  </tr>
  <tr>
   <td>dense_Dense2 (Dense)
   </td>
   <td>[null,10]
   </td>
   <td>330
   </td>
  </tr>
  <tr>
   <td colspan="3" >Total params: 25450<br/>Trainable params: 25450<br/> Non-trainable params: 0
   </td>
  </tr>
</table>

���ӁF��I�o�`�󒆓s�ܗL`null`�B�͌^�I���`���ܗ��᎟�召�C���᎟�召���Ȋ��X�I�C���Ȕ᎟�I�ݗʌ`�󒆈�`null`���B

## ����

������[API�����C�g�p`LayersModel`�I�꘢�D�����֑��A���͌^�B`LayersModel`��ܔ@���M���F

*   �p���d���͌^�I�͌^�ːM��
*   �͌^�I�d
*   �z�u�i��@�������C����a�ĕ����j
*   ����I��i�p���͌^�j

���a���͌^�����v��s��F

```js
const saveResult = await model.save('localstorage://my-model-1');
const model = await tf.loadLayersModel('localstorage://my-model-1');
```

�ݘ���q���C�͌^�푶�݊�I�{�n�����B<code>[model.save()](https://js.tensorflow.org/api/latest/#tf.Model.save)</code>�a[save and load](save_load.md)����@���c�͌^�ۑ��ݕs���I�}��i��@ file storage, <code>IndexedDB</code>, �G�����퓙���j�B

## ����

�����͌^�I��B�@�ʓI�͌^���v�萧���Z�́C�Ȏʈ꘢����󝇓��͌^���B���ʓI��q���꘢�Z�����a�I����F

```js
class SquaredSumLayer extends tf.layers.Layer {
 constructor() {
   super({});
 }
 // In this case, the output is a scalar.
 computeOutputShape(inputShape) { return []; }

 // call() is where we do the computation.
 call(input, kwargs) { return input.square().sum();}

 // Every layer needs a unique name.
 getClassName() { return 'SquaredSum'; }
}
```

�ȗp`apply()`���@�݈꘢�ʏ㘢����

```js
const t = tf.tensor([-2, 1, 0, 5]);
const o = new SquaredSumLayer().apply(t);
o.print(); // prints 30
```

> ���ӁF�@�ʍݖ͌^����ܗ�����C�͌^���s�\����

## �pCore API���͌^

�{���񓞗���TensorFlow.js�������͌^�I���@�B�ŏ�p�I�������g�p Layers API�C�����I�͎���������p�IKeras API�i�� [best practices and reduces cognitive load](https://keras.io/why-use-keras/)�j�BLayers API�񋟗���ʕ��֓I�H��C��@�d���n���C�͌^���񉻁C�C�ڐ��a���S�B

�������@����v�C�\����v�g�pCore API�F

*   ���v�X�������a�T��
*   �s���v���񉻈��ȑ����ȓI���񉻕��@

�pCore API�ʓI�͌^��ܗ���n��I�����B�������Ȉ꘢�������ʍ���C��o�꘢�ʁB��ȗpCore API���d�ʔV�O��I�͌^�F

```js
// The weights and biases for the two dense layers.
const w1 = tf.variable(tf.randomNormal([784, 32]));
const b1 = tf.variable(tf.randomNormal([32]));
const w2 = tf.variable(tf.randomNormal([32, 10]));
const b2 = tf.variable(tf.randomNormal([10]));

function model(x) {
  return x.matMul(w1).add(b1).relu().matMul(w2).add(b2).softmax();
}
```

��Core API���C����v���Ȍ��a���n���d�B���d�s���꘢`Variable`�CTensorFlow.js��c`Variable`�d�ʁB�ȗp[tf.variable()](https://js.tensorflow.org/api/latest/#variable)��`Variable`���c�꘢�ߑ��ݓI�ʕ���`Variable`���B

�{����@���pLayers�aCore API���͌^�B�ډ����C��[training models](train_models.md)�w�@���͌^�B
