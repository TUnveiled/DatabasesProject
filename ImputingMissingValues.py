from ReadCSVFile import readFile, writeFile
from Preprocessing import ImputeData

# It is difficult for us to deal with missing values since our dataset lacks them.
methods = ["Mean", "Median", "Mode"]
for method in methods:
    data, cols = readFile(filename="Electricity_P_Thinned_Hourly.csv")
    data = ImputeData(data, method)
    writeFile(cols, data, "Electricity_P_Thinned_Hourly_" + method + "Imp.csv")
