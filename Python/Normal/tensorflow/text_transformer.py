'''
------------------------------------------------------------------------------------------
text
    Transformer model for language understanding

This tutorial trains a Transformer model to translate Portuguese to English. 
This is an advanced example that assumes knowledge of text generation and attention.

The core idea behind the Transformer model is self-attention—the ability to 
attend to different positions of the input sequence to compute a representation of that sequence. 
Transformer creates stacks of self-attention layers 
and is explained below in the sections Scaled dot product attention and Multi-head attention.

A transformer model handles variable-sized input using stacks of self-attention layers instead of RNNs or CNNs. 
This general architecture has a number of advantages:

	* It make no assumptions about the temporal/spatial relationships across the data. 
		This is ideal for processing a set of objects (for example, StarCraft units).
	* Layer outputs can be calculated in parallel, instead of a series like an RNN.
	* Distant items can affect each other's output without passing through many RNN-steps, 
		or convolution layers (see Scene Memory Transformer for example).
	* It can learn long-range dependencies. This is a challenge in many sequence tasks.
	
The downsides of this architecture are:

	* For a time-series, 
		the output for a time-step is calculated from the entire history instead of only the inputs and current hidden-state. 
		This may be less efficient.
	* If the input does have a temporal/spatial relationship, like text, 
		some positional encoding must be added or the model will effectively see a bag of words.
	
After training the model in this notebook, you will be able to input a Portuguese sentence and return the English translation.
------------------------------------------------------------------------------------------
'''
# common library
from __future__ import absolute_import, division, print_function, unicode_literals

import re
import os
import json
import time
import pprint
import contextlib
from pathlib import Path
from PIL import Image

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import tensorflow as tf
import tensorflow_datasets as tfds

print(__doc__)

AUTOTUNE = tf.data.experimental.AUTOTUNE

# Display current path
basic_path = Path.cwd()
PROJECT_ROOT_DIR = basic_path.joinpath('Python', 'Normal', 'tensorflow')
print('PROJECT_ROOT_DIR = \n{0}\n'.format(PROJECT_ROOT_DIR))

# Display tensorflow version
print("TensorFlow version: ", tf.version.VERSION)

im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'attention_map_portuguese.png'))
im.show()

print   (
        '---------------------------------------------------------------------------------\n'
        '      Setup input pipeline                                                       \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Use TFDS to load the Portugese-English translation dataset from the TED Talks Open Translation Project.

This dataset contains approximately 50000 training examples, 1100 validation examples, and 2000 test examples.
------------------------------------------------------------------------------------------
'''
name_path = os.path.join('ted_hrlr_translate', 'pt_to_en')

examples, metadata = tfds.load(
                        name=name_path,
                        with_info=True,
                        as_supervised=True
                    )

train_examples, val_examples = examples['train'], examples['validation']

'''
-----------------------------------------------------------------------------------------
Create a custom subwords tokenizer from the training dataset.
-----------------------------------------------------------------------------------------
'''

tokenizer_en = tfds.features.text.SubwordTextEncoder.build_from_corpus(
					(en.numpy() for pt, en in train_examples), 
					target_vocab_size=2**13
				)

tokenizer_pt = tfds.features.text.SubwordTextEncoder.build_from_corpus(
					(pt.numpy() for pt, 
					en in train_examples), 
					target_vocab_size=2**13
				)

sample_string = 'Transformer is awesome.'

tokenized_string = tokenizer_en.encode(sample_string)
print ('Tokenized string is {}\n'.format(tokenized_string))

original_string = tokenizer_en.decode(tokenized_string)
print ('The original string: {}\n\n'.format(original_string))

assert original_string == sample_string

'''
-----------------------------------------------------------------------------------------
The tokenizer encodes the string by breaking it into subwords 
if the word is not in its dictionary.
-----------------------------------------------------------------------------------------
'''
for ts in tokenized_string:
	print ('{} ----> {}'.format(ts, tokenizer_en.decode([ts])))

BUFFER_SIZE = 20000
BATCH_SIZE = 64

'''
-----------------------------------------------------------------------------------------
Add a start and end token to the input and target.
-----------------------------------------------------------------------------------------
'''
def encode(lang1, lang2):
	lang1 = [tokenizer_pt.vocab_size] + tokenizer_pt.encode(
	lang1.numpy()) + [tokenizer_pt.vocab_size+1]

	lang2 = [tokenizer_en.vocab_size] + tokenizer_en.encode(
		lang2.numpy()) + [tokenizer_en.vocab_size+1]

	return lang1, lang2

'''
----------------------------------------------------------------------------------------
Note: 
To keep this example small and relatively fast, drop examples with a length of over 40 tokens.
----------------------------------------------------------------------------------------
'''
MAX_LENGTH = 40

def filter_max_length(x, y, max_length=MAX_LENGTH):
	return tf.logical_and(
							tf.size(x) <= max_length,
							tf.size(y) <= max_length
						)

'''
-----------------------------------------------------------------------------------------
Operations inside .map() run in graph mode and receive a graph tensor that do not have a numpy attribute. 
The tokenizer expects a string or Unicode symbol to encode it into integers. 
Hence, you need to run the encoding inside a tf.py_function, 
which receives an eager tensor having a numpy attribute that contains the string value.
----------------------------------------------------------------------------------------
'''
def tf_encode(pt, en):
	return tf.py_function(encode, [pt, en], [tf.int64, tf.int64])

train_dataset = train_examples.map(tf_encode)
train_dataset = train_dataset.filter(filter_max_length)
# cache the dataset to memory to get a speedup while reading from it.
train_dataset = train_dataset.cache()
train_dataset = train_dataset.shuffle(BUFFER_SIZE).padded_batch(
					BATCH_SIZE, 
					padded_shapes=([-1], [-1])
				)

train_dataset = train_dataset.prefetch(tf.data.experimental.AUTOTUNE)


val_dataset = val_examples.map(tf_encode)
val_dataset = val_dataset.filter(filter_max_length).padded_batch(
    BATCH_SIZE, padded_shapes=([-1], [-1]))

pt_batch, en_batch = next(iter(val_dataset))

print('pt_batch = \n{0},\n en_batch = \n{1}\n'.format(pt_batch, en_batch))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Positional encoding                                                        \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-------------------------------------------------------------------------------------------
Since this model doesn't contain any recurrence or convolution, positional encoding is added to give the model some information about the relative position of the words in the sentence.

The positional encoding vector is added to the embedding vector. Embeddings represent a token in a d-dimensional space where tokens with similar meaning will be closer to each other. 
But the embeddings do not encode the relative position of words in a sentence. 
So after adding the positional encoding, words will be closer to each other based on the similarity of their meaning and their position in the sentence, in the d-dimensional space.

See the notebook on positional encoding to learn more about it. The formula for calculating the positional encoding is as follows:
--------------------------------------------------------------------------------------------
'''
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'positional_encording.jpg'))
im.show()

