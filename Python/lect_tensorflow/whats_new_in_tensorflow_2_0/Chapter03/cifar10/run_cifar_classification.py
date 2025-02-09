# coding: utf-8
""" CustomEstimator"""
# common library
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import os
import argparse
import tensorflow as tf

sys.path.append(r'/home/munezou/VsCodeProject/Python/lect_tensorflow/whats_new_in_tensorflow_2_0/Chapter03/cifar10/')

from .cifar10_classification import Cifar10Classification

def main(argv):
    """ main routing """
    if argv is not None:
        print('argv: {}'.format(argv))

    print("Parsing arguments.")
    parser = argparse.ArgumentParser()
    parser.add_argument('-do', '--dropout_rate',
        type=float, help='drop out rate')
    parser.add_argument('-b', '--batch_size',
        type=int, help='Training / test batch size')
    parser.add_argument('-e', '--num_epochs',
        type=int, help='Num of epochs')
    parser.add_argument('-spe', '--steps_per_epoch',
        type=int, help='Steps per epoch')
    parser.add_argument('-lr', '--learning_rate',
        type=float, help='Learning rate')
    args = parser.parse_args()

    batch_size = args.batch_size
    num_epochs = args.num_epochs
    steps_per_epoch = args.steps_per_epoch
    
    learning_rate = args.learning_rate
    dropout_rate = args.dropout_rate

    cifar_classification = Cifar10Classification(batch_size)
    cifar_classification.build_model(model_dir='models/Cifar10ConvModel', 
        learning_rate=learning_rate, dropout_rate=dropout_rate)

    cifar_classification.train(num_epochs, steps_per_epoch)
    cifar_classification.check_test_accuracy()

if __name__ == '__main__':
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
    tf.compat.v1.app.run(main)
