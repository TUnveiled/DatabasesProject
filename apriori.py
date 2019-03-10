import pandas as pd
from mlxtend.frequent_patterns import apriori

df = pd.read_csv("C:/Users/Matthew/Downloads/dataverse_files/Electricity_P_Binary.csv")
df = df.loc[:, 'CWE':'TVE']
print(df)
results = apriori(df, min_support=0.6, use_colnames=True)

print(results)