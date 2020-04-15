from sklearn import tree

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

# https://www.youtube.com/watch?v=cKxRvEZd3Mw

features = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]


labels = [
    0, 1, 1, 0
]
clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

result = clf.predict(features)
print(result)
