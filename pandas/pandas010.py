import pandas as pd
import numpy as np

tabela = pd.read_csv("dataset\\planets.csv")

"""     SELEÇÃO POR RÓTULO      """
print(tabela[0:3]) #  Mostra as 3 primeiras linhas da tabela
print(tabela['Color']) #  Mostra a coluna Color da tabela
print("\n\n")

print(tabela.loc[2])
print("\n\n")

print(tabela.loc[:, ["Color", "Length of Day (hours)"]]) # Pegando 2 colunas da tabela
print("\n\n")

print(tabela.loc[0:4, ["Color",  "Length of Day (hours)"]]) # Pegando 5 linhas e 2 col (os pontos finais são incluídos)
print("\n\n")

print(tabela.loc[[4],["Color"]])  # Pegando a linha 4 e a coluna Color
print("\n\n\n")

"""     SELEÇÃO POR POSIÇÃO     """
print(tabela.iloc[1])
print("\n\n")

print(tabela.iloc[1:3, 4:7])  # Pegando 2 linhas e 3 colunas
print("\n\n")

print(tabela.iloc[[0,2,5,7],  [0,2,4]])  # Pegando 4 linhas e 3 colunas
print('\n\n')

print(tabela.iloc[:,  0:3])  # Pegando todas as linhas e 3 colunas
print('\n\n')

print(tabela.iloc[1,2])
print('\n\n')

"""     SELEÇÃO  POR CONDIÇÃO      """
print(tabela[tabela['Diameter (km)'] >= 13000])
print('\n\n')

print(tabela[tabela['Global Magnetic Field?'].isin(["No"])]) 
print("\n\n")


"""     CONTEXTO        """
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
print(s1)

df2 = tabela["Mass (10^24kg)"] # Vamos negativar  os valores da coluna Mass (10^24kg)
tabela["Mass (10^24kg)"] = -df2
print(tabela.loc[:,  ["Mass (10^24kg)"]])
