# ��(Tensors) �a ����(operations)

TensorFlow.js���꘢��JavaScript���g�p�ʗ����s�Z�I�y�ˁB�ʐ����ʘa����X���x�I�����B

## ��(Tensors)

`tf.Tensor`��TensorFlow.js���I�ŏd�v�I�������C�����꘢�`��ꈽ�������I���I�W���B`tf.Tensor`�a���������I�����B

�꘢`tf.Tensor`��ܔ@������:

*   `rank`: �ʓI�x
*   `shape`: ���x�I�����召
*   `dtype`: �ʒ��I�����^

>���F�ݍ@�����C�䏫�p�g�x�idimension�j�h�\��`rank�i���j`�B�݊���w���C�ʓI�g���idimensionality�j�h�L��w����x�I�召�B�i��@�C�꘢�`��[10, 5]�I�鐥�꘢rank-2 �I�ʁC���҉Ȑ��꘢2-�I�ʁB��꘢�x�I����10�B���ȍݗ��p���I�����C�`�q�ꉺ���I�o�d�p�@�C��ƔV�@�I�����B�j

��ȗp`tf.tensor()`���@���꘢��(array)���꘢`tf.Tensor`�F

```js
// ���꘢�������꘢rank-2�I�ʋ�
const a = tf.tensor([[1, 2], [3, 4]]);
console.log('shape:', a.shape);
a.print();
// ���҉ȗp�꘢�ꐔ��w�����I�`�󗈌��꘢��
const shape = [2, 2];
const b = tf.tensor([1, 2, 3, 4], shape);
console.log('shape:', b.shape);
b.print();
```

���ғI��v���C`tf.Tensor`�I�����^��A��
`dtype`32�ʕ��_�^(`float32`)�B���R`tf.Tensor`��Ȕ팚�ȉ������^�F�z(`bool`), 32�ʐ��^(`int32`),
64�ʐ�(`complex64`), �a������(`string`)�F

```js
const a = tf.tensor([[1, 2], [3, 4]], [2, 2], 'int32');
console.log('shape:', a.shape);
console.log('dtype', a.dtype);
a.print();
```

TensorFlow.js����񋟗���n����֓I�͎��p�쌚�����ʁC��@���ʓU������I��������`HTMLImageElement`����ʁB���R�ȍݕ������Q���X���I[���@](https://js.tensorflow.org/api/latest/#Tensors-Creation)�B

#### �C���ʓI�`��

`tf.Tensor`���I���f���ʐ����ʓI�`��I��(��@�꘢�`��[2,3]�I�ʏ��ܗL�I���f����2*3=6��)�B���ȍݑ啔����s���`��I�ʓI�召�p�������I,�ߏ��꘢`tf.Tensor`���`��(reshape)���O�꘢�`��ʏ퐥�L�p���L���I�B��q����ȗp`reshape()`
���@:

```js
const a = tf.tensor([[1, 2], [3, 4]]);
console.log('a shape:', a.shape);
a.print();

const b = a.reshape([4, 1]);
console.log('b shape:', b.shape);
b.print();
```

#### ��ʓI

�@�ʑz�v��꘢`tf.Tensor`�I�C�Ȏg�p`Tensor.array()` or `Tensor.data()`�����@:

```js
 const a = tf.tensor([[1, 2], [3, 4]]);
 //�ԉ񑽐��I
 a.array().then(array => console.log(array));
 // �ԉ�ʏ���ܓI���L�I�ꐔ
 a.data().then(data => console.log(data));
```

�䓯��񋟗������@�\�X�p�I���s�Ŗ{�C�A�������@�\��v�I�p���������ꍱ���\�r�B�ݐ����I�p�������C�n��g�p���@�B

```js
const a = tf.tensor([[1, 2], [3, 4]]);
 //�ԉ񑽐��I
console.log(a.arraySync());
// �ԉ�ʏ���ܓI���L�I�ꐔ
console.log(a.dataSync());
```

## ����

�Ȏg�p�ʑ������C������(operation)�ȑ��썱�����BTensorFlow.js�񋟗����\�ݗʏ�s�C�p�����㐔�a����w�I����B

��1: `tf.Tensor`�����L�I���f�sx<sup>2</sup>����:

```js
const x = tf.tensor([1, 2, 3, 4]);
const y = x.square();  // ������ tf.square(x)
y.print();
```

��2: ���� `tf.Tensor`���I���f����:

```js
const a = tf.tensor([1, 2, 3, 4]);
const b = tf.tensor([10, 20, 30, 40]);
const y = a.add(b);  // ������ tf.add(a, b)
y.print();
```

���ʐ��s�I�C���ȍ��Z��s��X�����I�B���I�������ԉ�꘢�V�I`tf.Tensor`�B

> ��: �啔���I�����ԉ� `tf.Tensor`,
> �R���ʉ\�s�����Z�o���B�Ӗ��������I`tf.Tensor`�㐥�Z�I�꘢�啿�B���p`Tensor.data()`����`Tensor.array()`�C�����@����ҎZ�����V�@�ˏ�����͏o���B�Ӗ����n�捱���@�I�Ŗ{���s�����Ŗ{�C�Ȕ�ƍݎZ�I�����j��UI���B

�ȍݗ��Q���X����Tensorflow.js��[����](https://js.tensorflow.org/api/latest/#Operations)�I�Z�x���B

## ����

���g�pWebGL�@�[, `tf.Tensor`�I�����K�Ȏ��Ǘ��B����WebGL�s����`tf.Tensor`���o���������@�����펩���B

�Ȏg�p`dispose() `���@����`tf.dispose()`���@�p�ȕ�`tf.Tensor`����p�I����:

```js
const a = tf.tensor([[1, 2], [3, 4]]);
a.dispose(); // ������ tf.dispose(a)
```

�݈꘢�p�������C����������ڍ݈�N������I�B�ۑ����L���ʓI���p�ȕ�������p�I���~���I���B����r���CTensorFlow.js�񋟗�`tf.tidy()`���@�B�����@�Ȑ��^���L�ݍs�����@�v�L�ԉ�I`tf.Tensor`,�a�s�������^�ꍱ�Ǖ��ʓI���@�L����:

```js
const a = tf.tensor([[1, 2], [3, 4]]);
const y = tf.tidy(() => {
  const result = a.square().log().neg();
  return result;
});
```

�ݘ���q���C`square()`�a`log()`���������v�L�ԉ�C���C���ț��I�ʉ�I����B��`neg()`��`tf.tidy()`�I�ԉ�C���ț��I�ʕs�����B

���R�Ȏ�TensorFlow.js�������ʓI���ʁB

```js
console.log(tf.memory());
```

`tf.memory()`����ň�o�L���O���z�����������I�M���B��[��](https://js.tensorflow.org/api/latest/#memory)�ȓ��X���I���B
