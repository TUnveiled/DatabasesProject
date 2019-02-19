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

# create the plots
for i in range(1, len(cols)):
    for j in range(1, len(cols)):

        # avoid repeats
        if i <= j:
            continue

        # extract relevant columns
        x = [float(row[i]) for row in data]
        y = [float(row[j]) for row in data]

        # find the correlation coefficient
        r = np.corrcoef(x, y)[0][1]

        # the correlation is unimportant and the x axis isn't time, skip this one
        if (abs(r) < 0.3) and (i < len(cols) - 2):
            continue

        # dont plot line of best fit for time graphs
        if i >= len(cols) - 2:
            plt.scatter(x, y, marker='.', alpha=0.1)
        else:
            # plot a line of best fit for non-time correlations
            plt.scatter(x, y, s=10, marker='.', alpha=0.1)
            plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='r')

        # labels are the column names
        plt.xlabel(cols[i])
        plt.ylabel(cols[j])
        plt.title(cols[j] + ' vs ' + cols[i])

        # fit axis to data
        plt.axis(option='tight')

        # fit ticks to data
        plt.xticks(np.arange(0, round(max(x) * 6 / 5), step=round(max(x) / 5)),
                   np.arange(0, round(max(x) * 6 / 5), step=round(max(x) / 5)))
        plt.yticks(np.arange(0, round(max(y) * 6 / 5), step=round(max(y) / 5)),
                   np.arange(0, round(max(y) * 6 / 5), step=round(max(y) / 5)))
        plt.grid(False)

        # save the graph as a png
        plt.savefig('Correlations/CORR_' + cols[j] + '_vs_' + cols[i] + '.png')
        plt.show()
