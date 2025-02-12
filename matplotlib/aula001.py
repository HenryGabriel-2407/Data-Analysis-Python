import matplotlib.pyplot as plt
import numpy as np


"""     TIPOS DE GRÁFICO        """
"""     Gráfico de Linha"""
#                   x           y
fig = plt.plot([1,2,3,4,5], [2,4,3,8,0])
plt.title("Primeiro gráfico")
plt.show()

"""  ======================================     """

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([2, 4, 3, 8, 0, 1, 6, 9, 2, 5, 3, 8, 0])
z = plt.plot(x,y, "r--", linewidth=3)
plt.title("Gráfico de Linha", fontdict={'family': 'serif', 'size':16}, loc='center')
plt.xlabel("Paçocas")
plt.ylabel("Quantidade de Paçocas", labelpad=16)
plt.show()