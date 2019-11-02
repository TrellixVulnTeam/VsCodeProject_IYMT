# TFX ���[�U�[�K�C�h

## �C���g���_�N�V����

TFX �� TensorFlow ��œ��삷��AGoogle �̃v���_�N�V�����X�P�[���̋@�B�w�K�v���b�g�t�H�[���ł��B
����͋@�B�w�K�V�X�e�����`�A�N���A�Ď����邽�߂ɕK�v�Ȑݒ�t���[�����[�N�Ƌ��L���C�u������񋟂��A
�������@�B�w�K�V�X�e���ɓ����ł���悤�ɂ��܂��B

## �C���X�g�[��

[![Python](https://img.shields.io/pypi/pyversions/tfx.svg?style=plastic)](https://github.com/tensorflow/tfx)
[![PyPI](https://badge.fury.io/py/tfx.svg)](https://badge.fury.io/py/tfx)

```
pip install tensorflow
pip install tfx
```

Note: [TensorFlow Serving](https://www.tensorflow.org/serving/),
[TensorFlow JS](https://js.tensorflow.org/),
[TensorFlow Lite](https://www.tensorflow.org/lite) �I�v�V�����̃R���|�[�l���g�ł��B�����̃C���X�g�[���ɂ��ẮA���ꂼ��̃h�L�������g���m�F���Ă��������B

Note: ���̃R�}���h�� [Apache Beam](beam.md) �� Direct runner �Ɠ����ɃC���X�g�[�����܂��B
�ʓr�A[Flink](https://flink.apache.org/)�̂悤�ȃX�g���[�~���O�����i�[���C���X�g�[������K�v������܂��B

## �R�A�R���|�[�l���g

### TFX �p�C�v���C��

TFX �p�C�v���C���͂������̃R���|�[�l���g��p���āA����̋@�B�w�K�^�X�N (���Ƃ��΁A
����̃f�[�^��p������A���f���̍\�z�ƃf�v���C) ���ŏI�I�Ɏ��s���邽�߂̃f�[�^�t���[���`���܂��B
�p�C�v���C���̃R���|�[�l���g�� TFX �̃��C�u������p���č\�z����܂��B
�p�C�v���C���̍ŏI���ʂ́A���_��v������ TFX �f�v���C�����g�^�[�Q�b�g���T�[�r�X�A�܂��͂��̗����ł��B

## TFX �p�C�v���C�� �R���|�[�l���g

TFX �p�C�v���C���͈�A�̃R���|�[�l���g��A���������̂ŁA�X�P�[���u���Ńn�C�p�t�H�[�}���X�ȋ@�B�w�K����������悤�ɐ݌v����Ă��܂��B
����ɂ̓��f�����O�A�P���A���_�̃T�[�r���O�A�����ăI�����C���A�l�C�e�B�u���o�C���A�v���AJavaScript �ւ̃f�v���C�̊Ǘ����܂܂�Ă��܂��B

TFX �p�C�v���C���ɂ͓T�^�I�ɂ͎��̃R���|�[�l���g���܂܂�܂� :

- [**ExampleGen**](examplegen.md) �̓p�C�v���C���̐擪�ɗ���R���|�[�l���g�ŁA
  �f�[�^�Z�b�g�̎�荞�݂ƁA�K�v�ȏꍇ�ɂ͕������s���܂��B

- [**StatisticsGen**](statsgen.md) �̓f�[�^�Z�b�g�̓��v�ʂ��v�Z���܂��B

- [**SchemaGen**](schemagen.md) �͓��v�ʂ��m�F���A�f�[�^�̃X�L�[�}�𐶐����܂��B

- [**ExampleValidator**](exampleval.md) �̓f�[�^�Z�b�g�Ɉُ�l�⌇���l���܂܂�Ȃ������������܂��B

- [**Transform**](transform.md) �̓f�[�^�Z�b�g�ɑ΂��ē����ʃG���W�j�A�����O���s���܂��B

- [**Trainer**](trainer.md) �̓��f�����P�����܂��B

- [**Evaluator**](evaluator.md) �͌P�����������ʂɂ��Đ[�����͂��s���܂��B

- [**ModelValidator**](modelval.md) �͏o�͂��ꂽ���f���̃o���f�[�V�������菕�����A
  �v���_�N�V�������ɓK�p����̂Ɂu�\���ǂ������v�ł��邱�Ƃ�ۏ؂��܂��B

- [**Pusher**](pusher.md) �̓T�[�r�X��񋟂���C���t���X�g���N�`���Ƀ��f�����f�v���C���܂��B

���̐}�͂����̃R���|�[�l���g�Ԃł̃f�[�^�̂���������킵�Ă��܂��B

![Component Flow](diag_all.svg)

### �R���|�[�l���g�̓����\��

TFX �̃R���|�[�l���g�͎���3�̎�v�ȕ������琬�藧���܂��B

- Driver
- Executor
- Publisher

<img src="images/component.svg" alt="Component Anatomy" style="width:40%" />

#### Driver �� Publisher

Driver �̓��^�f�[�^�X�g�A�ɑ΂��ăN�G���𔭍s���A Executor �Ƀ��^�f�[�^��񋟂��܂��B
����APublisher �� Executor �̏o�͂��󂯎�胁�^�f�[�^�Ƃ��ĕۑ����܂��B
�T�^�I�ɂ́A�J���҂� Driver �� Publisher �𒼐ڈ����K�v�͂���܂��񂪁ADriver �� Publisher ���񋟂��郍�O���b�Z�[�W�̓f�o�b�O�̖��ɗ��ł��傤�B
�ڍׂ� [�g���u���V���[�e�B���O](#�g���u���V���[�e�B���O) �ŉ��߂Ď��グ�܂��B

#### Executor

Executor �̓R���|�[�l���g���������s���ӏ��ł��B
�J���҂͂��ꂼ��̃R���|�[�l���g���������Ă���N���X�̎d�l�ɏ]�����R�[�h���L�q���邱�ƂŁAExecutor �̓����Ŏ��s����鏈�����L�q�ł��܂��B
���Ƃ��� [Transform �R���|�[�l���g](transform.md) �𗘗p����ꍇ�A `preprocessing_fn` ����������K�v��������ł��傤�B

## TFX ���C�u����

TFX �̓��C�u�����ƃp�C�v���C���̃R���|�[�l���g�̗������܂�ł��܂��B���̐}�� TFX �̒񋟂��郉�C�u�����ƃR���|�[�l���g�̊֌W��\���Ă��܂��B

![Libraries and Components](libraries_components.svg)

TFX �̓p�C�v���C���̃R���|�[�l���g���쐬���邽�߂ɕK�v�Ȃ������̃��C�u������ Python �p�b�P�[�W�Ƃ��Ē񋟂��܂��B
�����̃��C�u�����́A�����������p�C�v���C���ɓ��L�ȑ��ʂɏW���ł���悤�ɁA�p�C�v���C���̃R���|�[�l���g���쐬����Ƃ��ɗ��p�ł��܂��B

TFX �̃��C�u�����͎��̂��̂��܂�ł��܂�:

- [**TensorFlow Data Validation (TFDV)**](tfdv.md) �͋@�B�w�K�ŗp����f�[�^�̉�͂⌟�؂̂��߂̃��C�u�����ł��B
  ����͍����X�P�[���r���e�B�������A TensorFlow �y�� TFX �Ƃ��܂��A�g�ł���悤�ɐ݌v����Ă��܂��B
  TFDV �͎��̓��e���܂݂܂�:

    * �w�K�f�[�^�ƃe�X�g�f�[�^�̗v�񓝌v�ʂ̃X�P�[���u���ȎZ�o
    * �f�[�^�̕��z�ⓝ�v�ʁA�f�[�^�Z�b�g�̑g�ݍ��킹�ɑ΂��鑽�ʓI�Ȕ�r���s���r���[���[�Ƃ̓���
    * �K�{�ɂȂ�l�A�l��A��b�Ȃǂ̃f�[�^�Ɋ��҂ł�����e���������A�f�[�^�̃X�L�[�}�������I�ɐ���
    * �X�L�[�}�̌�����⏕���邽�߂̃X�L�[�}�r���[���[
    * �����l�A�l��𒴂����l�A����������ʂ̌^�Ƃ������ُ�l����肷�邽�߂ُ̈�l���m
    * �ǂ̓����ʂňُ�l���������̂��m�F���A������C������̂ɕK�v�Ȓm���𓾂邽�߂ُ̈�l�r���[���[

- [**TensorFlow Transform (TFT)**](tft.md) �� TensorFlow �Ńf�[�^�̑O�������s�����߂̃��C�u�����ł��B
  TensorFlow Transform �̓f�[�^�Z�b�g�S�̂�ʂ����������K�v�ȓ����ʂ̎Z�o�ɖ𗧂��܂��B���Ƃ��Ύ��̂悤�ȏ����ł�:

    * ���ςƕW���΍���p�������͒l�̐��K��
    * ���ׂĂ̓��͒l�����b�𐶐����A������𐮐��ɕϊ�
    * �ϑ����ꂽ�f�[�^�̕��z�����Ƃɂ��ċ�Ԃ�ݒ肵�A�����l (float) �����ꂼ��̋�Ԃ�\�������l�ɕϊ�

- [**TensorFlow**](train.md) �� TFX �̃��f�����w�K�����邽�߂ɗ��p����܂��B
  ����͊w�K�f�[�^�ƃ��f���̃R�[�h����͂���ƁA SaveModel ���o�͂��܂��B
  �܂��ATFT �ō쐬���ꂽ�����ʃG���W�j�A�����O�̃p�C�v���C����p���āA���͒l�̑O�������s�����Ƃ��ł��܂��B

- [**TensorFlow Model Analysis (TFMA)**](tfma.md) �� TensorFlow �̃��f����]�����邽�߂̃��C�u�����ł��B
  ����� TensorFlow �Ɠ����ɗ��p���邱�Ƃ� EvalSavedModel �𐶐����邱�Ƃ��ł��܂��B����� TFMA �̕��͂̊�{�ɂȂ�܂��B
  TFMA ��p���邱�ƂŁA�쐬�������f�����ʂ̃f�[�^�ɑ΂��ĕ��U�������s���A�w�K���ɒ�`�������̂Ƃ��Ȃ��w�W�ŕ]�����邱�Ƃ��ł��܂��B
  �����̎w�W���f�[�^�̈قȂ�X���C�X�ɑ΂��Čv�Z���AJupyter notebook ��p���ĉ����ł��܂��B

- [**TensorFlow Metadata (TFMD)**](https://github.com/tensorflow/metadata) ��
  �@�B�w�K���f���� TensorFlow �Ŋw�K������Ƃ��ɖ𗧂��^�f�[�^�ɂ��Ă̕W���I�ȕ\���`����񋟂��܂��B
  ���^�f�[�^�͎蓮�ō쐬���邱�Ƃ��A���̓f�[�^�̉�͂�ʂ��Ď����I�ɐ�������邱�Ƃ�����ł��傤�B
  �܂��A�f�[�^�̌��؁A�T���A�ό`�Ɏg���邩������܂���B
  ���^�f�[�^�̃V���A���C�Y�`���͎��̂��̂��܂݂܂��B

    * �\�`���̃f�[�^�ɑ΂���X�L�[�}�̋L�q (���Ƃ��� tf.Example)
    * �f�[�^�Z�b�g�S�̂ɑ΂���v�񓝌v�ʂ̈ꎮ

- [**ML Metadata (MLMD)**](mlmd.md) �͋@�B�w�K�f�x���b�p�[�ƃf�[�^�T�C�G���e�B�X�g�̃��[�N�t���[�Ɋ֌W���郁�^�f�[�^���L�^�E�������邽�߂̃��C�u�����ł��B
  ��T�̏ꍇ�A���^�f�[�^�� TFMD �̕\���𗘗p���܂��B
  MLMD �� [SQL-Lite](https://www.sqlite.org/index.html) �� [MySQL](https://www.mysql.com/)�A���̑��̗ގ������i���I�ȃf�[�^�X�g�A�̊Ǘ����s���܂��B

### TFX ���x����Z�p

#### �K�{�Ȃ���

- [**Apache Beam**](beam.md) �̓I�[�v���\�[�X�ŁA�o�b�`�����ƃX�g���[�~���O�����̗����ɑ΂�����I�ȃf�[�^���񏈗��p�C�v���C���̃��f���ƂȂ���̂ł��B
  TFX �� Beam ���f�[�^����ȃp�C�v���C�����������邽�߂ɗ��p���Ă��܂��B
  �p�C�v���C���� Beam ���T�|�[�g���镪�U������Ղ��o�b�N�G���h�ɗ��p���ē��삵�܂��B
  �T�|�[�g���镪�U������Ղɂ� Apache Flink, Google Cloud Dataflow �Ȃǂ��܂܂�܂��B

#### �I�v�V����

Apache Airflow, Kubeflow �̂悤�ȃI�[�P�X�g���[�^�[�͋@�B�w�K�p�C�v���C���̐ݒ�A�I�y���[�V�����A�Ď��A�����e�i���X�����ȈՂɂ��܂��B

- [**Apache Airflow**](orchestra.md) �̓��[�N�t���[���v���O�����ŋL�q���A���[�N�t���[�̃X�P�W���[�����O�A�Ď����s���v���b�g�t�H�[���ł��B
  TFX �� Airflow �����[�N�t���[���^�X�N�̗L���񏄉�O���t (directed acyclic graphs: DAGs) �ŏ����\�����߂ɗ��p���Ă��܂��B
  Airflow �̃X�P�W���[���[�͎w�肳�ꂽ�ˑ��֌W�ɂ��������āA���[�J�[��Ń^�X�N�����s���Ă����܂��B
  �L�x�ȃR�}���h���C�����[�e�B���e�B�� DAG �̕��G�� "��p" ���ȒP�Ɏ��s�ł���悤�ɂ��܂��B
  ���b�`�ȃ��[�U�[�C���^�[�t�F�C�X�̓p�C�v���C���̃v���_�N�V�������ł̎��s�󋵂̉����A�i�s�󋵂̊Ď��A�܂���肪���������Ƃ��̃g���u���V���[�e�B���O��e�Ղɂ��܂��B
  ���[�N�t���[���R�[�h�Œ�`����Ă���ꍇ�A�ێ��o�[�W�����Ǘ��A�e�X�g�A�R���{���[�V���������悢���̂ɂȂ�ł��傤�B

- [**Kubeflow**](https://www.kubeflow.org/) �̓V���v���Ń|�[�^�u�����X�P�[���u���ł���A
  Kubernetes ��ł̋@�B�w�K���[�N�t���[�̍쐬�ɓ������Ă��܂��B
  Kubeflow �̖ړI�͂ق��̃T�[�r�X���č쐬���邱�ƂȂ��A�I�[�v���\�[�X�̃x�X�g�E�I�u�E�u���[�h��
  �@�B�w�K�V�X�e���𑽗l�ȃC���t���X�g���N�`����œW�J���邽�߂́A�P���ȕ��@��񋟂��邱�Ƃł��B
  [Kubeflow Pipelines](https://www.kubeflow.org/docs/pipelines/pipelines-overview/)
  �� Kubeflow ��ōČ����̂��郏�[�N�t���[�������� Notebook �x�[�X�̌o���Ɠ������ꂽ�`��
  �\�z�E���s���邱�Ƃ��\�ɂ��܂��B
  Kubernetes ��ɍ\�z���ꂽ Kubeflow Pipeline �ɂ̓z�X�e�B���O���ꂽ���^�f�[�^�X�g�A�A
  �R���e�i�x�[�X�̃I�[�P�X�g���[�V�����G���W���A�m�[�g�u�b�N�T�[�o�[�A�����ă��[�U�[�����G�ȃp�C�v���C����
  �J���A���s�A�Ǘ�����̂������� UI ���܂܂�Ă��܂��B
  Kubeflow Pipeline SDK �̓R���|�[�l���g�̍쐬�⋤�L�A�p�C�v���C���̍\�z���v���O�����Ŏ��s�ł���悤�ɂ��܂��B

### �I�[�P�X�g���[�V�����ƃ|�[�^�r���e�B

TFX �� Apache Airflow �� Kubeflow �Ƃ����������̊���I�[�P�X�g���[�V�����t���[�����[�N�̊Ԃ�
�̈ڐA���������Ȃ�悤�ɐ݌v����Ă��܂��B�܂��A�x�A���^������ Google Cloud Platform (GCP)
�̂悤�ȈقȂ�R���s���[�e�B���O�v���b�g�t�H�[���̊Ԃł��ڐA�\�ł��B

Note: ���݂̃o�[�W�����̃��[�U�[�K�C�h�ł̓x�A���^���V�X�e���̂����A
��� Apache Airflow ���I�[�P�X�g���[�V�����ɗp�����ꍇ�ɂ��ďq�ׂĂ��܂��B

### Model vs. SavedModel

#### Model

���f�� (Model) �͊w�K�v���Z�X�̐��ʕ��ŁA�w�K�v���Z�X��ʂ��ē���ꂽ�d�݂��V���A���C�Y���ꂽ���R�[�h�ł��B
�d�݂͂��̌�A�V���ȓ��͂ɑ΂���\�����v�Z���邽�߂ɗ��p����܂��B
TFX �� TensorFlow �ɂ����āA�u���f���v�͂��鎞�_�Ŋw�K���ꂽ�d�݂��܂ރ`�F�b�N�|�C���g���w���܂��B

�u���f���v�͗\�����ǂ̂悤�ɍs���邩�����\���� TensorFlow �̃R���s���e�[�V�����O���t�̒�`
(�ʂ̌������������ Python �t�@�C��) ���w���ꍇ�����邱�Ƃɒ��ӂ��Ă��������B
����2�̈Ӗ��̂ǂ�����w�����͕����ɉ����ĕς��܂��B

#### SavedModel

- **[SavedModel](https://www.tensorflow.org/api_docs/python/tf/saved_model)�Ƃ�**
  ���ՓI�ŁA����Ɉˑ����Ȃ��A�����ꂽ�A���̏�Ԃɉ񕜉\�� TensorFlow ���f���̃V���A���C�[�[�V�����ł��B
- **�Ȃ��d�v�Ȃ̂�** : SavedModel �͍������ȃV�X�e���ŒP��̒��ۂ𗘗p���āA
  TensorFlow �̃��f�����쐬���A�ό`���A���p���邱�Ƃ��\�ɂ��邽�߂ł��B

SavedModel �� TensorFlow �̃��f���̃V���A���C�[�[�V�����`���ł��B
����̓��f�����v���_�N�V�������ŃT�[�r�X�񋟂���A�܂��͌P���������f�����l�C�e�B�u���o�C���� JavaScript �ŗ��p����ꍇ�ɐ�������܂��B
���Ƃ��΁A���f�����琄�_���ʂ�񋟂��� REST �T�[�r�X���쐬����ꍇ�A���f���� SavedModel ��
�V���A���C�Y���A TensorFlow Serving �ŃT�[�r�X�񋟂ł��܂��B�ڍׂ� [Serving a TensorFlow
Model](https://www.tensorflow.org/serving/tutorials/Serving_REST_simple) �����m�F���������B

### �X�L�[�}

TFX �̃R���|�[�l���g�̂����̂������́A_�X�L�[�}_ �ƌĂ΂����̓f�[�^�ɂ��Ă̋L�q�������܂��B
�X�L�[�}�� [schema.proto](https://github.com/tensorflow/metadata/tree/master/tensorflow_metadata/proto/v0) �̃C���X�^���X�ł��B
�X�L�[�}�� [protocol buffer](https://developers.google.com/protocol-buffers/) �A����ʂɂ� "protobuf" �Ƃ��Ēm���Ă�����̂̈��ł��B
�X�L�[�}�͓����ʂ̃f�[�^�^�A���̓����ʂ��K���܂܂�Ȃ���΂Ȃ�Ȃ����ǂ����A���͒l�̋������͈́A�Ȃǂ̎������w��ł��܂��B
TensorFlow Data Validation (TFDV) �𗘗p���闘�_�̈�́A�^��J�e�S���A���͒l�͈̔͂𐄘_���A
�����I�ɃX�L�[�}�𐄑����Ă���邱�Ƃł��B

schema protobuf ����̔��������Ɏ����܂��B:

```proto
...
feature {
  name: "age"
  value_count {
    min: 1
    max: 1
  }
  type: FLOAT
  presence {
    min_fraction: 1
    min_count: 1
  }
}
feature {
  name: "capital-gain"
  value_count {
    min: 1
    max: 1
  }
  type: FLOAT
  presence {
    min_fraction: 1
    min_count: 1
  }
}
...
```

�X�L�[�}�𗘗p���Ă���R���|�[�l���g�����Ɏ����܂� :

- TensorFlow Data Validation
- TensorFlow Transform

�T�^�I�� TFX �̃p�C�v���C���ł� TensorFlow Data Validation ���X�L�[�}�𐶐����A
�ق��̃R���|�[�l���g�͂���𗘗p���܂��B

Note: �����������ꂽ�X�L�[�}�́u�x�X�g�G�t�H�[�g�v�̂��̂ł���A�P�Ƀf�[�^�̊�{�I�ȓ����̐��������݂���̂ł��B
�������ꂽ�X�L�[�}�ɂ��ẮA�J���҂��m�F���A�K�v�ȏꍇ�͏C���������邱�Ƃ����҂���Ă��܂��B

## TFX ���g�����J��

TFX �͋@�B�w�K�̃v���W�F�N�g�⃊�T�[�`�A�����A���[�J���̃}�V����ł̊J���A�f�v���C���s���܂ł̂��ׂẴt�F�[�Y�ɂ����āA���͂ȃv���b�g�t�H�[����񋟂��܂��B
�R�[�h�̏d��������A[�w�K���ƃT�[�r�X�񋟎��̘c��](#training-serving-skew-detection) �̉\����r�����邽�߂ɁA
�w�K���Ɗw�K�ς݃��f���̃f�v���C���̗����� TFX �̃p�C�v���C�����������A[TensorFlow Transform](tft.md) ���C�u������
�����p���邽�߂� [Transform](transform.md) �R���|�[�l���g���w�K���Ɛ��_���̗����ŗ��p���邱�Ƃ������������܂��B
���̂悤�ɂ��邱�ƂŁA�O�������͂��s������̃R�[�h����т��ė��p���邱�Ƃ��ł��A
�w�K�ɗ��p����f�[�^�ƃv���_�N�V�������Ŋw�K�ς݃��f���ɗ^������f�[�^�̊Ԃō��ق������邱�Ƃ�������܂��B
�܂��A�R�[�h�̋L�q����x�ōς݂܂��B

### �f�[�^�T���A�����A�N���[�j���O

![Data Exploration, Visualization, and Cleaning](wrangling.svg)

TFX �p�C�v���C���͓T�^�I�ɂ� [ExampleGen](examplegen.md) �R���|�[�l���g����n�܂�܂��B
ExampleGen �R���|�[�l���g�͓��͂��ꂽ�f�[�^���󂯕t���A tf.Examples �̌`���ɐ��`���܂��B
����̓f�[�^�Z�b�g���w�K�p�ƕ]���p�ɕ������ꂽ���ƂŎ��s����邱�Ƃ��悭���邽�߁A�w�K�p�ƕ]���p�ɁA2�� ExampleGen �R���|�[�l���g�̃R�s�[�����݂���ꍇ������܂��B
�܂��A��ʓI�ɂ͎��� [StatisticsGen](statsgen.md) �R���|�[�l���g�� [SchemaGen](schemagen.md)
�R���|�[�l���g�������܂��B
�����̃R���|�[�l���g�̓f�[�^���m�F���A�f�[�^�̃X�L�[�}�Ɠ��v�ʂ𐄒肵�܂��B
�X�L�[�}�Ɠ��v�ʂ� [ExampleValidator](exampleval.md) �R���|�[�l���g�ɓ��͂���܂��B
���̃R���|�[�l���g�̓f�[�^�̒��Ɉُ�l�⌇���l�A������f�[�^�^�����݂��Ȃ����������܂��B
�����̃R���|�[�l���g�� [TensorFlow Data Validation](tfdv.md) �̔\�͂����p���Ă��܂��B

[TensorFlow Data Validation (TFDV)](tfdv.md) �̓f�[�^�Z�b�g�̒T���A�����A�N���[�j���O��
�s���ۂɖ��ɗ��c�[���ł��B
TFDV �̓f�[�^���m�F���ăf�[�^�̌^�A�J�e�S���A�l��𐄒肵�A���̌�A�����I�Ɉُ�l�⌇���l����肷��̂��菕�����܂��B
�܂��A�����c�[�����p�ӂ���Ă���A�f�[�^�Z�b�g�̓��e�����ɖ𗧂ł��傤�B
�p�C�v���C���̃R���|�[�l���g�̏����������������ƁA [MLMD](mlmd.md) ���烁�^�f�[�^��ǂݍ��݁A
�f�[�^�𕪐͂��邽�߂� TFDV �̉����c�[���� Jupyter �m�[�g�u�b�N��ŗ��p�ł��܂��B

��x���f�����f�v���C�������Ƃł���΁ATFDV ���f�v���C���ꂽ���f���ւ̐��_���N�G�X�g�Ɋ܂܂��
�V���ȃf�[�^���Ď����A�ُ�l��X���̕ω������o���邽�߂ɗ��p�ł��܂��B
����͎��n��f�[�^�Ńg�����h��G�ߐ�������A���Ԃ̌o�߂ɂ��������ĕω�������̂ɑ΂��Ă͂Ƃ��ɗL���ŁA
�f�[�^�̖��⃂�f����V�����f�[�^�ōĊw�K������K�v������Ƃ��ɁA�ʒm���s���菕���ɂȂ�܂��B

### �f�[�^�̉���

�p�C�v���C���̂����ATFDV �𗘗p����R���|�[�l���g (�T�^�I�ɂ� StatisticsGen, SchemaGen, ExampleValidator) �ł́A�f�[�^�������������ʂ� Jupyter notebook �ŉ����ł��܂��B
�f�[�^�����f����A�v���P�[�V�����ɍœK�������܂ŉ��x�����s���Č��ʂ��r���A�������s�����Ƃ��\�ł��B

�����̃R���|�[�l���g�̏o�͌��ʂ� [**ML Metadata (MLMD)**](mlmd.md) �ɃN�G���𔭍s���Ď擾�������� notebook �ŉ������邽�߂ɁA TFDV �̉������T�|�[�g���� API �𗘗p�ł��܂��B
����ɂ� [tfdv.load_statistics()](`tfdv.load_statistics`) �� [tfdv.visualize_statistics()](`tfdv.visualize_statistics`) ���܂܂�܂��B
�����̉����𗘗p���邱�ƂŁA�f�[�^�Z�b�g�̓����ɂ��Ă��悢�����𓾂邱�Ƃ�A�����K�v�ȏꍇ�͗v���ɂ����ďC�����邱�Ƃ��ł��܂��B

### ���f���̊J���Ɗw�K

![Feature Engineering](feature_eng.svg)

�T�^�I�� TFX �p�C�v���C���� [Transform](transform.md) �R���|�[�l���g���܂݂܂��B
����� [TensorFlow Transform (TFT)](tft.md) ���C�u���������p���ē����ʃG���W�j�A�����O���s���܂��B
Transform �R���|�[�l���g�� SchemaGen �R���|�[�l���g�̍쐬�����X�L�[�}����͂Ƃ��A[data transformations](https://www.tensorflow.org/tfx/transform/api_docs/python/tft) ��K�p���ă��f���̊w�K�ɗ��p��������ʂ̍쐬�A�g�ݍ��킹�A�ϊ����s���܂��B
�����l�̏�����^�̕ϊ��ɂ��Ă��A����炪���_���̃��N�G�X�g�ɂ��܂܂��\���̂���ꍇ�A Transform �R���|�[�l���g�Ŏ��s���ׂ��ł��B
TensorFlow �̃R�[�h�� TFX �Ŋw�K������悤�݌v����Ƃ��ɂ�[�������d�v�Ȍ�������������܂��B](train.md)

![Modeling and Training](train.svg)

Transform �R���|�[�l���g�� SavedModel �𐶐����܂��B
����� [Trainer](trainer.md) �R���|�[�l���g�̒��� TensorFlow �ɃC���|�[�g����A���f�����L�q����R�[�h�ŗ��p����܂��B
���� SavedModel �ɂ� Transform �R���|�[�l���g�̍쐬�����A�f�[�^�G���W�j�A�����O�ōs���ϊ������ׂĊ܂܂�Ă��܂��B
���̂��߁A�w�K���Ɛ��_���ł܂��������Ȃ��R�[�h��p��������̕ϊ����Ȃ���܂��B
Transform �R���|�[�l���g�Ő������ꂽ SavedModel ���܂ށA���f�����L�q����R�[�h�𗘗p���邱�ƂŁA�w�K�p�ƕ]���p�A�����̃f�[�^�𗘗p���A���f���̌P�����ł���悤�ɂȂ�܂��B

���f�����L�q����R�[�h�̍Ō�̃Z�N�V�����ŁA���f���� SavedModel �� EvalSavedModel �̗����̌`���ŕۑ����ׂ��ł��B EvalSavedModel �`���ŕۑ����邽�߂ɂ� Trainer �R���|�[�l���g�� [TensorFlow Model Analysis (TFMA)](tfma.md) ���C�u�������C���|�[�g���ēK�p���邱�Ƃ��K�v�ɂȂ�ł��傤�B

```python
import tensorflow_model_analysis as tfma
...

tfma.export.export_eval_savedmodel(
        estimator=estimator,
        export_dir_base=eval_model_dir,
        eval_input_receiver_fn=receiver_fn)
```

### ���f���̐U�镑���̕��͂Ɨ���

![Model Analysis](analysis.svg)

���f���̊J�����n�ߊw�K������ꍇ�A���f���̐U�镑���ɂ��ĕ��͂��A�^�ɗ������邱�Ƃ͋ɂ߂ďd�v�ł��B
�T�^�I�� TFX �p�C�v���C���� [Evaluator](evaluator.md) �R���|�[�l���g���܂݂܂��B
���̃R���|�[�l���g�͊J���̂��̃t�F�[�Y�ɂ����鋭�͂ȃc�[���Z�b�g��񋟂��� [TensorFlow Model Analysis (TFMA)](tfma.md) ���C�u�����̔\�͂����p���܂��B
Evaluator �R���|�[�l���g�͕ۑ����� EvalSavedModel ����͂Ƃ��Ď󂯕t���܂��B�܂��A���f���̐U�镑�������������͂���ۂɗ��p���� `SliceSpecs` �̃��X�g���w��ł��܂��B
���ꂼ��� SliceSpec �͊w�K�f�[�^���́A�J�e�S���J���ȓ����ʂɂ��������̃J�e�S���A���l�I�ȓ����ʂɂ��������̒l��Ƃ������A�m�F�������w�K�f�[�^�̐؂�����`���܂��B

���Ƃ��΁A�N�ԍw�����z��n��f�[�^�A�N��w�A���ʂƂ������قȂ�Z�O�����g�̌ڋq�ɑ΂��郂�f���̐U�镑���𗝉����悤�Ǝ��݂邱�Ƃ͏d�v�ɂȂ肦��ł��傤�B
�f�[�^�Z�b�g�������O�e�[���ȕ��z������ꍇ�ɁA����͂Ƃ��ɏd�v�ɂȂ肦�܂��B�����ł��d�v�ȃO���[�v�ɑ΂���e�F�ł��Ȃ��U�镑�����A�����h�ɑ΂���U�镑���ɂ���ĕ����B����Ă��܂��ꍇ�����邽�߂ł��B
���Ƃ��΁A���f�������ϓI�ȏ]�ƈ��ɑ΂��Ă͂��܂��@�\������̂́A��Ƃ̊����ɑ΂��Ă͖{���ɂЂǂ��߂���Ƃ��悤�ȏꍇ�A�����m���Ă������Ƃ͏d�v�ɂȂ邩������܂���B

### ���f���̕��͂Ɖ���

���f���̊w�K���I���A�w�K���ʂ� [Evaluator](evaluator.md) �R���|�[�l���g (����� [TFMA](tfma.md) �����p���Ă��܂�) �ɓ��͂��ď����������������ƁA���ʂ� Jupyter �X�^�C���̃m�[�g�u�b�N�ŉ����ł��܂��B
2��ڈȍ~�ł���΁A����܂ł̌��ʂ��r���āA���ʂ����f���ƃA�v���P�[�V�����ɂƂ��čœK�������܂ŉ��x�������ł��܂��B

�m�[�g�u�b�N��ŉ������s�����߂ɂ́A�܂�[**ML Metadata (MLMD)**](mlmd.md) �ɃN�G���𔭍s���A�R���|�[�l���g�Q�̎��s���ʂ��擾���܂��B
���ɁA TFMA �̉����p API �𗘗p����ƌ��ʂ̉������ł��܂��B
�����p API �ɂ� [tfma.load_eval_results()](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/load_eval_results)�� [tfma.view.render_slicing_metrics()](`tfma/view/render_slicing_metrics`) ���܂܂�܂��B
�������s�����ƂŃ��f���̓����ɂ��Ă��悢�����𓾂邱�Ƃ��ł��A�K�v�ȏꍇ�ɂ͏C�����ł���悤�ɂȂ�ł��傤�B

## �f�v���C�����g�^�[�Q�b�g

���f���̊J���Ɗw�K���I���Ă��̌��ʂɖ������Ă���Ȃ�A���_���N�G�X�g���󂯕t����ꏊ�ł���A1�܂��͕����̃f�v���C�����g�^�[�Q�b�g�Ƀ��f�����f�v���C����^�C�~���O�ł��B
TFX ��3�̃N���X�̃f�v���C�����g�^�[�Q�b�g���T�|�[�g���Ă��܂��B
�w�K�ς݃��f���� SavedModel �Ƃ��ăG�N�X�|�[�g����ƁA�����3�̂����̂ǂꂩ�A�܂��͂��ׂẴf�v���C�����g�^�[�Q�b�g�Ƀ��f�����f�v���C�ł��܂��B

![Component Flow](diag_all.svg)

### ���_: TensorFlow Serving

[TensorFlow Serving (TFS)](serving.md) �̓v���_�N�V�����������ɐ݌v���ꂽ�A�_��Ńn�C�p�t�H�[�}���X�ȋ@�B�w�K���f���̃T�[�r���O�V�X�e���ł��B
����� SavedModel ��ǂݍ��ނƁAREST �� gRPC �C���^�[�t�F�[�X�ł̐��_���N�G�X�g���󂯕t����悤�ɂȂ�܂��B
�܂��A�����̃v���Z�X�𓯊��E���U�����̂��߂̂������̍��x�ȃA�[�L�e�N�`����p���āA1�Ȃ����͕����̃l�b�g���[�N�T�[�o�[��ő��点�܂��B
TFS �̊J����f�v���C�Ɋւ���ڍׂɂ��Ă� [TFS �̃h�L�������g](serving.md)���Q�Ƃ��Ă��������B

�T�^�I�ȃp�C�v���C���ł� [Pusher](pusher.md) �R���|�[�l���g�� Trainer �R���|�[�l���g�ŌP�����ꂽ SavedModel ��ǂݍ��݁ATFS �̃C���t���X�g���N�`���Ƀf�v���C���܂��B
����͕����̃o�[�W�����⃂�f���̃A�b�v�f�[�g�̏������܂݂܂��B

### ���o�C���l�C�e�B�u�� IoT �A�v���P�[�V�����ł̐��_: TensorFlow Lite

[TensorFlow Lite](https://www.tensorflow.org/lite) �͊w�K�ς݂� TensorFlow ���f�����l�C�e�B�u���o�C���� IoT �A�v���P�[�V�����Ŏg�����߂̃c�[���ꎮ���f�x���b�p�[�ɒ񋟂��܂��B
TensorFlow Serving �Ɠ��l�ɁA����� SavedModel ��ǂݍ��݁A�ʎq����}����̂悤�ȍœK����@��p���āA���o�C���� IoT �f�o�C�X�œ��삷��悤�ɃT�C�Y�ƃp�t�H�[�}���X�̍œK�������݂܂��B
TensorFlow Lite �̗��p�ɂ��Ă̏ڍׂ� TensorFlow Lite �̃h�L�������g���Q�Ƃ��Ă��������B

### JavaScript �ł̐��_: TensorFlow JS

[TensorFlow JS](https://js.tensorflow.org/) �͋@�B�w�K���f���̊w�K�ƃf�v���C���u���E�U�� Node.js ��ōs�� JavaScript ���C�u�����ł��B
����� TensorFlow Serving �� TensorFlow Lite �Ɠ��l�� SavedModel ��ǂݍ��݁A����� TensorFlow.js Web �t�H�[�}�b�g�ɕϊ����܂��B
TensorFlow JS �̗��p�ɂ��Ă̏ڍׂ� TensorFlow JS �̃h�L�������g���Q�Ƃ��Ă��������B

## Airflow ��p���� TFX �p�C�v���C���̍쐬

### �C���X�g�[��

Airflow �� PyPI ����C���X�g�[���ł��܂�:

```python
# Airflow
# set this to avoid the GPL version; no functionality difference either way
export SLUGIFY_USES_TEXT_UNIDECODE=yes
pip install apache-airflow
```

### DAG �̍쐬

Python ��p���� TFX �p�C�v���C�����쐬���邽�߂ɂ́A`tfx.runtimes.tfx_airflow.PipelineDecorator` �Ńf�R���[�g���ꂽ�֐����`���āA
�p�C�v���C���ŗ��p����R���|�[�l���g���쐬���A�p�C�v���C���ɍ��킹�Ă������Ȃ����킹��K�v������܂��B
���̌�A�t�@�C���̃O���[�o���R���e�L�X�g�� `create_pipeline()` ���Ăяo���܂��B
���Ƃ��΁A�T�^�I�ȃp�C�v���C���͎��̂悤�ɂȂ�ł��傤 :

```python
@PipelineDecorator(
    pipeline_name='tfx_example_solution',
    schedule_interval=None,
    start_date=datetime.datetime(2018, 1, 1),
    enable_cache=True,
    additional_pipeline_args={'logger_args': logging_utils.LoggerConfig(
        log_root='/var/tmp/tfx/logs', log_level=logging.INFO)},
    metadata_db_root=os.path.join(home_dir, 'data/tfx/metadata'),
    pipeline_root=pipeline_root)
def create_pipeline():
  """Implements the example pipeline with TFX."""
  examples = csv_input(os.path.join(base_dir, 'no_split/span_1'))
  example_gen = CsvExampleGen(input_data=examples)
  statistics_gen = StatisticsGen(input_data=example_gen.outputs.output)
  infer_schema = SchemaGen(stats=statistics_gen.outputs.output)
  validate_stats = ExampleValidator(  # pylint: disable=unused-variable
      stats=statistics_gen.outputs.output,
      schema=infer_schema.outputs.output)
  transform = Transform(
      input_data=example_gen.outputs.output,
      schema=infer_schema.outputs.output,
      module_file=transforms)
  trainer = Trainer(
      module_file=model,
      transformed_examples=transform.outputs.transformed_examples,
      schema=infer_schema.outputs.output,
      transform_output=transform.outputs.transform_output,
      train_steps=10000,
      eval_steps=5000,
      warm_starting=True)
  model_analyzer = Evaluator(
      examples=example_gen.outputs.output,
      model_exports=trainer.outputs.output)
  model_validator = ModelValidator(
      examples=example_gen.outputs.output,
      model=trainer.outputs.output)
  pusher = Pusher(
      model_export=trainer.outputs.output,
      model_blessing=model_validator.outputs.blessing,
      serving_model_dir=serving_model_dir)

  return [
      example_gen, statistics_gen, infer_schema, validate_stats, transform,
      trainer, model_analyzer, model_validator, pusher
  ]

pipeline = TfxRunner().run(create_pipeline())
```

### Airflow ��p����ꍇ�� TFX �p�C�v���C���̏�����

[Apache Airflow](orchestra.md) �̃C���X�g�[���̍ۂɁA�p�C�v���C�����쐬����� `$AIRFLOW_HOME` �f�B���N�g�� (�f�t�H���g�ł� `~/airflow`) ������������܂��B
������A�p�C�v���C���̃R�[�h��ێ����邽�߂̃f�B���N�g�����쐬����K�v������܂�:

```bash
mkdir -p ~/airflow/dags     # or $AIRFLOW_HOME/dags
mkdir -p ~/airflow/data     # or $AIRFLOW_HOME/data
mkdir -p ~/airflow/plugins  # or $AIRFLOW_HOME/plugins
```

#### �p�C�v���C���̐ݒ�

���ۂ̃R�[�h�̍\���ɑ΂���B��̗v���́A`create_pipeline()` �֐� (����� "�p�C�v���C���̐ݒ�" ���̂��̂ł�) ���L���ꂽ Python �t�@�C���� `dags` �t�H���_�z���ɒu����Ă��Ȃ���΂����Ȃ��A�Ƃ������̂ł��B
Python �t�@�C���̖��O�� DAG �̖��O�ƈ�v�����邱�Ƃ𐄏����܂��BDAG �� `taxi` �Ƃ������O�̂Ƃ��ɂ́A���̃t�@�C������ `taxi` �Ƃ��ׂ��ł��B

�p�C�v���C���̐ݒ�t�@�C������ `create_pipeline()` �֐��� `PipelineDecorator` �Ńf�R���[�g����A`pipeline_name` �Ȃǂ̒l���ݒ肳��܂��B
������ Airflow �� web UI ��p���ăp�C�v���C���𖼑O�Ŏ��ʂ���ۂ�A�p�C�v���C���̃��O�t�@�C����z�u����ۂɏd�v�ƂȂ�܂��B

#### �p�C�v���C���̃R�[�h�̃f�v���C

��L�̃Z�N�V�����ŋL�q���Ă���悤�Ƀp�C�v���C���̐ݒ�t�@�C����z�u���A�t�@�C������ύX���܂��B

`data` �t�H���_�[�� `plugins` �t�H���_�[�z���ɐV�����t�H���_�[���쐬���p�C�v���C���̃R�[�h��z�u���邱�ƂŁA�p�C�v���C���R�[�h�̎c��̃R�[�h���f�v���C���܂��傤�B
�����̏o�͐�t�H���_�[�̖��O���p�C�v���C���Őݒ肵�����O (`PipelineDecorator` �Őݒ肵������) �ƈ�v�����邱�Ƃ̓O�b�h�v���N�e�B�X�ł��B
���Ƃ��΁A�p�C�v���C���̖��O�� `taxi` �̂Ƃ��A�o�̓t�H���_�[�̖��O�͎��̂悤�ɂȂ�܂�:

```bash
mkdir -p ~/airflow/data/taxi     # or $AIRFLOW_HOME/data/taxi
mkdir -p ~/airflow/plugins/taxi  # or $AIRFLOW_HOME/plugins/taxi

```

```python
home_dir = os.path.join(os.environ['HOME'], 'airflow/')
base_dir = os.path.join(home_dir, 'data/taxi/')
output_dir = os.path.join(base_dir, 'pipelines/')
```

�f�[�^�Z�b�g���t�@�C���Ƃ��ĕۑ������p����ꍇ�A `data` �t�H���_�[�z���Ƀt�@�C�����R�s�[���ׂ��ł�:

```bash
cp data.csv ~/airflow/data/taxi     # or $AIRFLOW_HOME/data/taxi
```

### �T���v���R�[�h

���K�I�ɁA�p�C�v���C���̐ݒ�̋L�q�ɂ̓p�C�v���C���̐ݒ�ɕK�v�ȍŏ����̃R�[�h�݂̂��܂ނׂ��ł��B[����͂��̂悤�ȃR�[�h�̃T���v���ł�](https://github.com/tensorflow/tfx/blob/master/tfx/examples/chicago_taxi_pipeline/taxi_pipeline_simple.py)�B

�R�[�h�ŌĂяo���Ă���ATensorFlow �̃��f���� Transform �� `preprocessing_fn` �Ȃǂ̏����̋L�q�͂��ׂĒP��̃t�@�C���Ɋ܂߂�ׂ��ł��B
[����͂��̂悤�ȃR�[�h�̃T���v���ł�](https://github.com/tensorflow/tfx/blob/master/tfx/examples/chicago_taxi_pipeline/taxi_utils.py)�B

## TFX �p�C�v���C���̃f�v���C�ƃI�y���[�V����

�V�����p�C�v���C���̏������J�n�����邽�߂ɂ� Airflow �� web UI �Ńp�C�v���C����L���ɂ��Ȃ���΂����܂���B
�����̏ꍇ�Aweb UI ���珈�����J�n����K�v������ł��傤�B
�������s���~�߂����ꍇ�́A�p�C�v���C���𖳌��ɂ��邱�Ƃ� web UI ����\�ł��B
�܂��A�p�C�v���C���̌��݂̏�Ԃ�A�ߋ��̗����̊m�F�A���O�̉{���� web UI �ŉ\�ł��B

### �p�C�v���C���̊J�n�ƍX�V

�����p�C�v���C�����܂����s���Ă��Ȃ��ꍇ�A Airflow ���R�}���h���C��������s����K�v������܂�:

```bash
airflow webserver -p 8080
airflow scheduler
```

#### �R�[�h�̍X�V

�p�C�v���C���̃f�v���C���s�������Ƃł��A�p�C�v���C���̃R�[�h�ɕύX�������邱�Ƃ��ł��܂��B
�ύX���������ꍇ�A Airflow �����t���b�V�����s�����̃^�C�~���O (�f�t�H���g��1���ł�) �܂ő҂��AAirflow �� web UI �y�[�W���X�V���ĕύX���m�F����K�v������܂��B
�p�C�v���C���� `pipeline_name` ��ύX�����ꍇ�ɂ́A�Â����O���c�邩������܂��񂪁A���̂��� "missing" (�s���s��) �ƕ\�������悤�ɂȂ�܂��B

#### �m�[�g�u�b�N��p��������

�p�C�v���C���Ɋ܂܂�� TFX �̃R���|�[�l���g�̓��͂Əo�͂𒲂ׁA���s���ʂ̔�r���s�����߂ɁAJupyter �X�^�C���̃m�[�g�u�b�N�͂ƂĂ��L�p�ȃc�[���ł��B
�����āATFDV �� TFMA �͂ǂ�������͂ȉ����̃T�|�[�g������Ă���A�J���҂��f�[�^�Z�b�g��T�����A���f���̏o�͌��ʂ��ڍׂɉ�͂ł���悤�ɂȂ��Ă��܂��B

## �g���u���V���[�e�B���O

### Log �t�@�C�����̃G���[�̒T����

TFX �̓��O�� PipelineDecotator �̒ǉ��̈����ł��� LoggerConfig �Őݒ肳�ꂽ�ꏊ�ɏo�͂��܂��B
�f�t�H���g�� `/var/tmp/tfx/logs/tfx.log` �ł��B
�����āA�I�[�P�X�g���[�^�[ (���Ƃ��� Airflow �� Kubeflow) ���܂����O�t�@�C�����o�͂��܂��B
�p�C�v���C���̃G���[�̕��͂����݂�Ƃ��ɂ́A�����̃��O�t�@�C�����ƂĂ��L���ł��B
`taxi` �Ƃ������O�̃p�C�v���C���œ��� LoggerConfig ���ݒ肳��Ă��Ȃ��ꍇ�ATFX �̃��O�� `/var/tmp/tfx/logs/tfx.log` �ɏo�͂���܂��B
����� [logging_utils.LoggerConfig](https://github.com/tensorflow/tfx/blob/master/tfx/utils/logging_utils.py) �I�u�W�F�N�g�𐶐����A�p�C�v���C���̐ݒ�� `logger_args` �ƌĂ΂��p�����[�^�ɗ^���邱�ƂŁA�ݒ�̕ύX���\�ł��B

```python
@PipelineDecorator(
    pipeline_name='tfx_example_solution',
    schedule_interval=None,
    start_date=datetime.datetime(2018, 1, 1),
    enable_cache=True,
    additional_pipeline_args={'logger_args': logging_utils.LoggerConfig(
        log_root='/var/tmp/tfx/logs', log_level=logging.INFO)},
    metadata_db_root=os.path.join(home_dir, 'data/tfx/metadata'),
    pipeline_root=pipeline_root)
```

Note: Docker �� Kubeflow �̃����[�g����� Executor �𓮂����Ă���ꍇ�AExecutor �̃��O�̓����[�g���[�J�[��ɏo�͂���܂��B

Airflow �𗘗p���Ă���ꍇ�A���O�� Airflow ���o�͂��郍�O�ɂ��L�^����܂��B
�f�t�H���g�� Airflow �̃��O�̏o�͐�� `$AIRFLOW_HOME/logs` �ŁA���̃t�@�C�����܂܂�܂�:

```
$AIRFLOW_HOME/logs/scheduler/{DATE}/taxi.py.log
$AIRFLOW_HOME/logs/scheduler/latest/taxi.py.log
$AIRFLOW_HOME/logs/taxi
$AIRFLOW_HOME/logs/taxi.COMPONENT_NAME
```

### �p�C�v���C���͕\������Ă��邪�AAirflow �Ŏ��s���悤�Ƃ���Ƃ݂���Ȃ�

�E�F�u�T�[�o�[�ƃX�P�W���[���[���ċN�����Ă݂Ă��������B

## Kubeflow ��p���� TFX �p�C�v���C���̍쐬

### �Z�b�g�A�b�v

Kubeflow �̓p�C�v���C�����K�͂Ɏ��s���邽�߂� Kubernetes �N���X�^��K�v�Ƃ��܂��B
Kubeflow �̃f�v���C���s�����߂̈�A�̎���ɂ��Ă͎��̃f�v���C�����g�K�C�h���C�����Q�Ƃ��Ă������� ([deplopying the Kubeflow cluster.](https://www.kubeflow.org/docs/started/getting-started-gke/))

### TFX �p�C�v���C���̐ݒ�Ǝ��s

Kubeflow ��� TFX �̃T���v���p�C�v���C�������s���邽�߂ɂ� Kubeflow �p�C�v���C����[�菇��](https://github.com/kubeflow/pipelines/tree/master/samples/tfx-oss)�ɂ��������Ă��������B
TFX �R���|�[�l���g�� Kubeflow pipeline ���\�z���邽�߂ɃR���e�i������Ă��܂��B
�܂��A�T���v���͑�K�͂ȃp�u���b�N�̃f�[�^�Z�b�g��ǂݍ��݁A�w�K���s���āA�N���E�h��ő�K�͂Ƀf�[�^����������X�e�b�v��������Ă��܂��B
