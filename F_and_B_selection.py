import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from mlxtend.feature_selection import SequentialFeatureSelector as sfs

df = pd.read_csv("CSV NAME HERE") # read the csv file in

X = df[:-1] # all the features
Y = df[-1] # the class

LR = LinearRegression() # create linear regression model

# setting up the forward selection. picking 6 best attributes. using R squared as the scoring metric
sfsF = sfs(LR, k_features=6, forward=True, floating=False, verbose=2, scoring='r2')

# setting up the backward selection. picking 6 best attributes. using R squared as the scoring metric
sfsB = sfs(LR, k_features=6, forward=False, floating=False, verbose=2, scoring='r2')

# running the selection tests
sfsF = sfsF.fit(X,Y)
sfsF = sfsB.fit(X,Y)

# getting the index of the best features
FIDX = sfsF.k_feature_idx_
BIDX = sfsB.k_feature_idx_

# printing out the results
print("Forward Selection: ")
print(FIDX)
print("Backwards Selection: ")
print(BIDX)