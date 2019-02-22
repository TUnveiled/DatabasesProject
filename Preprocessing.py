import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def readFile(filename='Electricity_P.csv'):
    appliances = {"WHE":"Whole House",
                  "RSE":"Basement",
                  "GRE":"Garage",
                  "MHE":"House Not Including Basement or Garage",
                  "B1E":"Bedroom 1",
                  "B2E":"Bedroom 2",
                  "BME":"Basement Lights and Outlets",
                  "CWE":"Clothes Washer",
                  "DWE":"Dishwasher",
                  "EQE":"Security and network",
                  "FRE":"Furnace Fan and Thermostat",
                  "HPE":"Heat Pump",
                  "OFE":"Home Office",
                  "UTE":"Utility Room",
                  "WOE":"Oven",
                  "CDE":"Clothes Dryer",
                  "DNE":"Dining Room Outlet",
                  "EBE":"Electronics Workbench",
                  "FGE":"Refrigerator",
                  "HTE":"Instant Hot Water",
                  "OUE":"Outside Outlet",
                  "TVE":"Entertainment",
                  "UNE":"Unaccounted"}

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                cols = row
                line_count += 1
            elif line_count == 1:
                list = [row]
                line_count += 1
            else:
                list.append(row)
                line_count += 1
        print(f'Processed {line_count} lines.')

    # converting list of lists with string values into 2D array of floats to do calculations
    data = np.array(list[1:], dtype=np.float32)
    return data, cols

# method to normalize data
# normType = "minmax", "l1", "l2"
def normalizeData(data, cols, normType):

    # initializing variable
    normData = [[]]

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

        # If normData is not empty, write it to a file
        if normData is not [[]]:
            with open('%s.csv' % normType, newline='', mode='w') as normalized_file:
                normalize_writer = csv.writer(normalized_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                normalize_writer.writerow(cols)

                normalize_writer.writerows(normData)
    return normData

# testSize = float between 0 to 100
def TrainTestSplit(data, testSize):
    X_train, X_test, y_train, y_test = train_test_split(data[:,0], data[:, 1:], test_size=testSize, random_state=42)
    return X_train, X_test, y_train, y_test


# imputeType = 'mean', 'median'
def ImputeData(data, imputeType):

    # sklearn automatically discards rows that have NaN values

    # if a value is Nan, replace it with the mean in that column
    if imputeType.lower() == 'mean':
        imp = SimpleImputer(missing_values=np.nan, strategy='mean')
        imp.fit(data)

        # if a value is Nan, replace it with the median in that column
    if imputeType.lower() == 'median':
        imp = SimpleImputer(missing_values=np.nan, strategy='median')
        imp.fit(data)

