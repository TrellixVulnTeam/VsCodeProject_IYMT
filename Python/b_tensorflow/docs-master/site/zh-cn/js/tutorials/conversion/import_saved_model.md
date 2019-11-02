# ��TensorFlow.js������TensorFlow GraphDef�͌^

TensorFlow GraphDef�͌^�i��ʐ���Python API���I�j�ȕۑ����ȉ��{�i���F
1. TensorFlow [SavedModel](https://www.tensorflow.org/programmers_guide/saved_model#overview_of_saving_and_restoring_models)
2. [Frozen Model](https://www.tensorflow.org/mobile/prepare_models#how_do_you_get_a_model_you_can_use_on_mobile)
3. [Session Bundle](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/session_bundle/README.md)
4. [Tensorflow Hub module](https://www.tensorflow.org/hub/)

�ȏ㏊�L�i���s�Ȕ�[TensorFlow.js converter](https://github.com/tensorflow/tfjs-converter)��TensorFlow.js��I�͌^�i���C��p�����Z�iinference�j�B

�i���ӁFTensorFlow�ߓ�����session bundle�i���C���I�͌^��SavedModel�i���B�j

## �K�v����

�͌^�I�H����v�p��Python���G�ȗp[pipenv](https://github.com/pypa/pipenv) �� [virtualenv](https://virtualenv.pypa.io)���꘢�u�I���B�p�𖽗߈����͌^��F

```bash
 pip install tensorflowjs
```

��TensorFlow�͌^������TensorFlow.js���v���B���C���I�͌^TensorFlow.js�p�Iweb�i���C�R�@����TensorFlow.js���B

## ���F��TensorFlow�͌^��TensorFlow.js�p�I web �i���͌^

�s��񋟓I�r�{�F

�p�@�F��SavedModel��F

```bash
tensorflowjs_converter \
    --input_format=tf_saved_model \
    --output_node_names='MobilenetV1/Predictions/Reshape_1' \
    --saved_model_tags=serve \
    /mobilenet/saved_model \
    /mobilenet/web_model
```

Frozen model ��:

```bash
tensorflowjs_converter \
    --input_format=tf_frozen_model \
    --output_node_names='MobilenetV1/Predictions/Reshape_1' \
    /mobilenet/frozen_model.pb \
    /mobilenet/web_model
```

Tensorflow Hub module ��:

```bash
tensorflowjs_converter \
    --input_format=tf_hub \
    'https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/1' \
    /mobilenet/web_model
```

|�r�{�Q�� | �`�q |
|---|---|
|`input_path`  | saved model, session bundle �� frozen model�I�����I�H�a�C��TensorFlow Hub�͓I�H�a�B|
|`output_path` | �o�����I�ۑ��H�a�B|

|  | �`�q
|---|---|
|`--input_format`     | �v�I�͌^�I�i���BSavedModel  tf_saved_model, frozen model  tf_frozen_model, session bundle  tf_session_bundle, TensorFlow Hub module  tf_hub�CKeras HDF5  keras�B |
|`--output_node_names`| �o�_�I�����C�������p�������B|
|`--saved_model_tags` | ��SavedModel�p�I�F�����v���IMetaGraphDef���Itag�C����tag�p�������u�B�� `serve`�B|
|`--signature_name`   | ��TensorFlow Hub module�p�I�F�v���I���C��`default`�B�Q�l https://www.tensorflow.org/hub/common_signatures/.|

�p�ȉ����ߊŏ��M���F

```bash
tensorflowjs_converter --help
```

### �퐶�I����

�r�{������F

* `model.json` �i�������a�d���j
* `group1-shard\*of\*` �i�񐧏d�����j

����Mobilenet v2�͌^�@�o�I�����F

```html
  output_directory/model.json
  output_directory/group1-shard1of5
  ...
  output_directory/group1-shard5of5
```

## ���F�݊���a�s�͌^

1. ����tfjs-convert npm��F

`yarn add @tensorflow/tfjs` �� `npm install @tensorflow/tfjs`

2. �� [FrozenModel class](https://github.com/tensorflow/tfjs-converter/blob/master/src/executor/frozen_model.ts) ��n���Z�F

```js
import * as tf from '@tensorflow/tfjs';
import {loadGraphModel} from '@tensorflow/tfjs-converter';

const MODEL_URL = 'model_directory/model.json';

const model = await loadGraphModel(MODEL_URL);
const cat = document.getElementById('cat');
model.execute(tf.fromPixels(cat));
```

��̑�Q�l [MobileNet ����](https://github.com/tensorflow/tfjs-converter/tree/master/demo/mobilenet).

`loadGraphModel` API���I`LoadOptions`�Q���ȗp���������Ҏ��苁���I�����B�X���M���Q�l [loadGraphModel() ����](https://js.tensorflow.org/api/1.0.0/#loadGraphModel)�B

## �x���I����

�ڑO�CTensorFlow.js���x������TensorFlow�Z�q�B��I�͌^��ܗ��s��x���I�Z�q�C`tensorflowjs_converter`�r�{����o�I�͌^���s��x���I�Z�q�B��github��N [issue](https://github.com/tensorflow/tfjs/issues)��m�����v�x���I�Z�q�B

## ���͌^�d

������v���͌^�I�d�C�Q�l�ȉ���F

```js
import * as tf from '@tensorflow/tfjs';

const weightManifestUrl = "https://example.org/model/weights_manifest.json";

const manifest = await fetch(weightManifestUrl);
this.weightManifest = await manifest.json();
const weightMap = await tf.io.loadWeights(
        this.weightManifest, "https://example.org/model");
```
