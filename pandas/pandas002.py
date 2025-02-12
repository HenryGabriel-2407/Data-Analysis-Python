import pandas as pd

data = pd.read_csv("dataset\\water_use_data_2013_to_2022.csv")

print(f"{data['year']}\n")

print(f"{data.county}\n")

print(f"{type(data['year'])}\n")

print(f"{data.iloc[1]}\n") #vai imprimir a linha 1 da tabela

pd_series = pd.Series([8.7, 9.3, 10.0], index=['ATV1', 'ATV2', 'PROVA'], name="Notas do aluno")
print(f"{pd_series.name}\n{pd_series}\n")