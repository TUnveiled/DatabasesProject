import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime

# dictionary for translating codes to human language
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

# interpret csv file
with open('Electricity_P.csv') as csv_file:

    # open csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    # loop to read csv
    for row in csv_reader:
        if line_count == 0:
            # line 1 is the column count
            cols = row
            line_count += 1
            row.append("Time of Day")
            row.append("Time of Year")

        elif line_count == 1:
            # line 2 is the first element
            currenttime = datetime.datetime.fromtimestamp(int(row[0]))

            # time is preprocessed preliminarily at this point, but not as much as we're planning
            row.append(currenttime.hour * 3600 + currenttime.minute * 60 + currenttime.second)
            row.append((float(currenttime.month) + float(currenttime.day) / 31 - 1) * 100 / 12)
            data = [row]
            line_count += 1
        else:
            # other lines are data rows
            currenttime = datetime.datetime.fromtimestamp(int(row[0]))

            # time is preprocessed preliminarily at this point, but not as much as we're planning
            row.append(currenttime.hour * 3600 + currenttime.minute * 60 + currenttime.second)
            row.append((float(currenttime.month) + float(currenttime.day) / 31 - 1) * 100 / 12)
            data.append(row)
            line_count += 1
    print(f'Processed {line_count} lines.')

for i in range(1, len(cols)-2):
    # plot the histogram
    n, bins, patches = plt.hist([row[i] for row in data], 20, facecolor='b')
    plt.xlabel(appliances[cols[i]] + ' Power Consumption')
    plt.ylabel('Entries')
    plt.title('Histogram of ' + appliances[cols[i]] + ' Power Consumption')

    # fit axis to data
    plt.axis(option='tight')

    # fit xticks to bins
    plt.xticks(np.arange(0, bins[1] * 21, step=np.round(bins[1]*4)),
               np.arange(0, bins[1] * 21, step=np.round(bins[1]*4)))
    plt.grid(False)

    # save figure as a png
    plt.savefig('Histograms/HIST_' + cols[i] + '.png')
    plt.show()
