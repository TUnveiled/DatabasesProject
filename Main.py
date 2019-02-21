import Preprocessing

data, cols = Preprocessing.readFile()

normalizedData = Preprocessing.normalizeData(data, cols, 'minmax')

print("\nThe normalized data:\n", normalizedData)



