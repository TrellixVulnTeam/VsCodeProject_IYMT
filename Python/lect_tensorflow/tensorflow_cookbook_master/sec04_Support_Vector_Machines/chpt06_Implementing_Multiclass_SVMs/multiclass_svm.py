'''
# Multi-class (Nonlinear) SVM Example
#
# This function wll illustrate how to
# implement the gaussian kernel with
# multiple classes on the iris dataset.
#
# Gaussian Kernel:
# K(x1, x2) = exp(-gamma * abs(x1 - x2)^2)
#
# X : (Sepal Length, Petal Width)
# Y: (I. setosa, I. virginica, I. versicolor) (3 classes)
#
# Basic idea: introduce an extra dimension to do
# one vs all classification.
#
# The prediction of a point will be the category with
# the largest margin or distance to boundary.
'''

# import required libraries
from __future__ import absolute_import, division, print_function, unicode_literals
import os
import datetime
from packaging import version
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets

print(__doc__)

# Display current path
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print('PROJECT_ROOT_DIR = \n{0}\n'.format(PROJECT_ROOT_DIR))

# Display tensorflow version
print("TensorFlow version: ", tf.version.VERSION)
assert version.parse(tf.version.VERSION).release[0] >= 2, "This notebook requires TensorFlow 2.0 or above."

# Load the data
# iris.data = [(Sepal Length, Sepal Width, Petal Length, Petal Width)]
iris = datasets.load_iris()

x_vals = np.array([[x[0], x[3]] for x in iris.data])
y_vals1 = np.array([1 if y == 0 else -1 for y in iris.target])
y_vals2 = np.array([1 if y == 1 else -1 for y in iris.target])
y_vals3 = np.array([1 if y == 2 else -1 for y in iris.target])

y_vals = np.array([y_vals1, y_vals2, y_vals3])

# display Correlation between Sepal Length and Petal Width due to variety
class1_x = [x[0] for i, x in enumerate(x_vals) if iris.target[i] == 0]
class1_y = [x[1] for i, x in enumerate(x_vals) if iris.target[i] == 0]
class2_x = [x[0] for i, x in enumerate(x_vals) if iris.target[i] == 1]
class2_y = [x[1] for i, x in enumerate(x_vals) if iris.target[i] == 1]
class3_x = [x[0] for i, x in enumerate(x_vals) if iris.target[i] == 2]
class3_y = [x[1] for i, x in enumerate(x_vals) if iris.target[i] == 2]

plt.plot(class1_x, class1_y, 'ro', label='setosa')
plt.plot(class2_x, class2_y, 'kx', label='versicolor')
plt.plot(class3_x, class3_y, 'gv', label='irginica')
plt.title('raw data on Iris Data')
plt.xlabel('Petal Length')
plt.ylabel('Sepal Width')
plt.legend(loc='lower right')
plt.ylim([-0.5, 3.0])
plt.xlim([3.5, 8.5])
plt.show()


# Declare batch size
batch_size = 50

# Declare gamma
Gam = -10.0

# Create variables for svm
b = tf.cast(tf.Variable(tf.random.normal(shape=[3, batch_size])), dtype=tf.float32)

# Declare function to do reshape/batch multiplication
def reshape_matmul(mat, _size):
    v1 = tf.expand_dims(mat, 1)
    v2 = tf.reshape(v1, [3, _size, 1])
    return tf.matmul(v2, v1)

def loss(input_x, bb, g, targets, bat_size):
    # Gaussian (RBF) kernel
    gamma = tf.cast(tf.constant(g), dtype=tf.float32)
    dist = tf.reduce_sum(tf.square(input_x), 1)
    dist = tf.reshape(dist, [-1, 1])
    sq_dists = tf.multiply(2., tf.matmul(input_x, tf.transpose(input_x)))
    my_kernel = tf.exp(tf.multiply(gamma, tf.abs(sq_dists)))

    # Compute SVM Model
    first_term = tf.reduce_sum(bb)
    b_vec_cross = tf.matmul(tf.transpose(bb), bb)
    y_target_cross = reshape_matmul(targets, bat_size)

    second_term = tf.reduce_sum(tf.multiply(my_kernel, tf.multiply(b_vec_cross, y_target_cross)), [1, 2])
    return tf.reduce_sum(tf.negative(tf.subtract(first_term, second_term)))

