from unicodedata import name
import numpy as np
import pydot
import pandas as pd
np.random.seed(42)  # for reproducibility
import os
import math
import h5py
from sklearn.metrics import roc_auc_score
import tensorflow as tf
# tf.compat.v1.disable_eager_execution()
# from keras.utils import np_utils
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import roc_curve,auc,roc_auc_score,matthews_corrcoef,accuracy_score,confusion_matrix
from sklearn.metrics import f1_score, precision_recall_curve, roc_auc_score,confusion_matrix ,precision_recall_curve,average_precision_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout, Activation, Convolution2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam
import sys
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import os

model = tf.keras.models.load_model('/mnt/raid5/data3/gawang/BERTpre6s/saved_model/model_EC.h5')
