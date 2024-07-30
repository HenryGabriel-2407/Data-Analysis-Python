import pandas as pd

data = pd.read_csv("dataset\\Footbal\\results.csv")

print(data.info())

data_pre = data.copy()

data_pre['date'] = pd.to_datetime(data_pre['date']) #transforma object em datetime
print(data_pre.info())


data_2 = pd.read_csv("dataset\\Vinho\\Red.csv")
print(f"Antes:\n{data_2.info()}\n")
data_2['Year'] = pd.to_numeric(data_2['Year'], errors='coerce')
print(f"Depois:\n{data_2.info()}\n")