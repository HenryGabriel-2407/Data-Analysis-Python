#Uma tabela no pandas é chamada de 'DataFrame', 'Table' ou 'Rectangular Data'
# Uma linha é chamada de 'exemplo', 'registro', 'observação' ou 'amostra'(sample)
#Nome das colunas é chamada de 'variável', 'características', 'atributo' ou 'entrada', elas podem ser independentes ou depedentes(em que os valores neste domínio muda se outro domínio mudar um certo valor)
# um array de elementos é chamado de 'series'
#População: todos os dados possíveis vs Amostragem (uma parcela desses dados)

#Tipos de Dados:
#Temos dados quantitativos, que podem ser divididos em discreto (inteiro, associados a contagem) e contínuos (float, medição); Mas discreto pode ser tratado como contínuo como, por exemplo, dinheiro
#Temos qualitativos, que podem ser em nominal (não expressa um ordem como azul, verde, Brasil, etc), ordinal (como tamanho da camisa e meses) e identificador (como cpf ou rg)
#Mas temos dados quantitativos que podem ser tartados como qualitativos como grau de satisfação de um restaurante.
#Temos textos e datas

import pandas as pd

data = pd.read_csv("water_use_data_2013_to_2022.csv")
print(data.head(10))
print("\n\n")
print(data.info())
print("\n\n")
print(type(data))
print(f"\n{data.shape}\n") #retorna a dimensão da tabela

print(f"{data.columns}\n") #retorna os metadados
print(f"{list(data.columns)}\n")

ajustes = data.rename(columns={'industry':'industria', 'year':'ano'}) #,inplace=True ->para modificar permanentemente
#ou pode renomer todas as colunas através de uma lista do mesmo tamanho data.columns = ['aaa', 'bbb',...., 'ccc']
print(f"{list(ajustes)}")