# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VbqC1qf_h5h8q4jbaVyU4QzpTKY64ltI
"""

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

home = pd.read_csv('home_data.csv')
home.head()
home.tail()
home.info()
home.columns
home

plt.figure(figsize=(6,6))
plt.scatter(home.sqft_living,home.price)
plt.show()

sns.lmplot('sqft_living', 'price', data = home)

sns.heatmap(home.corr())

sns.boxplot(x = 'zipcode', y = 'price', data = home)

home.columns

x = home[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'zipcode'
        ]]

y = home['price']


x = np.array(x.drop(['bedrooms', 'zipcode'], 1))





print(x.shape)

print(y.shape)


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=7)

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

acc= model.score(X_test, y_test)

print(acc)

x

home1 = home[home['id'] == 6414100192]

print(home1['price'])

print(prediction[1])

for x in range(len(prediction)):
    print(prediction[x], X_test[x], y_test[x])


plt.figure(figsize= (7,7))

plt.scatter(y_test, prediction)

model.coef_

print(model.intercept_)

dframe = pd.DataFrame(model.coef_, x.columns,columns = ['Values'],  )

dframe

mean_sq_err = metrics.mean_squared_error(y_test, prediction)
mean_sq_err
rmse = np.sqrt(mean_sq_err)
rmse