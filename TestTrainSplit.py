from Preprocessing import TrainTestSplit
from ReadCSVFile import readFile, writeFile

norms = ["MinmaxNorm"]

for norm in norms:
    data, cols = readFile(filename="Electricity_P_Thinned_Hourly_" + norm + ".csv")

    train, test = TrainTestSplit(data)

    writeFile(cols, train, "Electricity_P_Thinned_Hourly_" + norm + "_Train.csv")
    writeFile(cols, test, "Electricity_P_Thinned_Hourly_" + norm + "_Test.csv")

