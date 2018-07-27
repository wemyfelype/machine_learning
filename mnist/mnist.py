import warnings 
warnings.filterwarnings("ignore", message="numpy.dtype size changed") 
warnings.filterwarnings("ignore", message="numpy.ufunc size changed") 

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D

import numpy as np
from matplotlib import pyplot as plt

from keras.utils import np_utils
import cv2

#ipython.magic("timeit abs(-42)")

from keras import backend as K 
K.set_image_dim_ordering('th')

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 1, 28, 28).astype('float32')
x_test  = x_test.reshape(x_test.shape[0], 1, 28, 28).astype('float32')

x_train = x_train / 255
x_test = x_test / 255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]

print(y_test.shape)

model = Sequential()

model.add(Conv2D(30, (5,5), input_shape=(1, 28, 28), activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(15, (5,5), input_shape=(1, 28, 28), activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(128, activation='relu'))

model.add(Dense(64, activation='relu'))

model.add(Dense(32, activation='relu'))

model.add(Dense(num_classes, activation='softmax', name='predIct'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#model.summary()

model.fit(x_train, y_train, validation_data=(x_test,y_test), epochs=10, batch_size=200)