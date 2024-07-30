import pandas as pd

data = pd.read_csv("water_use_data_2013_to_2022.csv")

data_copy_ano = data['year'].copy()
data_copy = data.copy()
print(f"{data_copy_ano}\n")

data_copy_ano['year'] = 2024
print(f"{data_copy_ano.head()}\n")

linhas = data.shape[0]
novo_ano_em_dias = [f"Dia {i}" for i in range(linhas)]
data_copy['year'] = novo_ano_em_dias
print(data_copy.head(20))
print()

print(f"{data.head(10)}\n")

data_copy['Coluna sem noção'] = 'Default'

print(f"{data_copy}\n")