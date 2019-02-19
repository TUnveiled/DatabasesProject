import csv

appliances = {#"WHE":"WholeHouseEntries",
              #"RSE":"BasementEntries",
              #"GRE":"GarageEntries",
              #"MHE":"HouseNotIncludingBasementOrGarageEntries",
              "B1E":"Bedroom1Entries",
              "B2E":"Bedroom2Entries",
              "BME":"BasementLightAndOutletEntries",
              "CWE":"ClothesWasherEntries",
              "DWE":"DishwasherEntries",
              "EQE":"SecurityAndNetworkEntries",
              "FRE":"FurnaceFanAndThermostatEntries",
              "HPE":"HeatPumpEntries",
              "OFE":"HomeOfficeEntries",
              "UTE":"UtilityRoomEntries",
              "WOE":"OvenEntries",
              "CDE":"ClothesDryerEntries",
              "DNE":"DiningRoomOutletEntries",
              "EBE":"ElectronicsWorkbenchEntries",
              "FGE":"RefrigeratorEntries",
              "HTE":"KeurigEntries",
              "OUE":"OutsideOutletEntries",
              "TVE":"EntertainmentEntries",
              "UNE":"UnaccountedEntries"}

for x in appliances:
    with open('dataverse_files/Electricity_' + x) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} : {row[2]}')
                line_count += 1
        print(f'Processed {line_count} lines.')