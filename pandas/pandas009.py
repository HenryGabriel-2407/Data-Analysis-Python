import numpy as np
import pandas as pd

s = pd.Series([1,4,2,9,7,8,1,10, np.nan, 7,5]) # uma Series é basicamente uma coluna
print(s)

date = pd.date_range(start='1/1/2024', end='24/1/2024')
print(date)

tabela = pd.DataFrame(np.random.randn(24, 4), index=date, columns=list("ABCD")) #  uma DataFrame é basicamente uma tabela
print(tabela)

#Criando um DataFrame passando um dicionário de objetos onde as chaves são os rótulos das colunas e os valores são os valores das colunas.
tabela2 = pd.DataFrame({'A': pd.date_range('1/1/2024', periods=3),
                        'B': pd.Index(['Registro 1', 'Registro 2', 'Registro 3']),
                        'C': np.array([1,5,3], dtype="int32"),
                        'D': pd.Categorical(["Limão", "Laranja", "Maçã"]),
                        'E': "Comprado"})
print(tabela2)
print(tabela2.dtypes) #  Mostra o tipo de cada coluna
print("\n\n")
print(tabela2.describe)
print("\n\n")

tabela3 = pd.read_csv("dataset\\planets.csv")
print(tabela3.head()) # Mostra as primeiras linhas do arquivo csv
print(tabela3.tail())  # Mostra as últimas linhas do arquivo csv
print(tabela3.index)  # Mostra os índices das linhas do arquivo csv
print(tabela3.columns)   # Mostra os nomes das colunas do arquivo csv

print(tabela3.to_numpy()) # Os arrays NumPy têm um dtype para o array inteiro, enquanto os DataFrames pandas têm um dtype por coluna . Quando você chama DataFrame.to_numpy(), o pandas encontrará o dtype NumPy que pode conter todos os dtypes no DataFrame. Se o tipo de dado comum for object, DataFrame.to_numpy() será necessário copiar os dados.
print("\n\n")

tabela4 = pd.read_excel("dataset\\Vendas.xlsx")
print(tabela4.describe())  # Mostra as estatísticas descritivas das colunas do arquivo excel
print("\n\n")

print(tabela2.sort_values(by='C'))  # Ordena a tabela por uma coluna