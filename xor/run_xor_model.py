from flask import Flask
from tensorflow.keras import models
import numpy as np
import re

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

def loadModel():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = models.model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    return loaded_model


def compiler(model, optimizer, loss, metrics):
    model.compile(optimizer=optimizer,
                  loss=loss,
                  metrics=metrics)


def makePrediction(model, arr):
    return model.predict(arr, verbose=0)


model = loadModel()
# compile model
compiler(model, "adam", "binary_crossentropy", ["binary_accuracy"])

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "please enter next to the url eg. 0,1"


@app.route('/<text>')
def print_output(text):
    matchedText = re.search('^[0-1],[0-1]$', text)
    if(matchedText):
        arr = eval('np.array([[' + text + ']])')

        # predict results
        prediction = makePrediction(model, arr)
        return "XOR output:" + str(int(prediction[0][0].round()))
    return "please enter next to the url eg. 0,1"