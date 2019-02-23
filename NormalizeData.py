from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import normalize
from ReadCSVFile import readFile, writeFile

# method to normalize data
# normType = "minmax", "l1", "l2"
def normalizeData(data, normType):
    normData = threshold(data)

    # features range from 0 to 1
    if normType.lower() == 'minmax':
        minmax_scaler = MinMaxScaler(feature_range=(0, 1))
        normData = minmax_scaler.fit_transform(data)

    # Least absolute deviations - sum of absolute values in each column equals 1 (insensitive to outliers)
    elif normType.lower() == 'l1':
        normData = normalize(data, norm='l1', axis=1)

    # Least squares - sum of squares in each column equals 1 (sensitive to outliers)
    elif normType.lower() == 'l2':
        normData = normalize(data, norm='l2', axis=1)

    return normData


def threshold(data):
    thresholds = [0, 0, 68, 100, 0, 0, 0, 35, 0, 116]

    for row in range(len(data)):
        for col in range(1, 11):
            if data[row][col] > thresholds[col - 1]:
                data[row][col] = 1
            else:
                data[row][col] = 0

    return data


normTypes = ["Minmax", "11"]

for type in normTypes:
    # skip the Imputed ones because there are no missing values
    data, cols = readFile(filename="Electricity_P_Thinned_Hourly.csv")

    data = normalizeData(data, type)

    writeFile(cols, data, "Electricity_P_Thinned_Hourly_" + type + "Norm.csv")

