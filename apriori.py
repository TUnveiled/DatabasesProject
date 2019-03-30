import pandas as pd
from mlxtend.frequent_patterns import apriori

df = pd.read_csv("Electricity_P_Binary_NewThresh.csv")

df_tr = df.loc[:, 'CWE':'TVE']

results = apriori(df_tr, min_support=0.8, use_colnames=True)

print(results)