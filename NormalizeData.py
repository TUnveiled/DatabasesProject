from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import normalize

# method to normalize data
# normType = "minmax", "l1", "l2"
def normalizeData(data, normType):

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




