"""
Learning Optimal Tic-Tac-Toe Moves via a Neural Network
-------------------------------------------------------
We will build a one-hidden layer neural network
 to predict the optimal response given a set
 of tic-tac-toe boards.

"""

import os
from cpuinfo import get_cpu_info
import datetime
from packaging import version
import tensorflow as tf
import matplotlib.pyplot as plt
import csv
import numpy as np
import random
from tensorflow.python.framework import ops

print(__doc__)

'''
--------------------------------------------
In casee of windows, os name is 'nt'.
In case of linux, os name is 'posix'.
--------------------------------------------
'''

if os.name == 'nt':
    print(
        '--------------------------------------------------------------------------\n'
        '                      cpu information                                     \n'
        '--------------------------------------------------------------------------\n'
    )
    # display the using cpu information
    for key, value in get_cpu_info().items():
        print("{0}: {1}".format(key, value))

    print()
    print()

# Display current path
PROJECT_ROOT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
print('PROJECT_ROOT_DIR = \n{0}\n'.format(PROJECT_ROOT_DIR))

# Display tensorflow version
print("TensorFlow version: {0}\n".format(tf.version.VERSION))
assert version.parse(tf.version.VERSION).release[0] >= 2, "This notebook requires TensorFlow 2.0 or above."

# Definition of X's, O's, and empty spots:
# X = 1
# O = -1
# empty = 0
# response on 1-9 grid for placement of next '1'

# For example, the 'test_board' is:
#
#   O  |  -  |  -
# -----------------
#   X  |  O  |  O
# -----------------
#   -  |  -  |  X
#
# board above = [-1, 0, 0, 1, -1, -1, 0, 0, 1]
# Optimal response would be position 6, where
# the position numbers are:
#
#   0  |  1  |  2
# -----------------
#   3  |  4  |  5
# -----------------
#   6  |  7  |  8

# Test board optimal response:
response = 6
# Set batch size and five different symmetries of board positions
batch_size = 50
symmetry = ['rotate180', 'rotate90', 'rotate270', 'flip_v', 'flip_h']


# Print a board
def print_board(board):
    symbols = ['O', ' ', 'X']
    board_plus1 = [int(x) + 1 for x in board]
    board_line1 = ' {} | {} | {}'.format(symbols[board_plus1[0]],
                                         symbols[board_plus1[1]],
                                         symbols[board_plus1[2]])
    board_line2 = ' {} | {} | {}'.format(symbols[board_plus1[3]],
                                         symbols[board_plus1[4]],
                                         symbols[board_plus1[5]])
    board_line3 = ' {} | {} | {}'.format(symbols[board_plus1[6]],
                                         symbols[board_plus1[7]],
                                         symbols[board_plus1[8]])
    print(board_line1)
    print('___________')
    print(board_line2)
    print('___________')
    print(board_line3)


# Given a board, a response, and a transformation, get the new board+response
def get_symmetry(board, play_response, transformation):
    """
    :param board: list of integers 9 long:
     opposing mark = -1
     friendly mark = 1
     empty space = 0
    :param play_response: integer of where response is (0-8)
    :param transformation: one of five transformations on a board:
     'rotate180', 'rotate90', 'rotate270', 'flip_v', 'flip_h'
    :return: tuple: (new_board, new_response)
    """
    if transformation == 'rotate180':
        new_response = 8 - play_response
        return board[::-1], new_response

    elif transformation == 'rotate90':
        new_response = [6, 3, 0, 7, 4, 1, 8, 5, 2].index(play_response)
        tuple_board = list(zip(*[board[6:9], board[3:6], board[0:3]]))
        return [value for item in tuple_board for value in item], new_response

    elif transformation == 'rotate270':
        new_response = [2, 5, 8, 1, 4, 7, 0, 3, 6].index(play_response)
        tuple_board = list(zip(*[board[0:3], board[3:6], board[6:9]]))[::-1]
        return [value for item in tuple_board for value in item], new_response

    elif transformation == 'flip_v':
        new_response = [6, 7, 8, 3, 4, 5, 0, 1, 2].index(play_response)
        return board[6:9] + board[3:6] + board[0:3], new_response

    elif transformation == 'flip_h':  # flip_h = rotate180, then flip_v
        new_response = [2, 1, 0, 5, 4, 3, 8, 7, 6].index(play_response)
        new_board = board[::-1]
        return new_board[6:9] + new_board[3:6] + new_board[0:3], new_response

    else:
        raise ValueError('Method not implemented.')


