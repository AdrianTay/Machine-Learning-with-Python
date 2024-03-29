# -*- coding: utf-8 -*-
"""SVM and K-Fold.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S988iEft8PltiteqeX2MnnQnnGz5uM8t
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

import sklearn.datasets
import sklearn.svm
import matplotlib.pyplot as plt

iris = datasets.load_iris()

#print (iris.DESCR)

x = iris.data

y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4, random_state = 0)

model = svm.SVC(kernel='linear', C=1) 

model.fit(x_train, y_train)

acc = model.score(x_test, y_test)

print(acc)

##using k-fold cross validation here is because the iris datasets are too small
#need to prevent overfitting of the model

score = model_selection.cross_val_score(model , x, y, cv= 5)

print(score)

print(score.mean())

model1 = svm.SVC(kernel='poly', degree= 4, C=1) #degree is default by 3

model1.fit(x_train, y_train)


score1 = model_selection.cross_val_score(model1, x, y, cv=5)

print(score1)

print(score1.mean())