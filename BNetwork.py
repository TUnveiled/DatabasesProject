import pomegranate as pom
import pandas as pd
import pickle

'''clmns = ['UNIX_TS','CWE','DWE','FRE','HPE','WOE','CDE','EBE','FGE','HTE','TVE']
#pomegranate.utils.enable_gpu()
print(pom.utils.is_gpu_enabled())
#train = pd.read_csv("Electricity_P_Thinned_Hourly_MinmaxNorm_Train.csv")
#test = pd.read_csv("Electricity_P_Thinned_Hourly_MinmaxNorm_Test.csv")

df = pd.read_csv("Electricity_P_Thinned_Hourly_MeanImp.csv")

df_tr = df.loc[:, ['UNIX_TS','TVE']]

print("Starting Training")

model = pom.BayesianNetwork.from_samples(df_tr, algorithm='exact', state_names = clmns)
#model = pom.NaiveBayes.from_samples(df_tr)
model.bake()

json = model.to_json()

file = open("BNet.json", 'w+')

file.write(json)
file.close()'''

model = pom.BayesianNetwork.from_json('BNet.json')
#print(model.probability(['861.0', None]))
print(model.marginal())
print(model.state_count())