'''
------------------------------------------------------------------------------------------
genarative
    Deep Convolutional Generative Adversarial Network

This tutorial demonstrates how to generate images of handwritten digits using a Deep Convolutional Generative Adversarial Network (DCGAN). 
The code is written using the Keras Sequential API with a tf.GradientTape training loop.

------------------------------------------------------------------------------------------
'''
# common library
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import pprint
import time
import datetime
import contextlib
import tempfile
import functools
import imageio
import glob
import datetime
from pathlib import Path
from PIL import Image

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

import tensorflow as tf

print(__doc__)

AUTOTUNE = tf.data.experimental.AUTOTUNE
pd.options.display.max_rows = None

mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

# Display current path
basic_path = Path.cwd()
PROJECT_ROOT_DIR = basic_path.joinpath('Python', 'Normal', 'tensorflow')
print('PROJECT_ROOT_DIR = \n{0}\n'.format(PROJECT_ROOT_DIR))

# Display tensorflow version
print("TensorFlow version: ", tf.version.VERSION)



print   (
        '---------------------------------------------------------------------------------\n'
        '      What are GANs?                                                             \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Generative Adversarial Networks (GANs) are one of the most interesting ideas in computer science today. 
Two models are trained simultaneously by an adversarial process. 
A generator ("the artist") learns to create images that look real, 
while a discriminator ("the art critic") learns to tell real images apart from fakes.
------------------------------------------------------------------------------------------
'''
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'genarative_dcgan_01.jpg'))
im.show()

'''
------------------------------------------------------------------------------------------
During training, the generator progressively becomes better at creating images that look real, 
while the discriminator becomes better at telling them apart. 
The process reaches equilibrium when the discriminator can no longer distinguish real images from fakes.
------------------------------------------------------------------------------------------
'''
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'genarative_dcgan_02.jpg'))
im.show()

'''
-----------------------------------------------------------------------------------------
This notebook demonstrates this process on the MNIST dataset. 
The following animation shows a series of images produced by the generator as it was trained for 50 epochs. 
The images begin as random noise, and increasingly resemble hand written digits over time.
-----------------------------------------------------------------------------------------
'''
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'genarative_dcgan_03.jpg'))
im.show()

'''
----------------------------------------------------------------------------------------
To learn more about GANs, we recommend MIT's Intro to Deep Learning course.
----------------------------------------------------------------------------------------
'''
print   (
        '---------------------------------------------------------------------------------\n'
        '      Load and prepare the dataset                                               \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
----------------------------------------------------------------------------------------
You will use the MNIST dataset to train the generator and the discriminator. 
The generator will generate handwritten digits resembling the MNIST data.
----------------------------------------------------------------------------------------
'''
(train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()

train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')
train_images = (train_images - 127.5) / 127.5 # Normalize the images to [-1, 1]

BUFFER_SIZE = 60000
BATCH_SIZE = 256

# Batch and shuffle the data
train_dataset = tf.data.Dataset.from_tensor_slices(train_images).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

print   (
        '---------------------------------------------------------------------------------\n'
        '      Create the models                                                          \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Both the generator and discriminator are defined using the Keras Sequential API.
------------------------------------------------------------------------------------------
'''
print   (
        '---------------------------------------------------------------------------------\n'
        '      The Generator                                                              \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
The generator uses tf.keras.layers.Conv2DTranspose (upsampling) layers to produce an image from a seed (random noise). 
Start with a Dense layer that takes this seed as input, then upsample several times until you reach the desired image size of 28x28x1. 
Notice the tf.keras.layers.LeakyReLU activation for each layer, except the output layer which uses tanh.
-----------------------------------------------------------------------------------------
'''
def make_generator_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Reshape((7, 7, 256)))
    assert model.output_shape == (None, 7, 7, 256) # Note: None is the batch size

    model.add(tf.keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
    assert model.output_shape == (None, 7, 7, 128)
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    assert model.output_shape == (None, 14, 14, 64)
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    assert model.output_shape == (None, 28, 28, 1)

    return model

'''
------------------------------------------------------------------------------------------
Use the (as yet untrained) generator to create an image.
------------------------------------------------------------------------------------------
'''
generator = make_generator_model()

noise = tf.random.normal([1, 100])
generated_image = generator(noise, training=False)

plt.imshow(generated_image[0, :, :, 0], cmap='gray')

print   (
        '---------------------------------------------------------------------------------\n'
        '      The Discriminator                                                          \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
The discriminator is a CNN-based image classifier.
-----------------------------------------------------------------------------------------
'''
def make_discriminator_model():
    model = tf.keras.Sequential()
    model.add(
        tf.keras.layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1])
    )
    model.add(tf.keras.layers.LeakyReLU())
    model.add(tf.keras.layers.Dropout(0.3))

    model.add(tf.keras.layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
    model.add(tf.keras.layers.LeakyReLU())
    model.add(tf.keras.layers.Dropout(0.3))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1))

    return model

'''
------------------------------------------------------------------------------------------
Use the (as yet untrained) discriminator to classify the generated images as real or fake. 
The model will be trained to output positive values for real images, and negative values for fake images.
------------------------------------------------------------------------------------------
'''
discriminator = make_discriminator_model()
decision = discriminator(generated_image)
print ('decisio = {0}\n'.format(decision))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Define the loss and optimizers                                             \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Define loss functions and optimizers for both models.
------------------------------------------------------------------------------------------
'''
# This method returns a helper function to compute cross entropy loss
cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

print   (
        '---------------------------------------------------------------------------------\n'
        '      Discriminator loss                                                         \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
This method quantifies how well the discriminator is able to distinguish real images from fakes. 
It compares the discriminator's predictions on real images to an array of 1s, 
and the discriminator's predictions on fake (generated) images to an array of 0s.
----------------------------------------------------------------------------------------
'''
def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

print   (
        '---------------------------------------------------------------------------------\n'
        '      Generator loss                                                             \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
The generator's loss quantifies how well it was able to trick the discriminator. 
Intuitively, if the generator is performing well, the discriminator will classify the fake images as real (or 1). 
Here, we will compare the discriminators decisions on the generated images to an array of 1s.
------------------------------------------------------------------------------------------
'''
def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output), fake_output)

'''
------------------------------------------------------------------------------------------
The discriminator and the generator optimizers are different since we will train two networks separately.
------------------------------------------------------------------------------------------
'''
generator_optimizer = tf.keras.optimizers.Adam(1e-4)
discriminator_optimizer = tf.keras.optimizers.Adam(1e-4)

print   (
        '---------------------------------------------------------------------------------\n'
        '      Save checkpoints                                                           \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
This notebook also demonstrates how to save and restore models, 
which can be helpful in case a long running training task is interrupted.
-----------------------------------------------------------------------------------------
'''
checkpoint_dir = PROJECT_ROOT_DIR.joinpath('training_checkpoints')

checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(
                    generator_optimizer=generator_optimizer,
                    discriminator_optimizer=discriminator_optimizer,
                    generator=generator,
                    discriminator=discriminator
                )

print   (
        '---------------------------------------------------------------------------------\n'
        '      Define the training loop                                                   \n'
        '---------------------------------------------------------------------------------\n'
        )

EPOCHS = 50
noise_dim = 100
num_examples_to_generate = 16

# We will reuse this seed overtime (so it's easier)
# to visualize progress in the animated GIF)
seed = tf.random.normal([num_examples_to_generate, noise_dim])

'''
-------------------------------------------------------------------------------------------
The training loop begins with generator receiving a random seed as input. 
That seed is used to produce an image. 
The discriminator is then used to classify real images (drawn from the training set) and fakes images (produced by the generator). 
The loss is calculated for each of these models, and the gradients are used to update the generator and discriminator.
-------------------------------------------------------------------------------------------
'''
# Notice the use of `tf.function`
# This annotation causes the function to be "compiled".
@tf.function
def train_step(images):
    noise = tf.random.normal([BATCH_SIZE, noise_dim])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

def train(dataset, epochs):
    for epoch in range(epochs):
        start = time.time()

    for image_batch in dataset:
        train_step(image_batch)

    # Produce images for the GIF as we go
    generate_and_save_images(
        generator,
        epoch + 1,
        seed
    )

    # Save the model every 15 epochs
    if (epoch + 1) % 15 == 0:
        checkpoint.save(file_prefix = checkpoint_prefix)

    print ('Time for epoch {} is {} sec'.format(epoch + 1, time.time()-start))

    # Generate after the final epoch
    generate_and_save_images(
        generator,
        epochs,
        seed
    )

print   (
        '---------------------------------------------------------------------------------\n'
        '      Generate and save images                                                   \n'
        '---------------------------------------------------------------------------------\n'
        )
def generate_and_save_images(model, epoch, test_input):
    # Notice `training` is set to False.
    # This is so all layers run in inference mode (batchnorm).
    predictions = model(test_input, training=False)

    fig = plt.figure(figsize=(4,4))

    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i+1)
        plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
        plt.axis('off')

    plt.savefig(PROJECT_ROOT_DIR.joinpath('images', 'image_at_epoch_{:04d}.png'.format(epoch)))
    plt.show()

print   (
        '---------------------------------------------------------------------------------\n'
        '      Train the model                                                            \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Call the train() method defined above to train the generator and discriminator simultaneously. 
Note, training GANs can be tricky. 
It's important that the generator and discriminator do not overpower each other (e.g., that they train at a similar rate).

At the beginning of the training, the generated images look like random noise. 
As training progresses, the generated digits will look increasingly real. After about 50 epochs, they resemble MNIST digits. 
This may take about one minute / epoch with the default settings on Colab.
------------------------------------------------------------------------------------------
'''
train(train_dataset, EPOCHS)

'''
------------------------------------------------------------------------------------------
Restore the latest checkpoint.
------------------------------------------------------------------------------------------
'''
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

print   (
        '---------------------------------------------------------------------------------\n'
        '      Create a GIF                                                               \n'
        '---------------------------------------------------------------------------------\n'
        )
# Display a single image using the epoch number
def display_image(epoch_no):
    return Image.open(PROJECT_ROOT_DIR.joinpath('images', 'image_at_epoch_{:04d}.png'.format(epoch_no)))

display_image(EPOCHS)

'''
--------------------------------------------------------------------
Use imageio to create an animated gif using the images saved during training.
--------------------------------------------------------------------
'''
anim_file = str(PROJECT_ROOT_DIR.joinpath('images', 'dcgan.gif'))

with imageio.get_writer(anim_file, mode='I') as writer:
    filenames = glob.glob(str(PROJECT_ROOT_DIR.joinpath('images', 'image*.png')))
    filenames = sorted(filenames)
    last = -1
    for i,filename in enumerate(filenames):
        frame = 2*(i**0.5)
        if round(frame) > round(last):
            last = frame
        else:
            continue
        image = imageio.imread(filename)
        writer.append_data(image)
    image = imageio.imread(filename)
    writer.append_data(image)

data_today = datetime.date.today()

print   (
        '------------------------------------------------------------------------------------------------------\n'
    )

print   (
        '       finished        generative_dcgan.py                        ({0})                \n'.format(data_today)
    )

print   (
        '------------------------------------------------------------------------------------------------------\n'
        )
print()
print()
print()