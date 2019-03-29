import pandas as pd


df = pd.read_csv("C:\\Users\\Matthew\\Downloads\\dataverse_files\\Electricity_P.csv")

df_tr = df.loc[:, ['UNIX_TS','CWE','DWE','FRE','HPE','WOE','CDE','EBE','FGE','HTE','TVE']]
thresholds = [30, 500, 136, 100, 100, 150, 0, 70, 10, 116]

for row in range(len(df_tr.index)):
    for col in range(1, 11):
        if df_tr.iat[row, col] > thresholds[col - 1]:
            df_tr.iat[row, col] = 1

        else:
            df_tr.iat[row, col] = 0

df_tr.to_csv("Electricity_P_Binary.csv", index=False)