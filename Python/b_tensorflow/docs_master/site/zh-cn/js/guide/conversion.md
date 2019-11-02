# �͌^

TensorFlow.js �z���e�͌^�C���͌^�ȍ݊풆�g�p�C[�͌^](https://github.com/tensorflow/tfjs-models) ���L����B�A���C�\�ߍݑ����n���Q���������꘢ TensorFlow �͌^�C���]�� web �p�������g�p�͌^�B���CTensorFlow.js �񋟗��꘢ [�͌^��](https://github.com/tensorflow/tfjs-converter) �BTensorFlow.js ��L����:

1. �꘢���ߍs�����C�p�� Keras �a TensorFlow �͌^�ȍ� TensorFlow.js ���g�p�B
2. �꘢ API �C�p���݊풆�g�p TensorFlow.js ���a�s�͌^�B

## �I�͌^

TensorFlow.js ��Ȉȉ��{�i���I�͌^:

**SavedModel**: �ۑ� TensorFlow �͌^�I�Ҋi���BSavedModel �I�i�� [��](https://www.tensorflow.org/guide/saved_model)�B

**Keras model**: Keras �͌^�ʏ�ۑ� HDF5 �����B�L�ۑ� Keras �͌^�I�X���M���C [��](https://keras.io/getting-started/faq/#savingloading-whole-models-architecture-weights-optimizer-state)�B

**TensorFlow Hub module**: �����ŕ�@�� TensorFlow Hub ���s���I�͌^�CTensorFlow Hub ���꘢�����a�͌^�I����B�͌^ [��](tfhub.dev)�B

��r���I�͌^�I�i���C���v���s���I�Q����B��@�C��ۑ����꘢�� `model.h5` �I Keras �͌^�� `tmp/` �ځB���g�p TensorFlow.js ��͌^�C�ȍs�ȉ�����: 

    $ tensorflowjs_converter --input_format=keras /tmp/model.h5 /tmp/tfjs_model

��H�a `/tmp/model.h5` �I�͌^��o `model.json` �����y���񐧏d�������� `tmp/tfjs_model/` ���B

�L�s���i���I�͌^���I���ߍs�Q���I�X���M���C�Q TensorFlow.js �� [���q����](https://github.com/tensorflow/tfjs-converter)�B

�ݒ����C���Ֆ͌^�`�� TensorFlow.js ���ێx��������B�@�ʐ��x���I�C�䏫�`����Ȏg�p�I�i���B��ʏ��d���� 4MB �I���������͌^�ȕ֍� web ��g�p - ���A�Ȕ�푶�B���g�p���H�� [Grappler](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/grappler) ���͌^�`�B�`�I���������I�܁C������q�����B���X���͌^�I�o�v�L�e�B���ꉻ�C�p�ȓ��Q���Ȏw���폫�͌^�ʉ�������I���召�B�ʉ����ꏭ�͌^�召�I�Z�C�����ʗp�X���I����\���d�I�B�p�K�ۗʉ��@�͌^�I�y�x�ێ��݉ڎ�䗓��B
�@�ʍݒ����������s�x���I����C�����C�䏫�p�ň�o����I���́B������𓞉�I [GitHub](https://github.com/tensorflow/tfjs/issues)  - �����p�I�����X���V�I����B

### �ŉ����@

�R�ݒ�����s�͉��I�͌^�C�A�ʏ�ۓI�͌^���s�I�ŉ��������ݍl������I�������B�Ӗ�����Ƙ��I���a�s�\���Q���i�d�j�I���ځB

## �s�I�͌^

�����͌^�V�@�C��������d�����a�꘢�͌^�񕶌��BTensorFlow.js �񋟖͌^�� APIs �C�Ȏg�p���ڌ���͌^�󊎍݊풆�s���f�B

�ȉ������@�I TensorFlow SavedModel �� TensorFlow Hub �͓I API :

```js
const model = await tf.loadGraphModel(�epath/to/model.json�f);
```

�ȉ����@�I Keras �͌^�I API :

```js
const model = await tf.loadLayersModel(�epath/to/model.json�f);
```

`tf.loadGraphModel` API �ԉ� `tf.FrozenModel`�C�Ӗ����e�Q�����Œ�I�󊎕s�\�g�p�V�����͌^�s���B`tf.loadLayersModel` API �ԉ�I tf.Model�B�L tf.Model �I���M���C�Q[�͌^�w��](train_models.md)�B

�ݔV�@�C�䌚�s�{�����f�󊎖͌^�I���x�s��y�B����ړI�C��L�꘢�Ɨ��I��y��: https://github.com/tensorflow/tfjs-core/blob/master/integration_tests/benchmarks/benchmark.html�B �\���ӓ���P�����n�s���I�� - �����i�ʏ��v�j���C�R�������a���F��I�����ՁC�I�͌^�I��ꎟ�I���f����@���f���{�{�B
