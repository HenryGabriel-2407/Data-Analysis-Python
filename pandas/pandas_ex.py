import pandas as pd

data = pd.read_csv("dataset\\Footbal\\results.csv")

print(f"{data.head(10)}\n\n") # 10 primeiros registros da tabela

quantidade_inglaterra = data['country'].value_counts().get('England', 0)
quantidade_brasil = data['country'].value_counts().get('Brazil', 0)

print(f"A quantidade de jogos realizados na Inglaterra foram de {quantidade_inglaterra} vezes")
print(f"A quantidade de jogos realizados no Brasil foram de {quantidade_brasil} vezes\n")

print(f"{data.iloc[5900:5948:4]}\n")
print(f"{data.iloc[[100, 142, 8547, 5214, 4444]]}\n")