def get_angles(pos, i, d_model):
	angle_rates = 1 / np.power(10000, (2 * (i//2)) / np.float32(d_model))
	return pos * angle_rates

def positional_encoding(position, d_model):
	angle_rads = get_angles(
					np.arange(position)[:, np.newaxis],
					np.arange(d_model)[np.newaxis, :],
					d_model
				)
	
	# apply sin to even indices in the array; 2i
	angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
	
	# apply cos to odd indices in the array; 2i+1
	angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
	
	pos_encoding = angle_rads[np.newaxis, ...]
	
	return tf.cast(pos_encoding, dtype=tf.float32)

pos_encoding = positional_encoding(50, 512)
print ('pos_encoding.shape = {0}\n'.format(pos_encoding.shape))

plt.pcolormesh(pos_encoding[0], cmap='RdBu')
plt.xlabel('Depth')
plt.xlim((0, 512))
plt.ylabel('Position')
plt.colorbar()
plt.show()

print   (
        '---------------------------------------------------------------------------------\n'
        '      Masking                                                                    \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
Mask all the pad tokens in the batch of sequence. It ensures that the model does not treat padding as the input. 
The mask indicates where pad value 0 is present: it outputs a 1 at those locations, and a 0 otherwise.
-----------------------------------------------------------------------------------------
'''
def create_padding_mask(seq):
	seq = tf.cast(tf.math.equal(seq, 0), tf.float32)
	
	# add extra dimensions to add the padding
	# to the attention logits.
	return seq[:, tf.newaxis, tf.newaxis, :]  # (batch_size, 1, 1, seq_len)

x = tf.constant([[7, 6, 0, 0, 1], [1, 2, 3, 0, 0], [0, 0, 0, 4, 5]])

print('create_padding_mask(x) = \n{0}\n'.format(create_padding_mask(x)))

'''
-----------------------------------------------------------------------------------------
The look-ahead mask is used to mask the future tokens in a sequence. 
In other words, the mask indicates which entries should not be used.

This means that to predict the third word, only the first and second word will be used. 
Similarly to predict the fourth word, only the first, second and the third word will be used and so on.
----------------------------------------------------------------------------------------
'''
def create_look_ahead_mask(size):
	mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
	return mask  # (seq_len, seq_len)

x = tf.random.uniform((1, 3))
temp = create_look_ahead_mask(x.shape[1])

print('temp = \n{0}\n'.format(temp))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Scaled dot product attention                                               \n'
        '---------------------------------------------------------------------------------\n'
        )
im = Image.open(PROJECT_ROOT_DIR.joinpath('images/scaled_attention.png'))
im.show()

'''
------------------------------------------------------------------------------------------
The attention function used by the transformer takes three inputs: Q (query), K (key), V (value). 
The equation used to calculate the attention weights is:
-----------------------------------------------------------------------------------------
'''
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'attention_equation_01.jpg'))
im.show()

'''
----------------------------------------------------------------------------------------
The dot-product attention is scaled by a factor of square root of the depth. 
This is done because for large values of depth, 
the dot product grows large in magnitude pushing the softmax function 
where it has small gradients resulting in a very hard softmax.

For example, consider that Q and K have a mean of 0 and variance of 1. 
Their matrix multiplication will have a mean of 0 and variance of dk. 
Hence, square root of dk is used for scaling (and not any other number) 
because the matmul of Q and K should have a mean of 0 and variance of 1, 
and you get a gentler softmax.

The mask is multiplied with -1e9 (close to negative infinity). 
This is done because the mask is summed with the scaled matrix multiplication of Q 
and K and is applied immediately before a softmax. 
The goal is to zero out these cells, 
and large negative inputs to softmax are near zero in the output.
-----------------------------------------------------------------------------------------
'''
def scaled_dot_product_attention(q, k, v, mask):
	"""Calculate the attention weights.
	q, k, v must have matching leading dimensions.
	k, v must have matching penultimate dimension, i.e.: seq_len_k = seq_len_v.
	The mask has different shapes depending on its type(padding or look ahead) 
	but it must be broadcastable for addition.

	Args:
		q: query shape == (..., seq_len_q, depth)
		k: key shape == (..., seq_len_k, depth)
		v: value shape == (..., seq_len_v, depth_v)
		mask: Float tensor with shape broadcastable 
		to (..., seq_len_q, seq_len_k). Defaults to None.

	Returns:
		output, attention_weights
	"""

	matmul_qk = tf.matmul(q, k, transpose_b=True)  # (..., seq_len_q, seq_len_k)
	
	# scale matmul_qk
	dk = tf.cast(tf.shape(k)[-1], tf.float32)
	scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)

	# add the mask to the scaled tensor.
	if mask is not None:
		scaled_attention_logits += (mask * -1e9)  

	# softmax is normalized on the last axis (seq_len_k) so that the scores
	# add up to 1.
	attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)  # (..., seq_len_q, seq_len_k)

	output = tf.matmul(attention_weights, v)  # (..., seq_len_q, depth_v)

	return output, attention_weights

'''
-----------------------------------------------------------------------------------
As the softmax normalization is done on K, its values decide the amount of importance given to Q.

The output represents the multiplication of the attention weights and the V (value) vector. 
This ensures that the words you want to focus on are kept as-is and the irrelevant words are flushed out.
----------------------------------------------------------------------------------
'''
def print_out(q, k, v):
	temp_out, temp_attn = scaled_dot_product_attention(
								q, k, v, None
							)
	print ('Attention weights are:')
	print (temp_attn)
	print ('Output is:')
	print (temp_out)

np.set_printoptions(suppress=True)

temp_k = tf.constant(
						[[10,0,0],
						[0,10,0],
						[0,0,10],
						[0,0,10]], 
						dtype=tf.float32
					)  # (4, 3)

temp_v = tf.constant(
						[[  1,0],
						[  10,0],
						[ 100,5],
						[1000,6]], 
						dtype=tf.float32
					)  # (4, 2)

# This `query` aligns with the second `key`,
# so the second `value` is returned.
temp_q = tf.constant([[0, 10, 0]], dtype=tf.float32)  # (1, 3)
print_out(temp_q, temp_k, temp_v)

np.set_printoptions(suppress=True)

temp_k = tf.constant(
						[[10,0,0],
						[0,10,0],
						[0,0,10],
						[0,0,10]], 
						dtype=tf.float32
					)  # (4, 3)

temp_v = tf.constant(
						[[   1,0],
						[  10,0],
						[ 100,5],
						[1000,6]], 
						dtype=tf.float32
					)  # (4, 2)

# This `query` aligns with the second `key`,
# so the second `value` is returned.
temp_q = tf.constant([[0, 10, 0]], dtype=tf.float32)  # (1, 3)
print_out(temp_q, temp_k, temp_v)

# This query aligns equally with the first and second key, 
# so their values get averaged.
temp_q = tf.constant([[10, 10, 0]], dtype=tf.float32)  # (1, 3)
print_out(temp_q, temp_k, temp_v)

'''
--------------------------------------------------------------------------
Pass all the queries together.
--------------------------------------------------------------------------
'''
temp_q = tf.constant([[0, 0, 10], [0, 10, 0], [10, 10, 0]], dtype=tf.float32)  # (3, 3)
print_out(temp_q, temp_k, temp_v)

print   (
        '---------------------------------------------------------------------------------\n'
        '      Multi-head attention                                                       \n'
        '---------------------------------------------------------------------------------\n'
        )
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'multi_head_attention.png'))
im.show()

'''
----------------------------------------------------------------------------------------
Multi-head attention consists of four parts:

	* Linear layers and split into heads.
	* Scaled dot-product attention.
	* Concatenation of heads.
	* Final linear layer.

Each multi-head attention block gets three inputs; Q (query), K (key), V (value). 
These are put through linear (Dense) layers and split up into multiple heads.

The scaled_dot_product_attention defined above is applied to each head (broadcasted for efficiency). 
An appropriate mask must be used in the attention step. 
The attention output for each head is then concatenated (using tf.transpose, and tf.reshape) 
and put through a final Dense layer.

Instead of one single attention head, 
Q, K, and V are split into multiple heads 
because it allows the model to jointly attend to information at different positions from different representational spaces. 
After the split each head has a reduced dimensionality, 
so the total computation cost is the same as a single head attention with full dimensionality.
-----------------------------------------------------------------------------------------
'''
class MultiHeadAttention(tf.keras.layers.Layer):
	def __init__(self, d_model, num_heads):
		super(MultiHeadAttention, self).__init__()
		self.num_heads = num_heads
		self.d_model = d_model
		
		assert d_model % self.num_heads == 0
		
		self.depth = d_model // self.num_heads
		
		self.wq = tf.keras.layers.Dense(d_model)
		self.wk = tf.keras.layers.Dense(d_model)
		self.wv = tf.keras.layers.Dense(d_model)
		
		self.dense = tf.keras.layers.Dense(d_model)
    
	def split_heads(self, x, batch_size):
		"""Split the last dimension into (num_heads, depth).
		Transpose the result such that the shape is (batch_size, num_heads, seq_len, depth)
		"""
		x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
		return tf.transpose(x, perm=[0, 2, 1, 3])
    
	def call(self, v, k, q, mask):
		batch_size = tf.shape(q)[0]
		
		q = self.wq(q)  # (batch_size, seq_len, d_model)
		k = self.wk(k)  # (batch_size, seq_len, d_model)
		v = self.wv(v)  # (batch_size, seq_len, d_model)
		
		q = self.split_heads(q, batch_size)  # (batch_size, num_heads, seq_len_q, depth)
		k = self.split_heads(k, batch_size)  # (batch_size, num_heads, seq_len_k, depth)
		v = self.split_heads(v, batch_size)  # (batch_size, num_heads, seq_len_v, depth)
		
		# scaled_attention.shape == (batch_size, num_heads, seq_len_q, depth)
		# attention_weights.shape == (batch_size, num_heads, seq_len_q, seq_len_k)
		scaled_attention, attention_weights = scaled_dot_product_attention(
													q, k, v, mask
												)
		
		scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])  # (batch_size, seq_len_q, num_heads, depth)

		concat_attention = tf.reshape(
										scaled_attention, 
										(batch_size, -1, self.d_model)
									)  # (batch_size, seq_len_q, d_model)

		output = self.dense(concat_attention)  # (batch_size, seq_len_q, d_model)
		
		return output, attention_weights

'''
----------------------------------------------------------------------------------------
Create a MultiHeadAttention layer to try out. 
At each location in the sequence, y, the MultiHeadAttention runs all 8 attention heads across all other locations in the sequence, 
returning a new vector of the same length at each location.
---------------------------------------------------------------------------------------
'''
temp_mha = MultiHeadAttention(d_model=512, num_heads=8)
y = tf.random.uniform((1, 60, 512))  # (batch_size, encoder_sequence, d_model)
out, attn = temp_mha(y, k=y, q=y, mask=None)
print('out.shape = {0}, attn.shape = {1}\n'.format(out.shape, attn.shape))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Point wise feed forward network                                            \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Point wise feed forward network consists of two fully-connected layers with a ReLU activation in between.
-----------------------------------------------------------------------------------------
'''
def point_wise_feed_forward_network(d_model, dff):
		return tf.keras.Sequential([
			tf.keras.layers.Dense(dff, activation='relu'),  # (batch_size, seq_len, dff)
			tf.keras.layers.Dense(d_model)  # (batch_size, seq_len, d_model)
		])

sample_ffn = point_wise_feed_forward_network(512, 2048)
print('sample_ffn(tf.random.uniform((64, 50, 512))).shape = \n{0}\n'.format(sample_ffn(tf.random.uniform((64, 50, 512))).shape))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Encoder and decoder                                                        \n'
        '---------------------------------------------------------------------------------\n'
        )
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'transformer.png'))
im.show()

'''
-----------------------------------------------------------------------------------------
The transformer model follows the same general pattern 
as a standard sequence to sequence with attention model.

	* The input sentence is passed through N encoder layers 
		that generates an output for each word/token in the sequence.
	* The decoder attends on the encoder's output 
		and its own input (self-attention) to predict the next word.
-----------------------------------------------------------------------------------------
'''
print   (
        '---------------------------------------------------------------------------------\n'
        '      Encoder layer                                                              \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
Each encoder layer consists of sublayers:

	1. Multi-head attention (with padding mask)
	2. Point wise feed forward networks.
	
Each of these sublayers has a residual connection around it followed by a layer normalization. 
Residual connections help in avoiding the vanishing gradient problem in deep networks.

The output of each sublayer is LayerNorm(x + Sublayer(x)). 
The normalization is done on the d_model (last) axis. 
There are N encoder layers in the transformer.
------------------------------------------------------------------------------------------
'''
class EncoderLayer(tf.keras.layers.Layer):
	def __init__(self, d_model, num_heads, dff, rate=0.1):
		super(EncoderLayer, self).__init__()

		self.mha = MultiHeadAttention(d_model, num_heads)
		self.ffn = point_wise_feed_forward_network(d_model, dff)

		self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
		self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
		
		self.dropout1 = tf.keras.layers.Dropout(rate)
		self.dropout2 = tf.keras.layers.Dropout(rate)
    
	def call(self, x, training, mask):

		attn_output, _ = self.mha(x, x, x, mask)  # (batch_size, input_seq_len, d_model)
		attn_output = self.dropout1(attn_output, training=training)
		out1 = self.layernorm1(x + attn_output)  # (batch_size, input_seq_len, d_model)
		
		ffn_output = self.ffn(out1)  # (batch_size, input_seq_len, d_model)
		ffn_output = self.dropout2(ffn_output, training=training)
		out2 = self.layernorm2(out1 + ffn_output)  # (batch_size, input_seq_len, d_model)
		
		return out2

sample_encoder_layer = EncoderLayer(512, 8, 2048)

sample_encoder_layer_output = sample_encoder_layer(
								tf.random.uniform((64, 43, 512)), 
								False, None
							)

print('sample_encoder_layer_output.shape = {0}\n'.format(sample_encoder_layer_output.shape))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Decoder layer                                                              \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Each decoder layer consists of sublayers:

	1. Masked multi-head attention (with look ahead mask and padding mask)
	2. Multi-head attention (with padding mask). 
		V (value) and K (key) receive the encoder output as inputs. 
		Q (query) receives the output from the masked multi-head attention sublayer.
	3. Point wise feed forward networks
	
Each of these sublayers has a residual connection around it followed by a layer normalization. 
The output of each sublayer is LayerNorm(x + Sublayer(x)). 
The normalization is done on the d_model (last) axis.

There are N decoder layers in the transformer.

As Q receives the output from decoder's first attention block, and K receives the encoder output, 
the attention weights represent the importance given to the decoder's input based on the encoder's output. 
In other words, 
the decoder predicts the next word by looking at the encoder output and self-attending to its own output. 
See the demonstration above in the scaled dot product attention section.
--------------------------------------------------------------------------------------------
'''
class DecoderLayer(tf.keras.layers.Layer):
	def __init__(self, d_model, num_heads, dff, rate=0.1):
		super(DecoderLayer, self).__init__()

		self.mha1 = MultiHeadAttention(d_model, num_heads)
		self.mha2 = MultiHeadAttention(d_model, num_heads)

		self.ffn = point_wise_feed_forward_network(d_model, dff)

		self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
		self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
		self.layernorm3 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
		
		self.dropout1 = tf.keras.layers.Dropout(rate)
		self.dropout2 = tf.keras.layers.Dropout(rate)
		self.dropout3 = tf.keras.layers.Dropout(rate)

	def call(self, x, enc_output, training, look_ahead_mask, padding_mask):
		# enc_output.shape == (batch_size, input_seq_len, d_model)

		attn1, attn_weights_block1 = self.mha1(x, x, x, look_ahead_mask)  # (batch_size, target_seq_len, d_model)
		attn1 = self.dropout1(attn1, training=training)
		out1 = self.layernorm1(attn1 + x)
		
		attn2, attn_weights_block2 = self.mha2(
										enc_output, 
										enc_output, 
										out1, 
										padding_mask
									)  # (batch_size, target_seq_len, d_model)

		attn2 = self.dropout2(attn2, training=training)
		out2 = self.layernorm2(attn2 + out1)  # (batch_size, target_seq_len, d_model)
		
		ffn_output = self.ffn(out2)  # (batch_size, target_seq_len, d_model)
		ffn_output = self.dropout3(ffn_output, training=training)
		out3 = self.layernorm3(ffn_output + out2)  # (batch_size, target_seq_len, d_model)
		
		return out3, attn_weights_block1, attn_weights_block2

sample_decoder_layer = DecoderLayer(512, 8, 2048)

sample_decoder_layer_output, _, _ = sample_decoder_layer(
										tf.random.uniform((64, 50, 512)),
										sample_encoder_layer_output, 
										False, 
										None, 
										None
									)

print('sample_decoder_layer_output.shape = {0}\n'.format(sample_decoder_layer_output.shape))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Encoder                                                                    \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
The Encoder consists of:

	1. Input Embedding
	2. Positional Encoding
	3. N encoder layers
	
The input is put through an embedding which is summed with the positional encoding. 
The output of this summation is the input to the encoder layers. 
The output of the encoder is the input to the decoder.
-----------------------------------------------------------------------------------------
'''
class Encoder(tf.keras.layers.Layer):
	def __init__(
					self, 
					num_layers, 
					d_model, 
					num_heads, 
					dff, 
					input_vocab_size,
					maximum_position_encoding, 
					rate=0.1
				):
		super(Encoder, self).__init__()

		self.d_model = d_model
		self.num_layers = num_layers
		
		self.embedding = tf.keras.layers.Embedding(input_vocab_size, d_model)
		self.pos_encoding = positional_encoding(
								maximum_position_encoding, 
								self.d_model
							)
		
		
		self.enc_layers = [EncoderLayer(d_model, num_heads, dff, rate) 
						for _ in range(num_layers)]
	
		self.dropout = tf.keras.layers.Dropout(rate)
        
	def call(self, x, training, mask):

		seq_len = tf.shape(x)[1]
		
		# adding embedding and position encoding.
		x = self.embedding(x)  # (batch_size, input_seq_len, d_model)
		x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
		x += self.pos_encoding[:, :seq_len, :]

		x = self.dropout(x, training=training)
		
		for i in range(self.num_layers):
			x = self.enc_layers[i](x, training, mask)
		
		return x  # (batch_size, input_seq_len, d_model)

sample_encoder = Encoder(
					num_layers=2, d_model=512, num_heads=8, 
					dff=2048, input_vocab_size=8500,
					maximum_position_encoding=10000
				)
temp_input = tf.random.uniform((64, 62), dtype=tf.int64, minval=0, maxval=200)

sample_encoder_output = sample_encoder(temp_input, training=False, mask=None)

print ('sample_encoder_output.shape = {0}\n'.format(sample_encoder_output.shape))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Decoder                                                                    \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
The Decoder consists of:

	1. Output Embedding
	2. Positional Encoding
	3. N decoder layers

The target is put through an embedding which is summed with the positional encoding. 
The output of this summation is the input to the decoder layers. 
The output of the decoder is the input to the final linear layer.
----------------------------------------------------------------------------------------
'''
class Decoder(tf.keras.layers.Layer):
	def __init__(
					self, num_layers, d_model, num_heads, dff, target_vocab_size,
					maximum_position_encoding, rate=0.1
				):
		super(Decoder, self).__init__()

		self.d_model = d_model
		self.num_layers = num_layers
		
		self.embedding = tf.keras.layers.Embedding(target_vocab_size, d_model)
		self.pos_encoding = positional_encoding(maximum_position_encoding, d_model)
		
		self.dec_layers = [
							DecoderLayer(d_model, num_heads, dff, rate) 
							for _ in range(num_layers)
						]

		self.dropout = tf.keras.layers.Dropout(rate)
    
	def call(
				self, x, enc_output, training, 
				look_ahead_mask, padding_mask
			):

		seq_len = tf.shape(x)[1]
		attention_weights = {}
		
		x = self.embedding(x)  # (batch_size, target_seq_len, d_model)
		x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
		x += self.pos_encoding[:, :seq_len, :]
		
		x = self.dropout(x, training=training)

		for i in range(self.num_layers):
			x, block1, block2 = self.dec_layers[i](
													x, enc_output, 
													training, look_ahead_mask, 
													padding_mask
												)
			
			attention_weights['decoder_layer{}_block1'.format(i+1)] = block1
			attention_weights['decoder_layer{}_block2'.format(i+1)] = block2
		
		# x.shape == (batch_size, target_seq_len, d_model)
		return x, attention_weights

sample_decoder = Decoder(
							num_layers=2, d_model=512, num_heads=8, 
							dff=2048, target_vocab_size=8000,
							maximum_position_encoding=5000
						)
temp_input = tf.random.uniform((64, 26), dtype=tf.int64, minval=0, maxval=200)

output, attn = sample_decoder(
					temp_input, 
					enc_output=sample_encoder_output, 
					training=False,
					look_ahead_mask=None, 
					padding_mask=None
				)

print(
		'output.shape = {0}, attn[decoder_layer2_block2].shape = {1}\n'
		.format(output.shape, attn['decoder_layer2_block2'].shape)
	)

print   (
        '---------------------------------------------------------------------------------\n'
        '      Create the Transformer                                                     \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Transformer consists of the encoder, decoder and a final linear layer. 
The output of the decoder is the input to the linear layer and its output is returned.
------------------------------------------------------------------------------------------
'''
class Transformer(tf.keras.Model):
	def __init__(
					self, num_layers, d_model, num_heads, dff, input_vocab_size, 
					target_vocab_size, pe_input, pe_target, rate=0.1
				):
		super(Transformer, self).__init__()

		self.encoder = Encoder(
							num_layers, d_model, num_heads, dff, 
							input_vocab_size, pe_input, rate
						)

		self.decoder = Decoder(
							num_layers, d_model, num_heads, dff, 
							target_vocab_size, pe_target, rate
						)

		self.final_layer = tf.keras.layers.Dense(target_vocab_size)
    
	def call(
				self, inp, tar, training, enc_padding_mask, 
				look_ahead_mask, dec_padding_mask
			):

		enc_output = self.encoder(inp, training, enc_padding_mask)  # (batch_size, inp_seq_len, d_model)
		
		# dec_output.shape == (batch_size, tar_seq_len, d_model)
		dec_output, attention_weights = self.decoder(
											tar, enc_output, training, 
											look_ahead_mask, dec_padding_mask
										)
		
		final_output = self.final_layer(dec_output)  # (batch_size, tar_seq_len, target_vocab_size)
		
		return final_output, attention_weights

sample_transformer = Transformer(
						num_layers=2, d_model=512, num_heads=8, dff=2048, 
						input_vocab_size=8500, target_vocab_size=8000, 
						pe_input=10000, pe_target=6000
					)

temp_input = tf.random.uniform((64, 38), dtype=tf.int64, minval=0, maxval=200)
temp_target = tf.random.uniform((64, 36), dtype=tf.int64, minval=0, maxval=200)

fn_out, _ = sample_transformer(
				temp_input, temp_target, training=False, 
				enc_padding_mask=None, 
				look_ahead_mask=None,
				dec_padding_mask=None
			)

print('fn_out.shape = {0}\n'.format(fn_out.shape))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Set hyperparameters                                                        \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
To keep this example small and relatively fast, the values for num_layers, 
d_model, and dff have been reduced.

The values used in the base model of transformer were; num_layers=6, d_model = 512, dff = 2048. 
See the paper for all the other versions of the transformer.

Note: 
By changing the values below, you can get the model that achieved state of the art on many tasks.
-----------------------------------------------------------------------------------------
'''
num_layers = 4
d_model = 128
dff = 512
num_heads = 8

input_vocab_size = tokenizer_pt.vocab_size + 2
target_vocab_size = tokenizer_en.vocab_size + 2
dropout_rate = 0.1

print   (
        '---------------------------------------------------------------------------------\n'
        '      Optimizer                                                                  \n'
        '---------------------------------------------------------------------------------\n'
        )
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'transformer_equation_00.jpg'))
im.show()

class CustomSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
	def __init__(self, d_model, warmup_steps=4000):
		super(CustomSchedule, self).__init__()
		
		self.d_model = d_model
		self.d_model = tf.cast(self.d_model, tf.float32)

		self.warmup_steps = warmup_steps

	def __call__(self, step):
		arg1 = tf.math.rsqrt(step)
		arg2 = step * (self.warmup_steps ** -1.5)

		return tf.math.rsqrt(self.d_model) * tf.math.minimum(arg1, arg2)

learning_rate = CustomSchedule(d_model)

optimizer = tf.keras.optimizers.Adam(
				learning_rate, beta_1=0.9, 
				beta_2=0.98, epsilon=1e-9
			)

temp_learning_rate_schedule = CustomSchedule(d_model)

plt.plot(temp_learning_rate_schedule(tf.range(40000, dtype=tf.float32)))
plt.ylabel("Learning Rate")
plt.xlabel("Train Step")
plt.show()

print   (
        '---------------------------------------------------------------------------------\n'
        '      Loss and metrics                                                           \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Since the target sequences are padded, 
it is important to apply a padding mask when calculating the loss.
------------------------------------------------------------------------------------------
'''
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
					from_logits=True, reduction='none'
				)

def loss_function(real, pred):
	mask = tf.math.logical_not(tf.math.equal(real, 0))
	loss_ = loss_object(real, pred)

	mask = tf.cast(mask, dtype=loss_.dtype)
	loss_ *= mask

	return tf.reduce_mean(loss_)

train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(
					name='train_accuracy'
				)

print('train_loss = {0}, train_accuracy = {1}\n'.format(train_loss, train_accuracy))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Training and checkpointing                                                 \n'
        '---------------------------------------------------------------------------------\n'
        )
transformer = Transformer(
				num_layers, d_model, num_heads, dff,
				input_vocab_size, target_vocab_size, 
				pe_input=input_vocab_size, 
				pe_target=target_vocab_size,
				rate=dropout_rate
			)

def create_masks(inp, tar):
	# Encoder padding mask
	enc_padding_mask = create_padding_mask(inp)

	# Used in the 2nd attention block in the decoder.
	# This padding mask is used to mask the encoder outputs.
	dec_padding_mask = create_padding_mask(inp)

	# Used in the 1st attention block in the decoder.
	# It is used to pad and mask future tokens in the input received by 
	# the decoder.
	look_ahead_mask = create_look_ahead_mask(tf.shape(tar)[1])
	dec_target_padding_mask = create_padding_mask(tar)
	combined_mask = tf.maximum(dec_target_padding_mask, look_ahead_mask)

	return enc_padding_mask, combined_mask, dec_padding_mask

'''
---------------------------------------------------------------------------
Create the checkpoint path and the checkpoint manager. 
This will be used to save checkpoints every n epochs.
--------------------------------------------------------------------------
'''
checkpoint_path = str(PROJECT_ROOT_DIR.joinpath('training_checkpoints', 'train'))

ckpt = tf.train.Checkpoint(
			transformer=transformer,
			optimizer=optimizer
		)

ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

# if a checkpoint exists, restore the latest checkpoint.
if ckpt_manager.latest_checkpoint:
	ckpt.restore(ckpt_manager.latest_checkpoint)
	print ('Latest checkpoint restored!!')

'''
-------------------------------------------------------------------------
The target is divided into tar_inp and tar_real. 
tar_inp is passed as an input to the decoder. 
tar_real is that same input shifted by 1: 
At each location in tar_input, tar_real contains the next token that should be predicted.

For example, sentence = "SOS A lion in the jungle is sleeping EOS"

tar_inp = "SOS A lion in the jungle is sleeping"

tar_real = "A lion in the jungle is sleeping EOS"

The transformer is an auto-regressive model: 
it makes predictions one part at a time, and uses its output so far to decide what to do next.

During training this example uses teacher-forcing (like in the text generation tutorial). 
Teacher forcing is passing the true output to the next time step regardless of what the model predicts at the current time step.

As the transformer predicts each word, 
self-attention allows it to look at the previous words in the input sequence to better predict the next word.

To prevent the model from peaking at the expected output the model uses a look-ahead mask.
-------------------------------------------------------------------------
'''
EPOCHS = 20

# The @tf.function trace-compiles train_step into a TF graph for faster
# execution. The function specializes to the precise shape of the argument
# tensors. To avoid re-tracing due to the variable sequence lengths or variable
# batch sizes (the last batch is smaller), use input_signature to specify
# more generic shapes.

train_step_signature = [
    tf.TensorSpec(shape=(None, None), dtype=tf.int64),
    tf.TensorSpec(shape=(None, None), dtype=tf.int64),
]

@tf.function(input_signature=train_step_signature)
def train_step(inp, tar):
	tar_inp = tar[:, :-1]
	tar_real = tar[:, 1:]

	enc_padding_mask, combined_mask, dec_padding_mask = create_masks(inp, tar_inp)

	with tf.GradientTape() as tape:
		predictions, _ = transformer(
							inp, tar_inp, 
							True, 
							enc_padding_mask, 
							combined_mask, 
							dec_padding_mask
						)
		loss = loss_function(tar_real, predictions)

	gradients = tape.gradient(loss, transformer.trainable_variables)    
	optimizer.apply_gradients(zip(gradients, transformer.trainable_variables))

	train_loss(loss)
	train_accuracy(tar_real, predictions)

'''
---------------------------------------------------------------------------------
Portuguese is used as the input language and English is the target language.
---------------------------------------------------------------------------------
'''
for epoch in range(EPOCHS):
	start = time.time()

	train_loss.reset_states()
	train_accuracy.reset_states()

	# inp -> portuguese, tar -> english
	for (batch, (inp, tar)) in enumerate(train_dataset):
		train_step(inp, tar)
    
		if batch % 50 == 0:
			print ('Epoch {} Batch {} Loss {:.4f} Accuracy {:.4f}'.format(
				epoch + 1, batch, train_loss.result(), train_accuracy.result()))

	if (epoch + 1) % 5 == 0:
		ckpt_save_path = ckpt_manager.save()
		print ('Saving checkpoint for epoch {} at {}'
				.format(epoch+1, ckpt_save_path))

	print ('Epoch {} Loss {:.4f} Accuracy {:.4f}'
			.format(epoch + 1, train_loss.result(), train_accuracy.result()))

	print ('Time taken for 1 epoch: {} secs\n'.format(time.time() - start))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Evaluate                                                                   \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
The following steps are used for evaluation:

	* Encode the input sentence using the Portuguese tokenizer (tokenizer_pt). 
		Moreover, add the start and end token so the input is equivalent to what the model is trained with. 
		This is the encoder input.
	* The decoder input is the start token == tokenizer_en.vocab_size.
	* Calculate the padding masks and the look ahead masks.
	* The decoder then outputs the predictions by looking at the encoder output and its own output (self-attention).
	* Select the last word and calculate the argmax of that.
	* Concatentate the predicted word to the decoder input as pass it to the decoder.
	*In this approach, the decoder predicts the next word based on the previous words it predicted.

Note: 
The model used here has less capacity to keep the example relatively faster so the predictions maybe less right. 
To reproduce the results in the paper, 
use the entire dataset and base transformer model or transformer XL, by changing the hyperparameters above.
-------------------------------------------------------------------------------------------
'''
def evaluate(inp_sentence):
	start_token = [tokenizer_pt.vocab_size]
	end_token = [tokenizer_pt.vocab_size + 1]

	# inp sentence is portuguese, hence adding the start and end token
	inp_sentence = start_token + tokenizer_pt.encode(inp_sentence) + end_token
	encoder_input = tf.expand_dims(inp_sentence, 0)

	# as the target is english, the first word to the transformer should be the
	# english start token.
	decoder_input = [tokenizer_en.vocab_size]
	output = tf.expand_dims(decoder_input, 0)
    
	for i in range(MAX_LENGTH):
		enc_padding_mask, combined_mask, dec_padding_mask = create_masks(
																encoder_input, output
															)

		# predictions.shape == (batch_size, seq_len, vocab_size)
		predictions, attention_weights = transformer(
												encoder_input, 
												output,
												False,
												enc_padding_mask,
												combined_mask,
												dec_padding_mask
											)
		
		# select the last word from the seq_len dimension
		predictions = predictions[: ,-1:, :]

		predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)
		
		# return the result if the predicted_id is equal to the end token
		if predicted_id == tokenizer_en.vocab_size+1:
			return tf.squeeze(output, axis=0), attention_weights
		
		# concatentate the predicted_id to the output which is given to the decoder
		# as its input.
		output = tf.concat([output, predicted_id], axis=-1)

	return tf.squeeze(output, axis=0), attention_weights

def plot_attention_weights(attention, sentence, result, layer):
	fig = plt.figure(figsize=(16, 8))

	sentence = tokenizer_pt.encode(sentence)

	attention = tf.squeeze(attention[layer], axis=0)

	for head in range(attention.shape[0]):
		ax = fig.add_subplot(2, 4, head+1)
		
		# plot the attention weights
		ax.matshow(attention[head][:-1, :], cmap='viridis')

		fontdict = {'fontsize': 10}
		
		ax.set_xticks(range(len(sentence)+2))
		ax.set_yticks(range(len(result)))
		
		ax.set_ylim(len(result)-1.5, -0.5)
			
		ax.set_xticklabels(
			['<start>']+[tokenizer_pt.decode([i]) for i in sentence]+['<end>'], 
			fontdict=fontdict, rotation=90
		)
		
		ax.set_yticklabels(
			[tokenizer_en.decode([i]) for i in result if i < tokenizer_en.vocab_size], 
			fontdict=fontdict
		)
		
		ax.set_xlabel('Head {}'.format(head+1))

	plt.tight_layout()
	plt.show()

def translate(sentence, plot=''):
	result, attention_weights = evaluate(sentence)

	predicted_sentence = tokenizer_en.decode(
							[i for i in result if i < tokenizer_en.vocab_size]
						)  

	print('Input: {}'.format(sentence))
	print('Predicted translation: {}'.format(predicted_sentence))

	if plot:
		plot_attention_weights(attention_weights, sentence, result, plot)

translate("este é um problema que temos que resolver.")
print ("Real translation: this is a problem we have to solve .")

translate("os meus vizinhos ouviram sobre esta ideia.")
print ("Real translation: and my neighboring homes heard about this idea .")

translate("vou então muito rapidamente partilhar convosco algumas histórias de algumas coisas mágicas que aconteceram.")
print ("Real translation: so i 'll just share with you some stories very quickly of some magical things that have happened .")

'''
--------------------------------------------------------------------------------
You can pass different layers and attention blocks of the decoder to the plot parameter.
--------------------------------------------------------------------------------
'''
translate("este é o primeiro livro que eu fiz.", plot='decoder_layer4_block2')
print ("Real translation: this is the first book i've ever done.")

print   (
        '------------------------------------------------------------------------------------------------------\n'
        '       finished         text_transformer.py                                                           \n'
        '------------------------------------------------------------------------------------------------------\n'
        )
print()
print()
print()