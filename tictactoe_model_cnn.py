from keras import Sequential, Input
from keras.layers import Conv2D, Activation, Flatten, Dense
import numpy as np
from model import Model


class TicTacToeModelCnn(Model):
    def __init__(self, model=None):
        super().__init__(ninput=9,
                         layers=[],
                         model=model)

    def build_model(self, ninput, layers):
        model = Sequential()
        model.add(Conv2D(64, (2, 2), input_shape=(100, 3, 3, 1), name='layer1'))
        model.add(Activation('relu'))

        model.add(Flatten())
        model.add(Dense(64, name='layer2'))
        model.add(Activation('relu'))
        model.add(Dense(3, activation='softmax', name='layer3'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])
        return model

    def preprocess(self, plays):
        features, targets = super().preprocess(plays)
        print(type(features))
        features = np.array([f.reshape((3, 3, 1)) for f in features])
        print(type(features))
        return features, targets