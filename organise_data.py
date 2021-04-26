#basic 
import os
import numpy as np
import matplotlib.pyplot as plt
import shutil, os
import random


TRAIN_SPLIT = 'Dataset/TrainAndValList/train.lst'
VAL_SPLIT = 'Dataset/TrainAndValList/validation.lst'

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
        dataFolder_val = 'data/dataset/val/' + class_name
        dataFolder_test = 'data/dataset/test/' + class_name
        labels.append(class_name)
        if not os.path.exists(dataFolder_train):
          os.makedirs(dataFolder_train)
        if not os.path.exists(dataFolder_val):
          os.makedirs(dataFolder_val) 
        if not os.path.exists(dataFolder_test):
          os.makedirs(dataFolder_test)
        line = fp.readline()

# # Creating structure split for training data and test data
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

with open(VAL_SPLIT) as fp:
   line = fp.readline()
   while line:
       line = line.strip()
       image_class_, _, image_name_id = line.split('-')
       _, image_id = image_name_id.split('/')
       _, _, image_class = image_class_.split('/')
       _, image_id = image_id.split('n')
       image_id, _ = image_id.split('.')
       image_id.replace('n', '')
       split[int(image_id)] = 'val'
       tmp = line.replace('.//', '')
       line = fp.readline()

# # Put training and validation data into correct directories
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

with open(VAL_SPLIT, mode='r', encoding='utf-8-sig') as fp:
   line = fp.readline()
   while line:
       line = line.strip()
       tmp = line.replace('.//', '')
       class_name, _ = tmp.split('/')

       _, _, image_name_id = line.split('-')
       _, jpg_name = image_name_id.split('/')
   
       src = os.path.join('Dataset/Low-Resolution/', tmp)
       dst = os.path.join('data/dataset/val', class_name, jpg_name)
       shutil.move(src, dst)
       line = fp.readline()

# Extract a testset from the validationset 20% of the validationset
rootdir = 'data/dataset/val'
newdir = 'data/dataset/test'

for subdir, dirs, files in os.walk(rootdir):
   for dir in dirs:
      source = os.path.join(rootdir, dir)
      dest = os.path.join(newdir, dir)
      files = os.listdir(source)
      no_of_files = int(len(files) * 0.2)

      for file_name in random.sample(files, no_of_files):
         #print("image: ", file_name, "path: ", os.path.join(source, file_name), dest)
         shutil.move(os.path.join(source, file_name), dest)




