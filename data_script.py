# -*- coding: utf-8 -*-
"""data_script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/162LRw1U-EGzJMbO51dv3fyjdpTb7bYR9
"""

from keras_preprocessing.image import ImageDataGenerator
import pandas as pd
from google.colab import drive
import numpy as np

def generate_data():
  drive.mount('/content/drive')
  
  train_csv = r'/content/drive/My Drive/Colab Notebooks/face_detection/data/data_UMD/train.csv'
  test_csv = r'/content/drive/My Drive/Colab Notebooks/face_detection/data/data_UMD/test.csv'

  traindf = pd.read_csv(train_csv, dtype={'id': str, 'x1': np.int32, 'y1': np.int32, 'x2': np.int32, 'y2': np.int32})
  testdf = pd.read_csv(test_csv, dtype={'id': str, 'x1': np.int32, 'y1': np.int32, 'x2': np.int32, 'y2': np.int32}) 

  datagen = ImageDataGenerator(rescale=1./255., validation_split=0.2)
  
  train_dir = r'/content/drive/My Drive/Colab Notebooks/face_detection/data/data_UMD/train_test/train'
  test_dir = r'/content/drive/My Drive/Colab Notebooks/face_detection/data/data_UMD/train_test/test'

  train_generator = datagen.flow_from_dataframe(dataframe=traindf, directory=train_dir, x_col="id",
                                                y_col = ["x1", "y1", "x2", "y2"],
                                                subset='training', batch_size=64, seed=42,
                                                shuffle=True, class_mode="other",
                                                target_size=(256, 256))

  valid_generator = datagen.flow_from_dataframe(dataframe=traindf, directory=train_dir, x_col="id",
                                                y_col = ["x1","y1", "x2", "y2"], 
                                                subset="validation", batch_size=32, seed=42, 
                                                shuffle=True, class_mode="other",
                                                target_size=(256,256))

  test_datagen=ImageDataGenerator(rescale=1./255.)
  test_generator=test_datagen.flow_from_dataframe(dataframe=testdf, directory=test_dir, x_col="id", y_col=None,
                                                  batch_size=32, seed=42, shuffle=False, class_mode=None,
                                                  target_size=(256,256))
  return train_generator, valid_generator, test_generator

def testing():
  print("Ok!")

