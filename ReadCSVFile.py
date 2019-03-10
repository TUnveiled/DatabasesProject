import csv
import numpy as np

def readFile(filename='Electricity_P.csv'):
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

    # converting list of lists with string values into 2D array of floats to do calculations
    data = np.array(list[1:], dtype=np.float32)
    return data, cols


def readTestFile(filename, trainCols):
    data, cols = readFile(filename)

    cols = np.array(cols)

    colsToRemove = set(cols).difference(set(trainCols))
    colsToRemove = list(colsToRemove)

    for i in range(len(colsToRemove)):
        for j in range(len(cols)):
            if colsToRemove[i] == cols[j]:
                data = np.delete(data, j, 1)
                cols = np.delete(cols, j)
                break

    permutation = np.zeros(len(trainCols), np.int)
    for i in range(len(trainCols)):
        for j in range(len(cols)):
            if trainCols[i] == cols[j]:
                permutation[i] = j
                break

    return data[:, permutation]



def writeFile(cols, data, filename):
    with open(filename, 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        writer.writerow(cols)
        writer.writerows(data)