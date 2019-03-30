from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from ReadCSVFile import readFile, readTestFile
import numpy as np
import matplotlib.pyplot as plt
import metrics as m

imbs = ["SMOTEImb", "ADASYNImb"]
classes = ["TVEClass"]
trueAndPred = {"TVEClass": ()}
norms = ["MinMaxNorm"]
featselects = ["FSelect", "BSelect"]
classifiers = ["NB", "LR", "DT"]

for classif in classes:
    for imb in imbs:
        for norm in norms:
            for featselect in featselects:
                for classifier in classifiers:
                    trainFile = "Electricity_P_Thinned_Hourly_" + norm + "_Train_" + classif + "_" + imb + "_" + \
                                featselect + "_" + classifier + ".csv"
                    dataTrain, cols = readFile(filename=trainFile)
                    testFile = "Electricity_P_Thinned_Hourly_" + norm + "_Test.csv"
                    dataTest = readTestFile(testFile, cols)

                    true_class = dataTest[:, -1]

                    clf = LogisticRegression(solver='liblinear', max_iter=10000)
                    if classifier == "NB":
                        clf = GaussianNB(priors=[0.5, 0.5])
                    elif classifier == "DT":
                        clf = DecisionTreeClassifier()

                    clf.fit(dataTrain[:, :-1], dataTrain[:, -1])
                    DT = DecisionTreeClassifier()
                    DT.fit(dataTrain[:, :-1], dataTrain[:, -1])
                    print("\n\nFile : " + trainFile)
                    print("Feature Importances:")
                    print(cols[:-1])
                    print(DT.feature_importances_)

                    fig, ax = plt.subplots()
                    plt.bar(np.arange(len(cols) - 1), DT.feature_importances_)
                    plt.xticks(np.arange(len(cols) - 1), cols[:-1])
                    plt.title(f"Feature Importances for TVE, {classifier}/{imb[:-3]}/{featselect}")
                    plt.savefig(f'FeatureImportances/TVE_{classifier}_{imb[:-3]}_{featselect}.png')
                    plt.close()

                    pred_class = clf.predict(dataTest[:, :-1])
                    print("Confusion Matrix:")
                    print("_________________")
                    print(f'|TP:{m.tp(true_class, pred_class):4d}|FP:{m.fp(true_class, pred_class):4d}|')
                    print("|_______|_______|")
                    print(f'|TN:{m.tn(true_class, pred_class):4d}|FN:{m.fn(true_class, pred_class):4d}|')
                    print("|_______|_______|")

                    m.roc(true_class, pred_class, f"ROC Curve for TVE, {classifier}/{imb[:-3]}/{featselect}",
                          f'TVE_{classifier}_{imb[:-3]}_{featselect}')

                    if classifier == "LR":
                        print(f'Optimized Parameter: : N/A')
                    if classifier == "NB":
                        print(f'Optimized Parameter: N/A')
                    elif classifier == "DT":
                        print(f'Optimized Parameter: Decision Tree Depth:{clf.tree_.max_depth}')

                    print("accuracy/f1/precision/sensitivity/specificity/tp/tn/fp/fn")
                    print(str(m.accuracy(true_class, pred_class)) + "/" +
                          str(m.f1(true_class, pred_class)) + "/" +
                          str(m.precision(true_class, pred_class)) + "/" +
                          str(m.sensitivity(true_class, pred_class)) + "/" +
                          str(m.specificity(true_class, pred_class)) + "/" +
                          str(m.tp(true_class, pred_class)) + "/" +
                          str(m.tn(true_class, pred_class)) + "/" +
                          str(m.fp(true_class, pred_class)) + "/" +
                          str(m.fn(true_class, pred_class)))



