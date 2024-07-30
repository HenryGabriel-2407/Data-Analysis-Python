import pandas as pd

dct = {'Autores':['J.K. Rownling', 'Machado de Assis', 'George Orwell', 'Alessandra Bregadioli'], 
        'Títulos':['Harry Potter e o Cálice de Fogo', 'Memórias Póstumas de Brás Cubas', '1984', 'Folha Amarela'],
        'Preços': [25.40, 19.80, 20.50, 15.90]}

df = pd.DataFrame(dct)
print(df)

print(f"{df['Autores']}\n")

print(f"{df['Títulos'][2]}\n")

mascara = df['Autores'] == 'George Orwell'
print(f"{mascara}\n")

print(f"{df[mascara]}\n")

nova_linha = pd.DataFrame({'Autores': ['Henry Gabriel'], 'Títulos': ['O Inferno Congela'], 'Preços': [25.40]})
df= pd.concat([df, nova_linha], ignore_index = True)

print(f"{df}\n")
mascara = df['Títulos'] == 'O Inferno Congela'
df.loc[mascara, 'Títulos'] = 'O Inferno Congelado'

print(f"{df}\n")