import pandas as pd #importando a biblioteca

tabela = pd.read_excel("dataset\\Vendas.xlsx") # importanto a tabela
print(tabela)

faturamento_total = tabela["Valor Final"].sum() # soma de todos os valores da coluna "Valor Final"
print(f"\n\nO Faturamento da empresa foi de R${faturamento_total}\n")

#faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

#faturamento do Iguatemi Campinas por produto
faturamento_produtos_campinas = tabela[["ID Loja", "Valor Final", "Produto"]].groupby(["ID Loja", "Produto"]).sum()
print("\n\n", faturamento_produtos_campinas)