from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import sys
import array

from PIL import Image
from PIL import ImageOps

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])


model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)
#print(test_images[1])

test_image_names = [
    'photo1_sg.png',
    'photo2_sg.png',
    'photo3_sg.png'
]
test_images = [Image.open(i) for i in test_image_names]
test_images = 1.0 - np.array([np.array(i) for i in test_images]) / 255.0
predictions = model.predict(test_images)


for i in range(len(test_images)):
    p=predictions[i]
    print(p, np.argmax(p), class_names[np.argmax(p)])
    