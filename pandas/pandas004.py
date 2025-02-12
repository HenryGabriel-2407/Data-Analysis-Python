import pandas as pd

data = pd.read_csv("dataset\\Salary Prediction of Data Professions.csv")
print(data)
data['SALARY (R$)'] = data['SALARY'] * 5.5

print(data.head())


# ACessando os índices:
data_2 = pd.DataFrame({'bom': [50, 21, 100],
                       'médio': [131, 2, 30],
                       'ruim': [30, 20, 1]}, 
                       index=['Xbox', 'Nintendo', "Playstation"])
print(data_2)
print(data_2.index)