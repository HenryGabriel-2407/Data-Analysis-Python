import pandas as pd

df = pd.DataFrame({'Empresa':['Coca-Cola', 'Pepsi'],
                   'Funcionario': [['Jonh', 'Isa'], ['Ronaldo', 'Messi', 'Lucas']]})

df_explode = df.explode('Funcionario')  
print(df_explode)
print("="*40)

df_implode = df_explode.groupby('Empresa').agg(lambda x : x.tolist())
print(df_implode)

