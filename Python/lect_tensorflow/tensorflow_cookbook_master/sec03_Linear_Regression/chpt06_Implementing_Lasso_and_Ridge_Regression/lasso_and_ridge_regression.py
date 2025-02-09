'''
# LASSO and Ridge Regression
# 
# This function shows how to use TensorFlow to solve LASSO or 
# Ridge regression for 
# y = Ax + b
# 
# We will use the iris data, specifically: 
#   y = Sepal Length 
#   x = Petal Width
'''

# import required libraries
from __future__ import absolute_import, division, print_function, unicode_literals
import os
import datetime
from packaging import version
from pathlib import Path
import matplotlib.pyplot as plt
import sys
import numpy as np
import tensorflow as tf
from sklearn import datasets
from tensorflow.python.framework import ops

print(__doc__)

# Display current path
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print('PROJECT_ROOT_DIR = \n{0}\n'.format(PROJECT_ROOT_DIR))

# Display tensorflow version
print("TensorFlow version: ", tf.version.VERSION)
assert version.parse(tf.version.VERSION).release[0] >= 2, "This notebook requires TensorFlow 2.0 or above."


# Specify 'Ridge' or 'LASSO'
regression_type = 'LASSO'
#regression_type = 'Ridge'

###
# Load iris data
###

# iris.data = [(Sepal Length, Sepal Width, Petal Length, Petal Width)]
iris = datasets.load_iris()
x_vals = np.array([x[3] for x in iris.data])
y_vals = np.array([y[0] for y in iris.data])

###
# Model Parameters
###

# Declare batch size
batch_size = 50

# make results reproducible
seed = 13
np.random.seed(seed)
tf.random.set_seed(seed)

# Create variables for linear regression
A = tf.cast(tf.Variable(tf.random.normal(shape=[1,1])), dtype=tf.float32)
b = tf.cast(tf.Variable(tf.random.normal(shape=[1,1])), dtype=tf.float32)

###
# Loss Functions
###

# Select appropriate loss function based on regression type
def loss(method, input_x, aa, bb, targets):
    # Declare model operations
    model_output = tf.add(tf.matmul(input_x, aa), bb)

    if regression_type == 'LASSO':
        # Declare Lasso loss function
        # Lasso Loss = L2_Loss + heavyside_step,
        # Where heavyside_step ~ 0 if A < constant, otherwise ~ 99
        lasso_param = tf.constant(0.9)
        heavyside_step = tf.truediv(1., tf.add(1., tf.exp(tf.multiply(-50., tf.subtract(aa, lasso_param)))))
        regularization_param = tf.multiply(heavyside_step, 99.)
        return tf.add(tf.reduce_mean(tf.square(targets - model_output)), regularization_param)

    elif regression_type == 'Ridge':
        # Declare the Ridge loss function
        # Ridge loss = L2_loss + L2 norm of slope
        ridge_param = tf.constant(1.)
        ridge_loss = tf.reduce_mean(tf.square(aa))
        return tf.expand_dims(tf.add(tf.reduce_mean(tf.square(targets - model_output)), tf.multiply(ridge_param, ridge_loss)), 0)
        
    else:
        tf.print('Invalid regression_type parameter value',file=sys.stderr)
        return None

def grad(method, input_x, aa, bb, targets):
    with tf.GradientTape() as tape:
        loss_value = loss(method, input_x, aa, bb, targets)
    return tape.gradient(loss_value, [aa, bb])

###
# Optimizer
###

# Declare optimizer
optimize = tf.keras.optimizers.SGD(0.001)

###
# Run regression
###

# Training loop
loss_vec = []

for i in range(1500):
    rand_index = np.random.choice(len(x_vals), size=batch_size)
    rand_x = tf.cast(np.transpose([x_vals[rand_index]]), dtype=tf.float32)
    rand_y = tf.cast(np.transpose([y_vals[rand_index]]), dtype=tf.float32)
    grads = grad(regression_type, rand_x, A, b, rand_y)

    optimize.apply_gradients(zip(grads, [A, b]))

    temp_loss = loss(regression_type, rand_x, A, b, rand_y)
    loss_vec.append(temp_loss[0])
    if ( i + 1) % 300 == 0:
        print('Step #{0}  A = {1},  b = {2}'.format(i + 1, A.numpy(), b.numpy()))
        print('Loss = {0}'.format(temp_loss.numpy()))
        print('\n')

###
# Extract regression results
###

# Get the optimal coefficients
[slope] = A.numpy()
[y_intercept] = b.numpy()

# Get best fit line
best_fit = []
for i in x_vals:
    best_fit.append(slope * i + y_intercept)


###
# Plot results
###

# Plot regression line against data points
plt.plot(x_vals, y_vals, 'o', label='Data Points')
plt.plot(x_vals, best_fit, 'r-', label='Best fit line', linewidth=3)
plt.legend(loc='upper left')
plt.title('Sepal Length vs Pedal Width')
plt.xlabel('Pedal Width')
plt.ylabel('Sepal Length')
plt.show()

# Plot loss over time
plt.plot(loss_vec, 'k-')
plt.title(regression_type + ' Loss per Generation')
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()

date_today = datetime.date.today()

print   (
        '------------------------------------------------------------------------------------------------------\n'
    )

print   (
        '       finished         lasso_and_ridge_regression.py                             ({0})             \n'.format(date_today)
    )

print(
        '------------------------------------------------------------------------------------------------------\n'
    )
print()
print()
print()