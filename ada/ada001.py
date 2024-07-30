import pandas as pd

lista = [28, 34, 24, 12, 55, 12, 34, 57]

serie_panda = pd.Series(lista)
print(serie_panda)

print("\n\n")
notas = {"Henry": 9.5, "Alessandra": 10, "Guilherme": 9.5, "Yago": 5.4, "Leornado":8.9}
serie_notas = pd.Series(notas)
print(serie_notas["Henry"])
print(serie_notas.mean())
print(serie_notas.median())
print(serie_notas.describe())