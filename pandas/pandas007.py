import pandas as pd

data = pd.read_csv("dataset\\Vinho\\Red.csv")

selecao = (data['Country'] == 'Brazil') & (data['Price'] <= 15.00) # | --> OR ; ~ --> NOT
print(data[selecao])
print("\n\n")

print(data.query('Country == "France" and Rating >= 3.6'))
print("\n\n")

lista_ano = ['2011', '2014', '2017']
print(data.query('Year in @lista_ano'))
print("\n\n")

for index, row in data.head(10).iterrows():
    print(f'{index} --> {row["Region"]} - {row["Country"]}')

print(data['Country'].value_counts())