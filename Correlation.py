import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
data = pd.read_csv('KMeans_Thin_H_BIN_CDE_Hour.csv') #read csv file into dataframe


#code to generate correlation graph was found here https://medium.com/@sebastiannorena/finding-correlation-between-many-variables-multidimensional-dataset-with-python-5deb3f39ffb3
corr = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.savefig('correlation')
plt.show()


