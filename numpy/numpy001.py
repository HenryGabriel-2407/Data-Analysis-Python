import numpy as np

lista = [1, 2, 5, 8, 12, 43, 23]

array = np.array(lista)
array2 = np.array(np.sort(lista))

print(lista)
print(array2)

zeros = np.zeros(10)
print(zeros)

matriz_zeros = np.zeros((5,6))
print(matriz_zeros)
print("\n\n")

lista_notas = [9.8, 5.6, 7.6, 10, 8.9]
print(f"A maior nota foi {np.max(lista_notas)}")
print(f"A menor nota foi {np.min(lista_notas)}")
print("A média das notas foi de {:.2f}".format(np.mean(lista_notas)))
print(f"A posição do menor é {np.argmin(lista_notas)}")
print(f"Desvio padrão: {np.std(lista_notas)}\n\n")

#Atividade!!

lista_atv = np.zeros(10)
for i in range(len(lista_atv)):
    valor = float(input(f"Digite o novo valor da posição {int(i)}: "))
    lista_atv[int(i)] = valor
print(f"\nValores inseridos: {lista_atv}")
print(f"Array crescente: {np.sort(lista_atv)}")
print(f"Maior valor: {np.max(lista_atv)}")
print(f"Menor valor: {np.min(lista_atv)}")
print("Média: {:.2f}".format(np.mean(lista_atv)))
print(f"Desvio padrão: {np.std(lista_atv)}")
