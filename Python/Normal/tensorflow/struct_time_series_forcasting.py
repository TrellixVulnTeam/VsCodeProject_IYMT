'''
------------------------------------------------------------------------------------------
structed data
    Time series forecasting

This tutorial is an introduction to time series forecasting using Recurrent Neural Networks (RNNs). 
This is covered in two parts: 
first, you will forecast a univariate time series, then you will forecast a multivariate time series.
------------------------------------------------------------------------------------------
'''
# common library
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import pprint
import contextlib
import tempfile
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
mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

# Display current path
basic_path = Path.cwd()
PROJECT_ROOT_DIR = basic_path.joinpath('Python', 'Normal', 'tensorflow')
print('PROJECT_ROOT_DIR = \n{0}\n'.format(PROJECT_ROOT_DIR))

# Display tensorflow version
print("TensorFlow version: ", tf.version.VERSION)

print   (
        '---------------------------------------------------------------------------------\n'
        '      The weather dataset                                                        \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
This tutorial uses a weather time series dataset recorded by the Max-Planck-Institute for Biogeochemistry.

This dataset contains 14 different features such as air temperature, atmospheric pressure, and humidity. 
These were collected every 10 minutes, beginning in 2003. 
For efficiency, you will use only the data collected between 2009 and 2016. 
This section of the dataset was prepared by Francois Chollet for his book Deep Learning with Python.
------------------------------------------------------------------------------------------
'''
file_path = PROJECT_ROOT_DIR.joinpath('Data', 'jena_climate/jena_climate_2009_2016.csv.zip')
cacheDir = PROJECT_ROOT_DIR.joinpath('Data', 'jena_climate')

zip_path = tf.keras.utils.get_file(
                origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
                fname=file_path,
                extract=True,
                cache_dir=cacheDir
            )

csv_path = PROJECT_ROOT_DIR.joinpath('Data', 'jena_climate', 'datasets', 'jena_climate_2009_2016.csv')

df = pd.read_csv(csv_path)

# Let's take a glance at the data.
print('df.head() = \n{0}\n'.format(df.head()))

'''
----------------------------------------------------------------------------------------
As you can see above, an observation is recorded every 10 mintues. 
This means that, for a single hour, you will have 6 observations. 
Similarly, a single day will contain 144 (6x24) observations.

Given a specific time, let's say you want to predict the temperature 6 hours in the future. 
In order to make this prediction, you choose to use 5 days of observations. 
Thus, you would create a window containing the last 720(5x144) observations to train the model. 
Many such configurations are possible, making this dataset a good one to experiment with.

The function below returns the above described windows of time for the model to train on. 
The parameter history_size is the size of the past window of information. 
The target_size is how far in the future does the model need to learn to predict. 
The target_size is the label that needs to be predicted.
-----------------------------------------------------------------------------------------
'''
def univariate_data(dataset, start_index, end_index, history_size, target_size):
    data = []
    labels = []

    start_index = start_index + history_size
    if end_index is None:
        end_index = len(dataset) - target_size

    for i in range(start_index, end_index):
        indices = range(i-history_size, i)
        # Reshape data from (history_size,) to (history_size, 1)
        data.append(np.reshape(dataset[indices], (history_size, 1)))
        labels.append(dataset[i+target_size])
    return np.array(data), np.array(labels)

'''
----------------------------------------------------------------------------------------
In both the following tutorials, the first 300,000 rows of the data will be the training dataset,  
and there remaining will be the validation dataset. 
This amounts to ~2100 days worth of training data.
----------------------------------------------------------------------------------------
'''
TRAIN_SPLIT = 300000

'''
---------------------------------------------------------------------------------------
Setting seed to ensure reproducibility.
---------------------------------------------------------------------------------------
'''
tf.random.set_seed(13)

print   (
        '---------------------------------------------------------------------------------\n'
        '      Part 1: Forecast a univariate time series                                  \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
First, you will train a model using only a single feature (temperature), 
and use it to make predictions for that value in the future.

Let's first extract only the temperature from the dataset.
------------------------------------------------------------------------------------------
'''
uni_data = df['T (degC)']
uni_data.index = df['Date Time']
uni_data.head()

'''
------------------------------------------------------------------------------------------
Let's observe how this data looks across time.
------------------------------------------------------------------------------------------
'''
uni_data.plot(subplots=True)
plt.show()

uni_data = uni_data.values

'''
-----------------------------------------------------------------------------------------
It is important to scale features before training a neural network. 
Standardization is a common way of doing this scaling by subtracting the mean 
and dividing by the standard deviation of each feature.
You could also use a tf.keras.utils.normalize method 
that rescales the values into a range of [0,1].

Note: 
The mean and standard deviation should only be computed using the training data.
-----------------------------------------------------------------------------------------
'''
uni_train_mean = uni_data[:TRAIN_SPLIT].mean()
uni_train_std = uni_data[:TRAIN_SPLIT].std()

'''
-----------------------------------------------------------------------------------------
Let's standardize the data.
-----------------------------------------------------------------------------------------
'''
uni_data = (uni_data-uni_train_mean)/uni_train_std

'''
-----------------------------------------------------------------------------------------
Let's now create the data for the univariate model. 
For part 1, the model will be given the last 20 recorded temperature observations, 
and needs to learn to predict the temperature at the next time step.
-----------------------------------------------------------------------------------------
'''
univariate_past_history = 20
univariate_future_target = 0

x_train_uni, y_train_uni = univariate_data(
                                uni_data, 0, TRAIN_SPLIT,
                                univariate_past_history,
                                univariate_future_target
                            )

x_val_uni, y_val_uni = univariate_data(
                            uni_data, TRAIN_SPLIT, None,
                            univariate_past_history,
                            univariate_future_target
                        )

'''
---------------------------------------------------------------------------------------
This is what the univariate_data function returns.
---------------------------------------------------------------------------------------
'''
print ('Single window of past history')
print (x_train_uni[0])
print ('\n Target temperature to predict')
print (y_train_uni[0])

'''
--------------------------------------------------------------------------------------
Now that the data has been created, let's take a look at a single example. 
The information given to the network is given in blue, and it must predict the value at the red cross.
--------------------------------------------------------------------------------------
'''
def create_time_steps(length):
    time_steps = []
    for i in range(-length, 0, 1):
        time_steps.append(i)
    return time_steps

def show_plot(plot_data, delta, title):
    labels = ['History', 'True Future', 'Model Prediction']
    marker = ['.-', 'rx', 'go']
    time_steps = create_time_steps(plot_data[0].shape[0])
    if delta:
        future = delta
    else:
        future = 0

    plt.title(title)
    for i, x in enumerate(plot_data):
        if i:
            plt.plot(future, plot_data[i], marker[i], markersize=10, label=labels[i])
        else:
            plt.plot(time_steps, plot_data[i].flatten(), marker[i], label=labels[i])
    plt.legend()
    plt.xlim([time_steps[0], (future+5)*2])
    plt.xlabel('Time-Step')
    return plt

show_plot([x_train_uni[0], y_train_uni[0]], 0, 'Sample Example')
plt.show()

print   (
        '---------------------------------------------------------------------------------\n'
        '      Baseline                                                                   \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Before proceeding to train a model, let's first set a simple baseline. 
Given an input point, the baseline method looks at all the history 
and predicts the next point to be the average of the last 20 observations.
------------------------------------------------------------------------------------------
'''
def baseline(history):
    return np.mean(history)

show_plot(
        [x_train_uni[0], 
        y_train_uni[0], 
        baseline(x_train_uni[0])], 
        0, 
        'Baseline Prediction Example'
    )

plt.show()

'''
-----------------------------------------------------------------------------------------
Let's see if you can beat this baseline using a recurrent neural network.
-----------------------------------------------------------------------------------------
'''
print   (
        '---------------------------------------------------------------------------------\n'
        '      Recurrent neural network                                                   \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
A Recurrent Neural Network (RNN) is a type of neural network well-suited to time series data. 
RNNs process a time series step-by-step, 
maintaining an internal state summarizing the information they've seen so far. 
For more details, read the RNN tutorial. In this tutorial, 
you will use a specialized RNN layer called Long Short Term Memory (LSTM)

Let's now use tf.data to shuffle, batch, and cache the dataset.
-----------------------------------------------------------------------------------------
'''
BATCH_SIZE = 256
BUFFER_SIZE = 10000

train_univariate = tf.data.Dataset.from_tensor_slices((x_train_uni, y_train_uni))
train_univariate = train_univariate.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_univariate = tf.data.Dataset.from_tensor_slices((x_val_uni, y_val_uni))
val_univariate = val_univariate.batch(BATCH_SIZE).repeat()

'''
----------------------------------------------------------------------------------------
The following visualisation should help you understand how the data is represented after batching.
----------------------------------------------------------------------------------------
'''
im = Image.open(PROJECT_ROOT_DIR.joinpath('images', 'time_series.png'))
im.show()
'''
----------------------------------------------------------------------------------------
You will see the LSTM requires the input shape of the data it is being given.
----------------------------------------------------------------------------------------
'''
simple_lstm_model = tf.keras.models.Sequential([
                        tf.keras.layers.LSTM(8, input_shape=x_train_uni.shape[-2:]),
                        tf.keras.layers.Dense(1)
                    ])

simple_lstm_model.compile(optimizer='adam', loss='mae')

'''
----------------------------------------------------------------------------------------
Let's make a sample prediction, to check the output of the model.
----------------------------------------------------------------------------------------
'''
for x, y in val_univariate.take(1):
    print(simple_lstm_model.predict(x).shape)

'''
---------------------------------------------------------------------------------------
Let's train the model now. 
Due to the large size of the dataset,  in the interest of saving time, 
each epoch will only run for 200 steps,  instead of the complete training data as normally done.
---------------------------------------------------------------------------------------
'''
EVALUATION_INTERVAL = 200
EPOCHS = 10

simple_lstm_model.fit(
        train_univariate, 
        epochs=EPOCHS,
        steps_per_epoch=EVALUATION_INTERVAL,
        validation_data=val_univariate, 
        validation_steps=50
    )

print   (
        '---------------------------------------------------------------------------------\n'
        '      Predict using the simple LSTM model                                        \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
---------------------------------------------------------------------------------------
Now that you have trained your simple LSTM, let's try and make a few predictions.
---------------------------------------------------------------------------------------
'''
for x, y in val_univariate.take(3):
    plot = show_plot(
                    [x[0].numpy(), y[0].numpy(),
                    simple_lstm_model.predict(x)[0]], 
                    0, 'Simple LSTM model'
                )
    
    plot.show()

'''
---------------------------------------------------------------------------------------
This looks better than the baseline. 
Now that you have seen the basics, let's move on to part two, 
where you will work with a multivariate time series.
---------------------------------------------------------------------------------------
'''
print   (
        '---------------------------------------------------------------------------------\n'
        '      Part 2: Forecast a multivariate time series                                \n'
        '---------------------------------------------------------------------------------\n'
        )

'''
--------------------------------------------------------------------------------------
The original dataset contains fourteen features. 
For simplicity, this section considers only three of the original fourteen. 
The features used are air temperature, atmospheric pressure, and air density.

To use more features, add their names to this list.
--------------------------------------------------------------------------------------
'''
features_considered = ['p (mbar)', 'T (degC)', 'rho (g/m**3)']

features = df[features_considered]
features.index = df['Date Time']
print('features.head() = \n{0}\n'.format(features.head()))

'''
-------------------------------------------------------------------------------------
Let's have a look at how each of these features vary across time.
-------------------------------------------------------------------------------------
'''
features.plot(subplots=True)
plt.show()

'''
-------------------------------------------------------------------------------------
As mentioned, 
the first step will be to standardize the dataset using the mean and standard deviation of the training data.
-------------------------------------------------------------------------------------
'''
dataset = features.values
data_mean = dataset[:TRAIN_SPLIT].mean(axis=0)
data_std = dataset[:TRAIN_SPLIT].std(axis=0)

dataset = (dataset-data_mean)/data_std

print   (
        '---------------------------------------------------------------------------------\n'
        '      Single step model                                                          \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
----------------------------------------------------------------------------------------
In a single step setup, the model learns to predict a single point in the future based on some history provided.

The below function performs the same windowing task as below, however, here it samples the past observation based on the step size given.
----------------------------------------------------------------------------------------
'''
def multivariate_data(dataset, target, start_index, end_index, history_size,
                        target_size, step, single_step=False):
    data = []
    labels = []

    start_index = start_index + history_size
    if end_index is None:
        end_index = len(dataset) - target_size

    for i in range(start_index, end_index):
        indices = range(i-history_size, i, step)
        data.append(dataset[indices])

        if single_step:
            labels.append(target[i+target_size])
        else:
            labels.append(target[i:i+target_size])

    return np.array(data), np.array(labels)

'''
-----------------------------------------------------------------------------------------
In this tutorial, 
the network is shown data from the last five (5) days, i.e. 720 observations that are sampled every hour. 
The sampling is done every one hour since a drastic change is not expected within 60 minutes. 
Thus, 120 observation represent history of the last five days. 
For the single step prediction model, the label for a datapoint is the temperature 12 hours into the future. 
In order to create a label for this, the temperature after 72(12*6) observations is used.
-----------------------------------------------------------------------------------------
'''
past_history = 720
future_target = 72
STEP = 6

x_train_single, y_train_single = multivariate_data(
                                    dataset, dataset[:, 1], 0,
                                    TRAIN_SPLIT, past_history,
                                    future_target, STEP,
                                    single_step=True
                                )

x_val_single, y_val_single = multivariate_data(
                                    dataset, dataset[:, 1],
                                    TRAIN_SPLIT, None, past_history,
                                    future_target, STEP,
                                    single_step=True
                                )

'''
----------------------------------------------------------------------------------------
Let's look at a single data-point.
----------------------------------------------------------------------------------------
'''
print ('Single window of past history : {}'.format(x_train_single[0].shape))

train_data_single = tf.data.Dataset.from_tensor_slices((x_train_single, y_train_single))
train_data_single = train_data_single.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_data_single = tf.data.Dataset.from_tensor_slices((x_val_single, y_val_single))
val_data_single = val_data_single.batch(BATCH_SIZE).repeat()

single_step_model = tf.keras.models.Sequential()
single_step_model.add(tf.keras.layers.LSTM(32, input_shape=x_train_single.shape[-2:]))
single_step_model.add(tf.keras.layers.Dense(1))

single_step_model.compile(optimizer=tf.keras.optimizers.RMSprop(), loss='mae')

'''
---------------------------------------------------------------------------------------
Let's check out a sample prediction.
---------------------------------------------------------------------------------------
'''
for x, y in val_data_single.take(1):
    print(single_step_model.predict(x).shape)

single_step_history = single_step_model.fit(
                            train_data_single, epochs=EPOCHS,
                            steps_per_epoch=EVALUATION_INTERVAL,
                            validation_data=val_data_single,
                            validation_steps=50
                        )

def plot_train_history(history, title):
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(loss))

    plt.figure()

    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title(title)
    plt.legend()

    plt.show()

plot_train_history(
        single_step_history,
        'Single Step Training and validation loss'
    )

print   (
        '---------------------------------------------------------------------------------\n'
        '      Predict a single step future                                               \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Now that the model is trained, let's make a few sample predictions. 
The model is given the history of three features over the past five days sampled every hour (120 data-points), 
since the goal is to predict the temperature, the plot only displays the past temperature. 
The prediction is made one day into the future (hence the gap between the history and prediction).
------------------------------------------------------------------------------------------
'''
for x, y in val_data_single.take(3):
    plot = show_plot(
                [x[0][:, 1].numpy(), y[0].numpy(),
                single_step_model.predict(x)[0]], 12,
                'Single Step Prediction'
            )
    
    plot.show()

print   (
        '---------------------------------------------------------------------------------\n'
        '      Multi-Step model                                                           \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
-----------------------------------------------------------------------------------------
In a multi-step prediction model, given a past history, the model needs to learn to predict a range of future values. 
Thus, unlike a single step model, where only a single future point is predicted, a multi-step model predict a sequence of the future.

For the multi-step model, the training data again consists of recordings over the past five days sampled every hour. 
However, here, the model needs to learn to predict the temperature for the next 12 hours. 
Since an obversation is taken every 10 minutes, the output is 72 predictions. 
For this task, the dataset needs to be prepared accordingly, thus the first step is just to create it again, but with a different target window.
-----------------------------------------------------------------------------------------
'''
future_target = 72
x_train_multi, y_train_multi = multivariate_data(
                                    dataset, dataset[:, 1], 0,
                                    TRAIN_SPLIT, past_history,
                                    future_target, STEP
                                )

x_val_multi, y_val_multi = multivariate_data(
                                dataset, dataset[:, 1],
                                TRAIN_SPLIT, None, past_history,
                                future_target, STEP
                            )

'''
-----------------------------------------------------------------------------------------
Let's check out a sample data-point.
-----------------------------------------------------------------------------------------
'''

print ('Single window of past history : {}'.format(x_train_multi[0].shape))
print ('\n Target temperature to predict : {}'.format(y_train_multi[0].shape))

train_data_multi = tf.data.Dataset.from_tensor_slices((x_train_multi, y_train_multi))
train_data_multi = train_data_multi.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_data_multi = tf.data.Dataset.from_tensor_slices((x_val_multi, y_val_multi))
val_data_multi = val_data_multi.batch(BATCH_SIZE).repeat()

'''
----------------------------------------------------------------------------------------
Plotting a sample data-point.
----------------------------------------------------------------------------------------
'''
def multi_step_plot(history, true_future, prediction):
    plt.figure(figsize=(12, 6))
    num_in = create_time_steps(len(history))
    num_out = len(true_future)

    plt.plot(num_in, np.array(history[:, 1]), label='History')

    plt.plot(
            np.arange(num_out)/STEP, np.array(true_future), 'bo',
            label='True Future'
        )
    
    if prediction.any():
        plt.plot(
                np.arange(num_out)/STEP, np.array(prediction), 'ro',
                label='Predicted Future'
            )
    
    plt.legend(loc='upper left')
    plt.show()

'''
----------------------------------------------------------------------------------------
In this plot and subsequent similar plots, 
the history and the future data are sampled every hour.
----------------------------------------------------------------------------------------
'''
for x, y in train_data_multi.take(1):
    multi_step_plot(x[0], y[0], np.array([0]))

'''
----------------------------------------------------------------------------------------
Since the task here is a bit more complicated than the previous task, 
the model now consists of two LSTM layers. 
Finally, since 72 predictions are made, the dense layer outputs 72 predictions.
----------------------------------------------------------------------------------------
'''
multi_step_model = tf.keras.models.Sequential()

multi_step_model.add(
        tf.keras.layers.LSTM(32,
        return_sequences=True,
        input_shape=x_train_multi.shape[-2:])
    )

multi_step_model.add(tf.keras.layers.LSTM(16, activation='relu'))
multi_step_model.add(tf.keras.layers.Dense(72))

multi_step_model.compile(optimizer=tf.keras.optimizers.RMSprop(clipvalue=1.0), loss='mae')

'''
----------------------------------------------------------------------------------------
Let's see how the model predicts before it trains.
----------------------------------------------------------------------------------------
'''
for x, y in val_data_multi.take(1):
    print (multi_step_model.predict(x).shape)

multi_step_history = multi_step_model.fit(
                            train_data_multi, epochs=EPOCHS,
                            steps_per_epoch=EVALUATION_INTERVAL,
                            validation_data=val_data_multi,
                            validation_steps=50
                        )

plot_train_history(multi_step_history, 'Multi-Step Training and validation loss')

print   (
        '---------------------------------------------------------------------------------\n'
        '      Predict a multi-step future                                                \n'
        '---------------------------------------------------------------------------------\n'
        )
'''
------------------------------------------------------------------------------------------
Let's now have a look at how well your network has learnt to predict the future.
------------------------------------------------------------------------------------------
'''
for x, y in val_data_multi.take(3):
    multi_step_plot(x[0], y[0], multi_step_model.predict(x)[0])

print   (
        '------------------------------------------------------------------------------------------------------\n'
        '       finished         struct_time_series_forcasting.py                  (2020/05/16)                \n'
        '------------------------------------------------------------------------------------------------------\n'
        )
print()
print()
print()