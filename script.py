#!/usr/bin/env python3.5

import requests
import html2text
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

def main():
    text1 = finalText('https://www.android.com/')
    text2 = finalText('https://www.apple.com/uk/iphone/')
    documents = [text1, text2]
    vectorizer, model = trainModel(documents)
    testModel(vectorizer, model)

def finalText(url): #take a website and tranform it to text
    r = requests.get(url)   #make the request

    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text_maker.ignore_images = True

    text = text_maker.handle(r.text)    #html to text
    splitted_text = text.split()

    final_text = []
    for i in splitted_text:             #clear the text
        temp = re.sub("[^A-Za-z]", "", i)
        if (temp != ''):
            final_text.append(temp)

    return " ".join(final_text)         #make the array text again


def trainModel(documents):  #use KMeans cluster algorigthm to train the model
    vectorizer = TfidfVectorizer(stop_words='english') #tokenize words -avoid unnecessary words
    X = vectorizer.fit_transform(documents)

    true_k = 2  #create two clusters
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind]),
        print
    return vectorizer,model


def testModel(vectorizer,model):    #make predictions according to the model
    print("\n")
    print("Prediction")

    print("\n")
    print("Prediction for word android")
    Y = vectorizer.transform(["android."])
    prediction = model.predict(Y)
    print(prediction)

    print("Prediction for word iphone")
    Y = vectorizer.transform(["iphone."])
    prediction = model.predict(Y)
    print(prediction)

if __name__ == "__main__":
    main()
