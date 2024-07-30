import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset\\Vinho\\Red.csv")

eixo_x = data['Country'].value_counts().keys()
eixo_y = data['Country'].value_counts().values

plt.title("Países que produzem vinho (red)") #título
plt.xticks(rotation=-70) #ângulo do texto debaixo do gráfico
plt.bar(eixo_x, eixo_y) 
plt.xlabel("Países")
plt.ylabel("Quantidade")
plt.show()