#  RNN �͌^

TensorFlow Lite ����ڑO������ TensorFlow ����B�R���ߍ�㞎��I����C�����͌^�˕s�\������B

�ꍱ� RNN �I�ˏ���󓞘���v�I�e�B���񕶞��T�q���ڑO�I��C��񋟗� RNN �͌^�I�����B

## �ڑO�x���I

�ڑO�C���v�v�L�w�� `sequence_length`�C�A�Ȑ����g�p[`tf.nn.static_rnn`](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn) �I RNN �͌^�B

���� `tf.nn.rnn_cell` ����g�p `tf.nn.static_rnn`:

*   [tf.nn.rnn_cell.LSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/LSTMCell)
*   [tf.nn.rnn_cell.RNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/RNNCell)
*   [tf.nn.rnn_cell.GRUCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/GRUCell)
*   [tf.nn.rnn_cell.BasicLSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/BasicLSTMCell)
*   [tf.nn.rnn_cell.BasicRNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/BasicRNNCell)

�O�CTensorFlow Lite �񋟗��ꍱ RNN ����I�֑���@�B�����@�g�ȍ� TensorFlow Lite ���g�p RNN �ˁB

�p�I�֑���@�@���F

*   [tf.nn.dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)
*   [tf.nn.bidirectional_dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/bidirectional_dynamic_rnn)
*   [tf.nn.rnn_cell.RNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/RNNCell)
*   [tf.nn.rnn_cell.LSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/LSTMCell)

## �s�x���I

TensorFlow Lite �ڑO�s�x�� [Control Flow](https://www.tensorflow.org/api_docs/cc/group/control-flow-ops) ����B�\���C����g�p�������񓞓I�����C�ێg�p���� TensorFlow �����I�͌^���s�\�퐬���F

*   [tf.nn.static_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn) ���w���� `sequence_length`
*   [tf.nn.dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)
*   [tf.nn.bidirectional_dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/bidirectional_dynamic_rnn)

���ӁFTensorFlow Lite �� 2019 �N��O���L�K�I Control Flow ����B�́C���L�I RNN �ˏ��Ȕ퐬���B

## ����

�������g�p����q�����I RNN �͌^�C���v�C�����I�˛󊎏d�V�B����������s�I�F

### 1. �d

�@�ʉ\�C�œI�������d�͌^�ˁC�g�p�s�L `sequence_length` �I [tf.nn.static_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn)�B

### 2. �g�p����񎦘a�Z������I�֑���@

TensorFlow Lite  RNN ����񋟗��ꍱ�֑���@�C�g���� TensorFlow Lite ���Ȏg�p RNN �ˁB�g�p [OpHints](https://www.tensorflow.org/lite/guide/ops_custom#converting_tensorflow_models_to_convert_graphs)�C�����@�݉Ȑ���s�C�A�� TensorFlow Lite ���풆�s�C����֓���I�Z������B

���񐥉p�I�֑���@�F

*   [tf.lite.experimental.nn.dynamic_rnn](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn.py#L41)
    *   �֑� tf.nn.dynamic_rnn
*   [tf.lite.experimental.nn.bidirectional_dynamic_rnn](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn.py#L279)
    *   �֑� tf.nn.bidirectional_dynamic_rnn
*   [tf.lite.experimental.nn.TfLiteRNNCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn_cell.py#L39)
    *   �֑� tf.nn.rnn_cell.RNNCell
*   [tf.lite.experimental.nn.TfLiteLSTMCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn_cell.py#L159)
    *   �֑� tf.nn.rnn_cell.LSTMCell


���ӁF���֑���@�K��N�g�p�B��@�C�@�ʐ��ݎg�p `tf.lite.experimental.nn.dynamic_rnn`�C�K�����a `tf.lite.experimental.nn.TfLiteRNNCell` �z���g�p�C���s���g�p `tf.nn.rnn_cell.RNNCell`�B


�g�p[tf.keras.layers.StackedRNNCells](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells) ���� [tf.nn.rnn_cell.MultiRNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/MultiRNNCell)�B


[TensorFlow Lite LSTM ops API](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/g3doc/README.md) �񋟗��g�p���֑���@�I�����B

�L�I Colab �����C�ȎQ [TensorFlowLite_LSTM_Keras_Tutorial](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/TensorFlowLite_LSTM_Keras_Tutorial.ipynb)�B

���ӁF�� [tf.nn.rnn_cell.GRUCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/GRUCell)�C�v�L�֑�I���@�B