import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset\\Vinho\\Red.csv")

print(data.head())

print(data.info())

eixo_x = data['Year'].value_counts().sort_index().keys() #ordenar por ano
eixo_y = data['Year'].value_counts().sort_index().values

plt.plot(eixo_x, eixo_y)
plt.title("Quantidade de vinhos (Red) produzidos por ano")
plt.xticks(rotation=-45)
plt.show()