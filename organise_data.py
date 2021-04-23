#basic 
import os
import numpy as np
import matplotlib.pyplot as plt

#tensorflow 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models


#DATA_PATH = '/content/data/???'
TRAIN_SPLIT = 'Dataset/TrainAndValList/train.lst'
TEST_SPLIT = 'Dataset/TrainAndValList/validation.lst'
DATA = 'Dataset/Low-Resolution/200-n000008-Airedale'

# Data handling
# FROM https://github.com/RuoyiDu/PMG-Progressive-Multi-Granularity-Training/blob/master/organize_dataset.py
split = {}

# Creating folders for training and test data
with open(TRAIN_SPLIT) as fp:
   line = fp.readline()
   labels = []

   while line:
        line = line.strip()
        tmp = line.replace('.//', '')
        class_name, _ = tmp.split('/')
        #class_name, _, _ = line.split('-')
        #_, _, class_name = class_name.split('/')
        
        dataFolder_train = 'data/dataset/train/' + class_name
        dataFolder_test = 'data/dataset/test/' + class_name
        labels.append(class_name)
        if not os.path.exists(dataFolder_train):
          os.makedirs(dataFolder_train)
        if not os.path.exists(dataFolder_test):
          os.makedirs(dataFolder_test) 
        line = fp.readline()

# Creating structure split for training data and test data
with open(TRAIN_SPLIT) as fp:
   line = fp.readline()
   while line:
       line = line.strip()
       _, _, image_name_id = line.split('-')
       _, image_id = image_name_id.split('/')
       _, image_id = image_id.split('n')
       image_id, _ = image_id.split('.')
       image_id.replace('n', '')
       split[int(image_id)] = 'train'
       line = fp.readline()

with open(TEST_SPLIT) as fp:
   line = fp.readline()
   while line:
       line = line.strip()
       image_class_, _, image_name_id = line.split('-')
       _, image_id = image_name_id.split('/')
       _, _, image_class = image_class_.split('/')
       _, image_id = image_id.split('n')
       image_id, _ = image_id.split('.')
       image_id.replace('n', '')
       split[int(image_id)] = 'test'
       tmp = line.replace('.//', '')
       line = fp.readline()

# Put training data into correct directories
# TODO
import shutil, os
from pathlib import Path
with open(TRAIN_SPLIT, mode='r', encoding='utf-8-sig') as fp:
   line = fp.readline()
   while line:
       line = line.strip()
       tmp = line.replace('.//', '')
       class_name, _ = tmp.split('/')

       _, _, image_name_id = line.split('-')
       _, jpg_name = image_name_id.split('/')
   
       src = os.path.join('Dataset/Low-Resolution/', tmp)
       dst = os.path.join('data/dataset/train', class_name, jpg_name)
       shutil.move(src, dst)
       line = fp.readline()

with open(TEST_SPLIT, mode='r', encoding='utf-8-sig') as fp:
   line = fp.readline()
   while line:
       line = line.strip()
       tmp = line.replace('.//', '')
       class_name, _ = tmp.split('/')

       _, _, image_name_id = line.split('-')
       _, jpg_name = image_name_id.split('/')
   
       src = os.path.join('Dataset/Low-Resolution/', tmp)
       dst = os.path.join('data/dataset/test', class_name, jpg_name)
       shutil.move(src, dst)
       line = fp.readline()
