"""
Adapted from: https://www.datacamp.com/community/tutorials/tensorflow-tutorial
Project: Belgian traffic signs
"""

import tensorflow as tf
import os

def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory)
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f)
                      for f in os.listdir(label_directory)
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels

ROOT_PATH = "/home/isa/tensorflow-exercises/"
train_data_directory = os.path.join(ROOT_PATH, "data/Training")
test_data_directory = os.path.join(ROOT_PATH, "data/Testing")

images, labels = load_data(train_data_directory)
