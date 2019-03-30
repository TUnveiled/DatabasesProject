from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from ReadCSVFile import readFile, readTestFile
import metrics as m

imbs = ["SMOTEImb", "ADASYNImb"]
classes = ["CWEClass", "DWEClass", "FREClass", "HPEClass", "WOEClass",
           "CDEClass", "EBEClass", "FGEClass", "HTEClass", "TVEClass"]
trueAndPred = {"CWEClass": (),
               "DWEClass": (),
               "FREClass": (),
               "HPEClass": (),
               "WOEClass": (),
               "CDEClass": (),
               "EBEClass": (),
               "FGEClass": (),
               "HTEClass": (),
               "TVEClass": ()}
norms = ["MinMaxNorm"]
featselects = ["FSelect", "BSelect"]
classifiers = ["NB", "LR", "DT"]

for classif in classes:
    for imb in imbs:
        for norm in norms:
            for featselect in featselects:
                for classifier in classifiers:
                    clf = LogisticRegression(solver='lbfgs', max_iter=10000)
                    if classifier == "NB":
                        clf = GaussianNB()
                    elif classifier == "DT":
                        clf = DecisionTreeClassifier()

                    trainFile = "Electricity_P_Thinned_Hourly_" + norm + "_Train_" + classif + "_" + imb + "_" + \
                                featselect + "_" + classifier + ".csv"
                    dataTrain, cols = readFile(filename=trainFile)

                    clf.fit(dataTrain[:, :-1], dataTrain[:, -1])

                    testFile = "Electricity_P_Thinned_Hourly_" + norm + "_Test.csv"
                    dataTest = readTestFile(testFile, cols)

                    true_class = dataTest[:, -1]
                    pred_class = clf.predict(dataTest[:, :-1])
                    print(true_class, pred_class)
                    if trueAndPred[classif] == ():
                        trueAndPred[classif] = (true_class, pred_class, classif + "/" + imb + "/" + norm + "/" +
                                                featselect + "/" + classifier)
                    elif m.f1(true_class, pred_class) > m.f1(trueAndPred[classif][0], trueAndPred[classif][1]):
                        trueAndPred[classif] = (true_class, pred_class, classif + "/" + imb + "/" + norm + "/" +
                                                featselect + "/" + classifier)

    print("Classifier : " + trueAndPred[classif][2])
    print("accuracy/f1/precision/sensitivity/specificity/tp/tn/fp/fn")
    print(str(m.accuracy(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.f1(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.precision(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.sensitivity(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.specificity(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.tp(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.tn(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.fp(trueAndPred[classif][0], trueAndPred[classif][1])) + "/" +
          str(m.fn(trueAndPred[classif][0], trueAndPred[classif][1])))

