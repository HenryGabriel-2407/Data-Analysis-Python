import pandas as pd
import numpy as np

dates = pd.date_range('24/07/2024', periods=6)

data = {
    "A": [0.5, 1.2, np.nan, 0.3, 0.9, np.nan],
    "B": [np.nan, 0.7, -1.0, 2.1, np.nan, 1.3],
    "C": [1.0, 0.4, np.nan, 0.8, -0.5, np.nan],
    "D": [5, 5, 5, 5, 5, 5]
}
# np.nan serve para representar valores faltantes e qualquer operação será ignorada
df = pd.DataFrame(data, index=dates)
print(f"{df}\n\n")

df1 = df.reindex(index=dates[0:4], columns=list(data) + ['E']) # index 4 datas e criar uma nova coluna
print(f"{df1}\n\n")

df_sem_nan = df.dropna() # remover linhas com valores NaN
print(f"{df_sem_nan}\n\n")

df_com_valores = df1.fillna(value=0)  # preencher valores NaN com 0
print(f"{df_com_valores}\n\n")
print(sum(df_com_valores['A']))

df2 = pd.isna(df1)  # verificar se há valores NaN
print(f"{df2}\n\n")


"""     ESTATÍSTICAS        """
# Média
df1_media = df1['A'].mean()
print(f"{df1_media}\n\n")
df1_media_1 = df1.mean(axis=1)
print(f"{df1_media_1}\n\n") #  média por linha


""" Funções definidas pelo user     """
a = df.agg(lambda x: np.mean(x) * 2.5 ) # função lambda para calcular a média por linha e multiplicar por 2.5
print(f"{a}\n\n")

b = df.transform(lambda x: x * 2) # função lambda para multiplicar todos os valor por 2
print(f"{b}\n\n")

"""Trabalhando com Strings"""
series = pd.Series(["Python", "Data Science", "Pandas"])
print(f"{series}\n\n")
print(f"{series.str.upper()}\n\n")
print(f"{series.str.lower()}\n\n")

print(f"{series.str.replace('a', '@')}\n\n")
print(f"{series.str.split(' ')}\n\n")


emails = pd.Series([
    "alice.smith@example.com",
    "bob.jones@dataanalytics.org",
    "carla_diaz@university.edu",
    "david.wang@techworld.net",
    "emma.wilson@company.co.uk",
    "frank.miller@business.com",
    "grace_hill@nonprofit.org",
    "henry.brown@startup.io",
    "isabel.green@oldschool.edu",
    "john_doe@creativeagency.biz",
    "karen.taylor@corporate.us",
    "liam.james@travelcompany.com",
    "maria.gomez@webapp.dev",
    "nathan.lee@ecommerce.shop",
    "olivia.jones@digitalmarket.net"
])
for email in emails:
    print(f"{email.split('@')[1]}; ",end='')
print("\n\n")