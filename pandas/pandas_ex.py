import pandas as pd

data = pd.read_csv("C:\\Users\\Usuário\\Desktop\\Pastando\\Python\\Análise de Dados\\dataset\\results.csv")

print(f"{data.head(10)}\n\n")

coluna_country = data['country']
quantidade_inglaterra = 0
quantidade_brasil = 0
for pais in coluna_country:
    if pais == 'England':
        quantidade_inglaterra += 1
    elif pais == 'Brazil':
        quantidade_brasil += 1
    else: 
        continue

print(f"A quantidade de jogos realizados na Inglaterra foram de {quantidade_inglaterra} vezes")
print(f"A quantidade de jogos realizados no Brasil foram de {quantidade_brasil} vezes\n")

print(f"{data.iloc[5900:5948:4]}\n")
print(f"{data.iloc[[100, 142, 8547, 5214, 4444]]}\n")