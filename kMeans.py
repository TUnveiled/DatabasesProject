from sklearn.cluster import KMeans
import pandas as pd
import numpy
from scipy import stats
numpy.set_printoptions(threshold=numpy.inf)

import matplotlib.pyplot as plt


df = pd.read_csv("Electricity_P_Thinned_Hourly_MinmaxNorm.csv")
df = df.loc[:, 'CWE':]
#Make a copy of DF
df_tr = df

#Standardize
clmns = ['CWE','DWE','FRE','HPE','WOE','CDE','EBE','FGE','HTE','TVE','Hour','Weekday','Month','Season']

#df_tr_std = stats.zscore(df_tr[clmns])


'''Sum_of_squared_distances = []
K = range(1,14)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(df_tr)
    Sum_of_squared_distances.append(km.inertia_)


plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()'''


#Cluster the data
kmeans = KMeans(n_clusters=7, random_state=0).fit(df_tr)
labels = kmeans.labels_

#Glue back to originaal data
df_tr['clusters'] = labels

#Add the column into our list
clmns.extend(['clusters'])

df_tr.sort_values(['clusters']).to_csv("KMeans.csv")

#Lets analyze the clusters
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print (df_tr[clmns].groupby(['clusters']).mean())
