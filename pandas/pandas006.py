import pandas as pd

data = pd.read_csv("dataset\\Vinho\\Red.csv")
print(f"{data}\n")

print(f"{data['Country'].unique()}\n") #mostra todos os países sem repetição, mostra valores únicos na coluna

selecao = data['Country'] == 'Italy'
selecao2 = data['Price'] <= 15
print(f"{data[selecao][selecao2]}\n\n")

print(data.query('Country == "Germany"'))
print()

print(f"{data.loc[selecao2].reset_index(drop=True)}\n")