# Read in board move csv file
def get_moves_from_csv(csv_file):
    """
    :param csv_file: csv file location containing the boards w/ responses
    :return: moves: list of moves with index of best response
    """
    play_moves = []
    with open(csv_file, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            play_moves.append(([int(x) for x in row[0:9]], int(row[9])))

    return play_moves


# Get random board with optimal move
def get_rand_move(play_moves, rand_transforms=2):
    """
    :param play_moves: list of the boards w/responses
    :param rand_transforms: how many random transforms performed on each
    :return: (board, response), board is a list of 9 integers, response is 1 int
    """
    (board, play_response) = random.choice(play_moves)
    possible_transforms = ['rotate90', 'rotate180', 'rotate270', 'flip_v', 'flip_h']
    for _ in range(rand_transforms):
        random_transform = random.choice(possible_transforms)
        (board, play_response) = get_symmetry(board, play_response, random_transform)
    return board, play_response


# Get list of optimal moves w/ responses
moves = get_moves_from_csv(os.path.join(PROJECT_ROOT_DIR, 'base_tic_tac_toe_moves.csv'))

# Create a train set:
train_length = 500
train_set = []
for t in range(train_length):
    train_set.append(get_rand_move(moves))

# To see if the network learns anything new, we will remove
# all instances of the board [-1, 0, 0, 1, -1, -1, 0, 0, 1],
# which the optimal response will be the index '6'.  We will
# Test this at the end.
test_board = [-1, 0, 0, 1, -1, -1, 0, 0, 1]
train_set = [x for x in train_set if x[0] != test_board]


def init_weights(shape):
    return tf.Variable(tf.random.normal(shape), dtype=tf.float32)


def model(X, A1, A2, bias1, bias2):
    layer1 = tf.nn.sigmoid(tf.add(tf.matmul(X, A1), bias1))
    layer2 = tf.add(tf.matmul(layer1, A2), bias2)
    # Note: we don't take the softmax at the end because our cost function does that for us
    return layer2

A1 = init_weights([9, 81])
bias1 = init_weights([81])
A2 = init_weights([81, 9])
bias2 = init_weights([9])

def loss(X, Y, A1, A2, bias1, bias2):
    X = tf.cast(X, dtype=tf.float32)
    Y = tf.cast(Y, dtype=tf.float32)

    model_output = model(X, A1, A2, bias1, bias2)
    return tf.math.reduce_mean(input_tensor=tf.nn.sparse_softmax_cross_entropy_with_logits(labels=Y, logits=model_output), dtype=tf.float32)

def grad(X, Y, A1, A2, bias1, bias2):
    with tf.GradientTape() as tape:
        loss_value = loss(X, Y, A1, A2, bias1, bias2)
    return tape.gradient(loss_value, [A1, A2, bias1, bias2])


# Declare optimizer
optimizer = tf.keras.optimizers.SGD(learning_rate=0.025)


def prediction(X, A1, A2, bias1, bias2):
    model_output_value = model(X, A1, A2, bias1, bias2)
    return tf.argmax(input=model_output_value, axis=1)


loss_vec = []

for i in range(10000):
    rand_indices = np.random.choice(range(len(train_set)), batch_size, replace=False)
    batch_data = [train_set[i] for i in rand_indices]
    x_input = tf.convert_to_tensor([x[0] for x in batch_data], dtype=tf.float32)
    y_target = tf.convert_to_tensor(np.array([y[1] for y in batch_data]), dtype=tf.float32)

    grads = grad(x_input, y_target, A1, A2, bias1, bias2)
    optimizer.apply_gradients(zip(grads, [A1, A2, bias1, bias2]))

    temp_loss = loss(x_input, y_target, A1, A2, bias1, bias2)
    loss_vec.append(temp_loss.numpy())
    if i % 500 == 0:
        print('Iteration: {}, Loss: {}'.format(i, temp_loss.numpy()))

# Print loss
plt.plot(loss_vec, 'k-', label='Loss')
plt.title('Loss (MSE) per Generation')
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()

# Make Prediction:
test_boards = [test_board]
feed_dict = {X: test_boards}

logits = model(test_boards, A1, A2, bias1, bias2)

predictions = prediction(test_boards, A1, A2, bias1, bias2)
print(predictions)


# Declare function to check for win
def check(board):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for ix in range(len(wins)):
        if board[wins[ix][0]] == board[wins[ix][1]] == board[wins[ix][2]] == 1.:
            return 1
        elif board[wins[ix][0]] == board[wins[ix][1]] == board[wins[ix][2]] == -1.:
            return 1
    return 0


# Let's play against our model
game_tracker = [0., 0., 0., 0., 0., 0., 0., 0., 0.]
win_logical = False
num_moves = 0
while not win_logical:
    player_index = input('Input index of your move (0-8): ')
    num_moves += 1
    # Add player move to game
    game_tracker[int(player_index)] = 1.

    # Get model's move by first getting all the logits for each index
    [potential_moves] = model([game_tracker], A1, A2, bias1, bias2)
    
    # Now find allowed moves (where game tracker values = 0.0)
    allowed_moves = [ix for ix, x in enumerate(game_tracker) if x == 0.0]

    # Find best move by taking argmax of logits if they are in allowed moves
    model_move = np.argmax([x if ix in allowed_moves else -999.0 for ix, x in enumerate(potential_moves)])

    # Add model move to game
    game_tracker[int(model_move)] = -1.

    print('Model has moved')
    print_board(game_tracker)

    # Now check for win or too many moves
    if check(game_tracker) == 1 or num_moves >= 5:
        print('Game Over!')
        win_logical = True

date_today = datetime.date.today()

print(
    '------------------------------------------------------------------------------------------------------\n'
)

print(
    '       finished         tic_tac_toe_moves.py                ({0})   \n'.format(date_today)
)

print(
    '------------------------------------------------------------------------------------------------------\n'
)
print()
print()
print()