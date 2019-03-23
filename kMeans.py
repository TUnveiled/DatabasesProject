from sklearn.cluster import KMeans
import pandas as pd
import numpy
from scipy import stats
numpy.set_printoptions(threshold=numpy.inf)

import matplotlib.pyplot as plt


df = pd.read_csv("Electricity_P_Thinned_Hourly_11Norm.csv")
df = df.loc[:, 'CWE':]
#Make a copy of DF
df_tr = df

#Standardize
clmns = ['CWE','DWE','FRE','HPE','WOE','CDE','EBE','FGE','HTE','TVE','Hour','Weekday','Month','Season']

df_tr_std = stats.zscore(df_tr[clmns])


#Cluster the data
kmeans = KMeans(n_clusters=5, random_state=0).fit(df_tr_std)
labels = kmeans.labels_

#Glue back to originaal data
df_tr['clusters'] = labels

#Add the column into our list
clmns.extend(['clusters'])

#Lets analyze the clusters
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print (df_tr[clmns].groupby(['clusters']).mean())
