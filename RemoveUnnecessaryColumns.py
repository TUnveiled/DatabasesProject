from ReadCSVFile import readFile, writeFile
import numpy as np
data, cols = readFile(filename="Electricity_P.csv")

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

toRemove = ["WHE", "RSE", "GRE", "MHE", "B1E", "B2E", "BME", "EQE", "OFE",
            "UTE", "DNE", "OUE", "UNE"]

for col in toRemove:
    for i in range(0, len(cols)):
        if cols[i] == col:
            data = np.delete(data, i, 1)
            cols = np.delete(cols, i)
            i -= 1
            break

writeFile(cols, data, "Electricity_P_Thinned.csv")
