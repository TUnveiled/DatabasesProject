from sklearn.naive_bayes import GaussianNB
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
                            featselect + "_NB.csv"
                dataTrain, cols = readFile(filename=trainFile)

                NB = GaussianNB()
                NB.fit(dataTrain[:, :-1], dataTrain[:, -1])

                testFile = "Electricity_P_Thinned_Hourly_" + norm + "_Test.csv"
                dataTest = readTestFile(testFile, cols)

                true_class = dataTest[:, -1]
                pred_class = NB.predict(dataTest[:, :-1])

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
                      str(m.fn(true_class, pred_class)))

