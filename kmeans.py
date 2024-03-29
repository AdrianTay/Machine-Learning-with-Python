# -*- coding: utf-8 -*-
"""KMeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iSY5FfyIgPNEe4HD-Rs38OSwVKsFx2Z
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('health_data.csv')
data.columns = map(str.upper,data.columns)
data = data.dropna()
data

cluster = data[['ALCEVR1',	'ALCPROBS1',	'MAREVER1'	,'COCEVER1',	'INHEVER1',	'CIGAVAIL'	,'DEP1'	,'ESTEEM1',	'VIOL1',	'PASSIST',	'DEVIANT1']]

# This is for scaling 
cluster_s = cluster.copy()
cluster_s['ALCEVR1'] = preprocessing.scale(cluster_s['ALCEVR1'].astype('float64'))
cluster_s['ALCPROBS1'] = preprocessing.scale(cluster_s['ALCPROBS1'].astype('float64'))
cluster_s['MAREVER1'] = preprocessing.scale(cluster_s['MAREVER1'].astype('float64'))
cluster_s['COCEVER1'] = preprocessing.scale(cluster_s['COCEVER1'].astype('float64'))
cluster_s['INHEVER1'] = preprocessing.scale(cluster_s['INHEVER1'].astype('float64'))
cluster_s['CIGAVAIL'] = preprocessing.scale(cluster_s['CIGAVAIL'].astype('float64'))
cluster_s['DEP1'] = preprocessing.scale(cluster_s['DEP1'].astype('float64'))
cluster_s['ESTEEM1'] = preprocessing.scale(cluster_s['ESTEEM1'].astype('float64'))
cluster_s['VIOL1'] = preprocessing.scale(cluster_s['VIOL1'].astype('float64'))
cluster_s['PASSIST'] = preprocessing.scale(cluster_s['PASSIST'].astype('float64'))
cluster_s['DEVIANT1'] = preprocessing.scale(cluster_s['DEVIANT1'].astype('float64'))

cluster_train, cluster_test = train_test_split(cluster_s, test_size = 0.3, random_state =222)


from scipy.spatial.distance import cdist

clusters = range(1,11)

mean_dist = []

for k in clusters: 
  model = KMeans(n_clusters = k)
  model.fit(cluster_train)
  mean_dist.append(sum(np.min(cdist(cluster_train, model.cluster_centers_, 'euclidean'), axis=1)) / cluster_train.shape[0]) #cluster_train.shape[0] = 3220  #cluster_train.shape[1] = 13

plt.plot(clusters, mean_dist)
plt.ylabel('mean_dist')
plt.xlabel('number of k')
plt.title("Elbow curve for k values")

from sklearn.decomposition import PCA

k = 2

model1= KMeans(n_clusters = k)

model1.fit(cluster_train)

pca2 = PCA(2)

plot_columns = pca2.fit_transform(cluster_train)

plt.scatter(x=plot_columns[:,0] , y=plot_columns[:,1] , c=model1.labels_)

plt.xlabel('Canonical_var1')
plt.ylabel('Canonical_var2')
plt.show()