from imblearn.over_sampling import SMOTE, ADASYN
import numpy as np
from ReadCSVFile import readFile, writeFile

def correctImbalancedData(data, algoType, index):

    x_result, y_result = [], []

    if algoType.lower() == 'smote':
        sm = SMOTE(random_state=42)
        x_result, y_result = sm.fit_sample(np.delete(data, index, 1), data[:, index])
    elif algoType.lower() == 'adasyn':
        ada = ADASYN(random_state=42)
        x_result, y_result = ada.fit_sample(np.delete(data, index, 1), data[:, index])

    return x_result, y_result


norms = ["11Norm", "MinMaxNorm"]
algos = ["SMOTE", "ADASYN"]
for i in range(1, 11):
    for norm in norms:
        for algo in algos:
            data, cols = readFile(filename="Electricity_P_Thinned_Hourly_" + norm + "_Train.csv")

            print(cols[i])
            cols.append(cols[i])
            cols = np.delete(cols, i)

            X, y = correctImbalancedData(data, algo, i)
            data = []
            for n in range(len(y)):
                data.append(np.append(X[n], y[n]))

            writeFile(cols, data, filename="Electricity_P_Thinned_Hourly_" + norm + "_Train_" + cols[-1]
                                         + "Class_" + algo + "Imb.csv")
