import pandas as pd

data = pd.read_csv("dataset\\Footbal\\results.csv")

print(f"{data.head()}\n")
print(f"{data.iloc[[1, 374, 4583], 6]}\n")
print(f"{data.iloc[342, 7]}\n")
print(f"{data.loc[123:132, ['city','country']]}\n") 
del data['date']
print(f"{data.head()}\n")
# data.to_csv("novo_nome_do_arquivo", index=False) serve para salvar as modificações, e index=False serve para 'eliminar' os indices na hora de salvar

data_2 = pd.DataFrame({'bom': [50, 21, 100],
                       'médio': [131, 2, 30],
                       'ruim': [30, 20, 1]}, index=['Xbox', 'Nintendo', "Playstation"])

print(f"{data_2.loc['Xbox']}")