def grad(input_x, bb, g, targets, bat_size):
    with tf.GradientTape() as tape:
        loss_value = loss(input_x, bb, g, targets, bat_size)
    return tape.gradient(loss_value, [bb])

def predection(input_x, bb, g, targets, pred_grid):
    # Gaussian (RBF) prediction kernel
    rA = tf.reshape(tf.reduce_sum(tf.square(input_x), 1), [-1, 1])
    rB = tf.reshape(tf.reduce_sum(tf.square(pred_grid), 1), [-1, 1])
    pred_sq_dist = tf.add(tf.subtract(rA, tf.multiply(2., tf.matmul(input_x, tf.transpose(pred_grid)))), tf.transpose(rB))
    pred_kernel = tf.exp(tf.multiply(g, tf.abs(pred_sq_dist)))

    prediction_output = tf.matmul(tf.multiply(targets, bb), pred_kernel)
    return tf.argmax(prediction_output - tf.expand_dims(tf.reduce_mean(prediction_output, 1), 1), 0)

def accuracy(input_x, bb, g, targets, pred_grid):
    prediction_value = predection(input_x, bb, g, targets, pred_grid)
    return tf.reduce_mean(tf.cast(tf.equal(prediction_value, tf.argmax(targets, 0)), tf.float32))

# Declare optimizer
optimizer = tf.keras.optimizers.SGD(0.01)

# Training loop
loss_vec = []
batch_accuracy = []

for i in range(100):
    rand_index = np.random.choice(len(x_vals), size=batch_size)
    rand_x = tf.cast(x_vals[rand_index], dtype=tf.float32)
    rand_y = tf.cast(y_vals[:, rand_index], dtype=tf.float32)
    
    grads = grad(rand_x, b, Gam, rand_y, batch_size)
    optimizer.apply_gradients(zip(grads, [b]))
    
    temp_loss = loss(rand_x, b, Gam, rand_y, batch_size)
    loss_vec.append(temp_loss)
    
    acc_temp = accuracy(rand_x, b, Gam, rand_y, rand_x)
    batch_accuracy.append(acc_temp)
    
    if (i + 1) % 25 == 0:
        print('Step #{0}'.format(i + 1))
        print('Loss = {0}\n'.format(temp_loss.numpy()))

# Create a mesh to plot points in
x_min, x_max = x_vals[:, 0].min() - 1, x_vals[:, 0].max() + 1
y_min, y_max = x_vals[:, 1].min() - 1, x_vals[:, 1].max() + 1

xx, yy = np.meshgrid(
            np.arange(x_min, x_max, 0.02),
            np.arange(y_min, y_max, 0.02)
        )

grid_points = tf.cast(np.c_[xx.ravel(), yy.ravel()], dtype=tf.float32)
grid_predictions = predection(rand_x, b, Gam, rand_y, grid_points).numpy()
grid_predictions = grid_predictions.reshape(xx.shape)

# Plot points and grid
plt.contourf(xx, yy, grid_predictions, cmap=plt.cm.Paired, alpha=0.8)
plt.plot(class1_x, class1_y, 'ro', label='I. setosa')
plt.plot(class2_x, class2_y, 'kx', label='I. versicolor')
plt.plot(class3_x, class3_y, 'gv', label='I. virginica')
plt.title('Gaussian SVM Results on Iris Data')
plt.xlabel('Petal Length')
plt.ylabel('Sepal Width')
plt.legend(loc='lower right')
plt.ylim([-0.5, 3.0])
plt.xlim([3.5, 8.5])
plt.show()

# Plot batch accuracy
plt.plot(batch_accuracy, 'k-', label='Accuracy')
plt.title('Batch Accuracy')
plt.xlabel('Generation')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

# Plot loss over time
plt.plot(loss_vec, 'k-')
plt.title('Loss per Generation')
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()

# Evaluations on new/unseen data

date_today = datetime.date.today()

print   (
        '------------------------------------------------------------------------------------------------------\n'
    )

print   (
        '       finished         multiclass_svm.py                                          ({0})             \n'.format(date_today)
    )

print(
        '------------------------------------------------------------------------------------------------------\n'
    )
print()
print()
print()