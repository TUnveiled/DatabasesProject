import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics

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
data = [[]]
cols = [""]


with open('Electricity_P.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            cols = row
            line_count += 1
        elif line_count == 1:
            row.append("Time of Day")
            list = [row]
            line_count += 1
        else:
            list.append(row)
            line_count += 1
    print(f'Processed {line_count} lines.')

columns = ('WHE', 'RSE', 'GRE', 'MHE', 'B1E', 'BME', 'CWE', 'DWE', 'EQE', 'FRE', 'HPE', 'OFE', 'UTE', 'WOE', 'B2E', 'CDE', 'DNE', 'EBE', 'FGE', 'HTE', 'OUE', 'TVE', 'UNE')
rows = ['Mean', 'Median']
stats=[[]]

for i in range (1, len(cols)):
    stats[0].append(statistics.mean([int(row[i]) for row in list]))
    stats[1].append(statistics.median([int(row[i]) for row in list]))
    stats[2].append(statistics.mode([int(row[i]) for row in list]))
    stats[3].append(statistics.pstdev([int(row[i]) for row in list]))

print(stats)