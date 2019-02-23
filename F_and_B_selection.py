import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from mlxtend.feature_selection import SequentialFeatureSelector as sfs

df = pd.read_csv("C:/Users/Matthew/PycharmProjects/DatabasesProject/Electricity_P_Thinned_Hourly_MinmaxNorm.csv") # read the csv file in

LR = LinearRegression() # create linear regression model

# setting up the forward selection. picking 6 best attributes. using R squared as the scoring metric
sfsF = sfs(LR, k_features=6, forward=True, floating=False, verbose=2, scoring='r2')

# setting up the backward selection. picking 6 best attributes. using R squared as the scoring metric
sfsB = sfs(LR, k_features=6, forward=False, floating=False, verbose=2, scoring='r2')

names = {"1":"UNIX_TS",
                  "2":"CWE",
                  "3":"DWE",
                  "4":"FRE",
                  "5":"HPE",
                  "6":"WOE",
                  "7":"CDE",
                  "8":"EBE",
                  "9":"FGE",
                  "10":"HTE",
                  "11":"TVE",
                  "12":"Hour",
                  "13":"Weekday",
                  "14":"Month",
                  "15":"Season"}

for x in range(2,12):
    tempDF = df
    X = tempDF.drop(names[str(x)], axis=1)
    Y = df[names[str(x)]]

    # running the selection tests
    For = sfsF.fit(X, Y)
    Back = sfsB.fit(X, Y)

    # getting the index of the best features
    FIDX = list(For.k_feature_idx_)
    BIDX = list(Back.k_feature_idx_)

    # printing out the results
    print("Forward Selection for "+ str(names[str(x)]) +" : ")
    print(FIDX)
    print("Backwards Selection for "+str(names[str(x)]) +" : ")
    print(BIDX)