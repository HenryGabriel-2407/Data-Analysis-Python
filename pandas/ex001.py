import pandas as pd

tabela = pd.read_excel("Vendas.xlsx")
print(tabela)
faturamento_total = tabela["Valor Final"].sum()
print(f"\n\nO Faturamento da empresa foi de R${faturamento_total}\n")

#faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

#faturamento do Iguatemi Campinas por produto
faturamento_produtos_campinas = tabela[["ID Loja", "Valor Final", "Produto"]].groupby(["ID Loja", "Produto"]).sum()
print("\n\n", faturamento_produtos_campinas)