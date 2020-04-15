import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras

import numpy as np
'''
XOR gate
---------------------------
|input1 | input2 | output |
|0      | 0      | 0      |
|0      | 1      | 1      |
|1      | 0      | 1      |
|1      | 1      | 0      |
---------------------------
'''


def compiler(model, optimizer, loss, metrics):
    model.compile(optimizer=optimizer,
                  loss=loss,
                  metrics=metrics)


def getInput():
    data = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    return data


def getLabels():
    data = np.array([
        0, 1, 1, 0
    ])
    return data


def addLayers(model):
    # model.add(layers.Dense(2, activation='relu'))
    model.add(layers.Dense(2, activation='sigmoid'))
    model.add(layers.Dense(1, activation='sigmoid'))


def trainData(model, epochs):
    # assign inputs and labels
    input_data = getInput()
    labels = getLabels()
    model.fit(input_data, labels, epochs=epochs)


def saveModel(model):
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)

    model.save_weights("model.h5")
    print("Saved model to disk")


model = keras.Sequential()

# compiler
compiler(model, "adam", "mse", ["binary_accuracy"])

# add layers
addLayers(model)

# train model
trainData(model, 10000)

# save model
# saveModel(model)

# predictions
result = model.predict([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

print(result)
