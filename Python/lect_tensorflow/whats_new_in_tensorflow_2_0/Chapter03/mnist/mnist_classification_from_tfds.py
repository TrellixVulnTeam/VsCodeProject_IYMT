'''
------------------------------------------------------------------------------------------
chapter03/minist
    mnist_classification_from_tfds
------------------------------------------------------------------------------------------
'''
# common library
from __future__ import absolute_import, division, print_function, unicode_literals

import time
import os
from packaging import version
from PIL import Image
import itertools

import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_datasets as tfds

print(__doc__)

# Display current path
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print('PROJECT_ROOT_DIR = \n{0}\n'.format(PROJECT_ROOT_DIR))

# Display tensorflow version
print("TensorFlow version: ", tf.version.VERSION)
assert version.parse(tf.version.VERSION).release[0] >= 2, \
"This notebook requires TensorFlow 2.0 or above."

'''
---------------------------------------------------------------------------------
Can use below simple code to download 'mnist' dataset
datasets, info = tfds.load(name='mnist', with_info=True, as_supervised=True)
mnist_train, mnist_test = datasets['train'], datasets['test']
---------------------------------------------------------------------------------
'''

print   (
        '------------------------------------------------------------------------------------------------------\n'
        '   Below function loads mnist data using tensorflow_datasets, split to train, validation and test.    \n'
        '------------------------------------------------------------------------------------------------------\n'
        )

def load_mnist():
    """ load tensorflow mnist builtin dataset """
    # Split the training data to 90, and 10 %
    ds_train_s, ds_validate_s = tfds.Split.TRAIN.subsplit([9, 1])
    # Download and load three datasets directly
    tfds_train, tfds_validate, tfds_test = tfds.load(
                                                name='mnist',
                                                split=[ds_train_s, ds_validate_s, tfds.Split.TEST], 
                                                as_supervised=True
                                            )
        
    return tfds_train, tfds_validate, tfds_test

mnist_train, mnist_validate, mnist_test = load_mnist()

BUFFER_SIZE = 10 # Use a much larger value for real code.
BATCH_SIZE = 64
NUM_EPOCHS = 3

def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255

    return image, label

train_data = mnist_train.map(scale).shuffle(BUFFER_SIZE).batch(BATCH_SIZE).take(5)
validation_data = mnist_validate.map(scale).batch(BATCH_SIZE).take(5)
test_data = mnist_test.map(scale).batch(BATCH_SIZE).take(5)

STEPS_PER_EPOCH = 5

train_data = train_data.take(STEPS_PER_EPOCH)
validation_data = validation_data.take(STEPS_PER_EPOCH)
test_data = test_data.take(STEPS_PER_EPOCH)

image_batch, label_batch = next(iter(train_data))
print(image_batch.shape)

print()

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(
        32, 3, activation='relu',
        kernel_regularizer=tf.keras.regularizers.l2(0.02),
        input_shape=(28, 28, 1)
    ),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Model is the full model w/o custom layers
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(train_data, validation_data=validation_data, epochs=NUM_EPOCHS)

loss, acc = model.evaluate(test_data)
print("Loss {}, Accuracy {}\n".format(loss, acc))
