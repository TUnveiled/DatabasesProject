from sklearn import tree
from ReadCSVFile import readFile, readTestFile
import metrics as m

imbs = ["SMOTEImb", "ADASYNImb"]
classes = ["CWEClass", "DWEClass", "FREClass", "HPEClass", "WOEClass",
           "CDEClass", "EBEClass", "FGEClass", "HTEClass", "TVEClass"]
norms = ["MinMaxNorm"]
featselects = ["FSelect", "BSelect"]

for classif in classes:
    for imb in imbs:
        for norm in norms:
            for featselect in featselects:
                trainFile = "Electricity_P_Thinned_Hourly_" + norm + "_Train_" + classif + "_" + imb + "_" + \
                            featselect + "_DT.csv"
                dataTrain, cols = readFile(filename=trainFile)

                DT = tree.DecisionTreeClassifier()
                DT.fit(dataTrain[:, :-1], dataTrain[:, -1])

                testFile = "Electricity_P_Thinned_Hourly_" + norm + "_Test.csv"
                dataTest = readTestFile(testFile, cols)

                true_class = dataTest[:, -1]
                pred_class = DT.predict(dataTest[:, :-1])

                print("File : " + trainFile)
                print("accuracy/f1/precision/sensitivity/specificity/tp/tn/fp/fn")
                print(str(m.accuracy(true_class, pred_class)) + "/" +
                      str(m.f1(true_class, pred_class)) + "/" +
                      str(m.precision(true_class, pred_class)) + "/" +
                      str(m.sensitivity(true_class, pred_class)) + "/" +
                      str(m.specificity(true_class, pred_class)) + "/" +
                      str(m.tp(true_class, pred_class)) + "/" +
                      str(m.tn(true_class, pred_class)) + "/" +
                      str(m.fp(true_class, pred_class)) + "/" +
                      str(m.fn(true_class, pred_class)) +"\n")















'''from sklearn import tree
import pandas as pd

cols = ['CWE','DWE','FRE','HPE','WOE','CDE','EBE','FGE','HTE','TVE']

test_df = pd.read_csv("Electricity_P_Thinned_Hourly_11Norm_Test.csv")
train_df = pd.read_csv("Electricity_P_Thinned_Hourly_11Norm_Train.csv")
clf = tree.DecisionTreeClassifier()

for col in cols:
    temp_train = train_df
    temp_test = test_df

    train_X = temp_train.drop(col, axis=1)
    train_Y = train_df[col]

    test = temp_test.drop(col, axis=1)

    clf = clf.fit(train_X, train_Y)
    print("Predicting {}".format(col))
    print(clf.predict(test))
    print("")'''