import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from ReadCSVFile import readFile, writeFile
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt

#df = pd.read_csv("C:/Users/Matthew/PycharmProjects/DatabasesProject/Electricity_P_Thinned_Hourly_MinmaxNorm.csv") # read the csv file in

#LR = LogisticRegression(solver='lbfgs', max_iter=10000) # create linear regression model
LR = GaussianNB() # create linear regression model

names = {1:"UNIX_TS",
                  2:"CWE",
                  3:"DWE",
                  4:"FRE",
                  5:"HPE",
                  6:"WOE",
                  7:"CDE",
                  8:"EBE",
                  9:"FGE",
                  10:"HTE",
                  11:"TVE",
                  12:"Hour",
                  13:"Weekday",
                  14:"Month",
                  15:"Season"}

imbs = ["SMOTEImb", "ADASYNImb"]
classes = ["CWE", "DWE", "FRE", "HPE", "WOE", "CDE", "EBE", "FGE", "HTE", "TVE"]
norms = ["MinMaxNorm"]
classifiers = ["NB", "LR", "DT"]
for classif in classes:
    for imb in imbs:
        for norm in norms:
            for classifier in classifiers:
                clf = LogisticRegression(solver='lbfgs', max_iter=10000)
                if classifier == "NB":
                    clf = GaussianNB()
                elif classifier == "DT":
                    clf = DecisionTreeClassifier()


                # setting up the forward selection. picking 6 best attributes. using R squared as the scoring metric
                sfsF = sfs(clf, k_features=(1, 8), forward=True, floating=False, verbose=0, scoring='accuracy')

                # setting up the backward selection. picking 6 best attributes. using R squared as the scoring metric
                sfsB = sfs(clf, k_features=(1, 8), forward=False, floating=False, verbose=0, scoring='accuracy')

                data, cols = readFile("Electricity_P_Thinned_Hourly_" + norm + "_Train_" + classif + "Class_" + imb + ".csv")
                For = sfsF.fit(data[:, :14], data[:, 14].astype(bool))

                # getting the index of the best features
                FIDX = list(For.k_feature_idx_)
                FIDX.append(14)

                # printing out the results
                print("Forward Selection for " + str(classif) + " : ")
                print(FIDX)

                data = data[:, FIDX]
                cols = np.take(cols, FIDX)

                writeFile(cols, data, "Electricity_P_Thinned_Hourly_" + norm + "_Train_" + classif + "Class_" + imb
                        + "_FSelect_" + classifier + ".csv")

                data, cols = readFile("Electricity_P_Thinned_Hourly_" + norm + "_Train_" + classif + "Class_" + imb
                                      + ".csv")
                Back = sfsB.fit(np.delete(data, 14, 1), data[:, 14].astype(bool))

                BIDX = list(Back.k_feature_idx_)
                BIDX.append(14)
                print("Backward Selection for " + str(classif) + " : ")
                print(BIDX)

                data = data[:, BIDX]
                cols = np.take(cols, BIDX)

                writeFile(cols, data, "Electricity_P_Thinned_Hourly_" + norm + "_Train_" + classif + "Class_" + imb
                          + "_BSelect_" + classifier + ".csv")

