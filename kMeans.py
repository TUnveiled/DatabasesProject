from sklearn.cluster import KMeans
import pandas as pd
import numpy
numpy.set_printoptions(threshold=numpy.inf)
import matplotlib.pyplot as plt


X = pd.read_csv("Electricity_P_Thinned_Hourly_11Norm.csv")
print(X.size)


kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

labels = kmeans.labels_

print(labels.size)

#print(kmeans.cluster_centers_)