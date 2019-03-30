from sklearn.cluster import KMeans
import pandas as pd
import numpy
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("Electricity_P_Thinned_Hourly_Binary.csv")
df = df.loc[:, 'CWE':'Hour']
clmns = ['CWE','DWE','FRE','HPE','WOE','CDE','EBE','FGE','HTE','TVE']

#Make a copy of DF

'''Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(df_tr_std)
    Sum_of_squared_distances.append(km.inertia_)


plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k MM zscore')
plt.show()'''


for i in range(len(clmns)):
    df_tr = df.loc[:, [clmns[i],'Hour']]
    nclusters = 24
    kmeans = KMeans(n_clusters=nclusters, random_state=0).fit(df_tr)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    # Glue back to originaal data
    df_tr['clusters'] = labels

    # Add the column into our list
    clmns.extend(['clusters'])

    df_tr.sort_values(['clusters']).to_csv("KMeans_Thin_H_BIN_" + clmns[i] + "_Hour.csv", index=False)

    text = "Hour: "
    plt.scatter(centers[:, 1], centers[:, 0], c='red', alpha=0.5)
    plt.ylabel(clmns[i])
    plt.xlabel('Hour')
    plt.title(clmns[i]+" VS. Hour")
    plt.xticks(range(0,24))

    for x in range(0,24):
        plt.axvline(x)
    plt.savefig('Kmeans_Plots\\'+clmns[i] + " VS. Hour.png")
    plt.show()