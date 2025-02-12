import pandas as pd

data = pd.read_csv("dataset\\water_use_data_2013_to_2022.csv")

data_copy_ano = data['year'].copy() # Cópia
data_copy = data.copy() # Copiando toda tabela
print(f"{data_copy_ano}\n")

data_copy['year'] = 2024 # Todos os valores da coluna  'year' são substituídos por 2024
print(f"{data_copy['year']}\n")

linhas = data.shape[0]
novo_ano_em_dias = [f"Dia {i}" for i in range(linhas)]
data_copy['year'] = novo_ano_em_dias
print(data_copy.head(20))
print()

print(f"{data.head(10)}\n")

data_copy['Coluna sem noção'] = 'Default'

print(f"{data_copy}\n")