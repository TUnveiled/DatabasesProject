import Preprocessing
from NormalizeData import normalizeData

data, cols = Preprocessing.readFile(filename='Electricity_P_Hourly.csv')

normalizedData = normalizeData(data, 'minmax')

print("\nThe normalized data:\n", normalizedData)



