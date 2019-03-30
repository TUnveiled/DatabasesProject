import csv
import datetime

appliances = {"WHE":"Whole House",
              "RSE":"Basement",
              "GRE":"Garage",
              "MHE":"House Not Including Basement or Garage",
              "B1E":"Bedroom 1",
              "B2E":"Bedroom 2",
              "BME":"Basement Lights and Outlets",
              "CWE":"Clothes Washer",
              "DWE":"Dishwasher",
              "EQE":"Security and Network",
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


class PST(datetime.tzinfo):
    """PST"""

    def utcoffset(self, dt):
        return datetime.timedelta(hours=-8)

    def tzname(self, dt):
        return "PST"

    def dst(self, dt):
        return datetime.timedelta(0)


toRemove = {"WHE", "RSE", "GRE", "MHE", "UNE"}

data = []
dataByHour = []
cols = []

with open('Electricity_P_Thinned.csv') as csv_file:
    # open csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    # loop to read csv
    for row in csv_reader:
        if line_count == 0:
            # line 1 is the column count
            cols = row
            line_count += 1
            row.append("Hour")
            row.append("Weekday")
            row.append("Month")
            row.append("Season")

        elif line_count == 1:
            # line 2 is the first element
            currenttime = datetime.datetime.fromtimestamp(int(float(row[0])), tz=PST())

            #
            row.append(currenttime.hour)
            row.append(currenttime.weekday())
            row.append(currenttime.month)
            row.append(currenttime.month // 4)
            data = [row]
            line_count += 1

        else:
            # other lines are data rows
            currenttime = datetime.datetime.fromtimestamp(int(float(row[0])), tz=PST())
            row.append(currenttime.hour)
            row.append(currenttime.weekday())
            row.append(currenttime.month)
            row.append(currenttime.month // 4)
            data.append(row)
            line_count += 1
    print(f'Processed {line_count} lines.')

previousRow = data[0]
binEndings = []
index = 1
# find the end of each hour in the dataset
for row in data[1:]:
    if row[-4] != previousRow[-4]:
        binEndings.append(index)

    previousRow = row
    index += 1

previousBinEnding = 0

# find the max power usage of each appliance for each hour and create the dataset
for binEnding in binEndings:
    tempslice = data[previousBinEnding:binEnding]
    maxes = tempslice[0]
    for row in tempslice:
        for i in range(0, len(row)):
            if maxes[i] < row[i]:
                maxes[i] = row[i]
    dataByHour.append(maxes)

    previousBinEnding = binEnding

with open('Electricity_P_Thinned_Hourly.csv', 'w', newline='') as outFile:
    writer = csv.writer(outFile)
    writer.writerow(cols)
    writer.writerows(dataByHour)
