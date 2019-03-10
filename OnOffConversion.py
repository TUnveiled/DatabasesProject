import pandas as pd


df = pd.read_csv("C:/Users/Matthew/Downloads/dataverse_files/Electricity_P.csv")
df = df[['UNIX_TS','CWE','DWE','FRE','HPE','WOE','CDE','EBE','FGE','HTE','TVE']]

thresholds = [0, 0, 68, 100, 0, 0, 0, 35, 0, 116]

'''for row in range(len(df.index)):
    for col in range(1, 11):
        if df.iat[row, col] > thresholds[col - 1]:
            df.iat[row, col] = 1

        else:
            df[row, col] = 0

df.to_csv("Electricity_P_Binary.csv")'''