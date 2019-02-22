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
        print(f'Processed {line_count} lines.')

    # converting list of lists with string values into 2D array of floats to do calculations
    data = np.array(list[1:], dtype=np.float32)
    return data, cols