import pandas as pd
from mlxtend.frequent_patterns import apriori

df = pd.read_csv("Electricity_P_Thinned_Hourly_MinmaxNorm.csv")

df = df.loc[:, 'CWE':'TVE']

results = apriori(df, min_support=0.5, use_colnames=True)

print(results)