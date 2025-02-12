# concat() é usado para concatenar DataFrames (horizontalmente ou verticalmente), e merge() realiza junções do tipo SQL, combinando DataFrames com base em colunas específicas.
import pandas as pd 
import numpy as np

data = pd.DataFrame(np.random.randn(10, 4), columns= ['A', 'B', 'C', 'D'])
print(f"{data}\n\n")

parte1, parte2, parte3 = data[:3], data[3:7], data[7:]
print(f"{parte1}\n\n")
print(f"{parte2}\n\n")
print(f"{parte3}\n\n")

# Concatenar
resultado = pd.concat([parte2, parte1, parte3])
print(f"{resultado}\n\n")


left = pd.DataFrame({'key': ["foo", "foo", "foo"], "lvar": [1,2, 3]})
right = pd.DataFrame({'key': ["foo", "foo"], "rvar": [4, 5]})
result = pd.merge(left, right, on='key')
print(f"{result}\n\n")

left1 = pd.DataFrame({'key': ["foo", "bar"], "lvar": [1,2]})
right1 = pd.DataFrame({'key': ["foo", "bar"], "rvar": [4,5]})
result1 = pd.merge(left1, right1, on='key')
print(f"{result1}\n\n")


# DataFrame de clientes
clientes = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "nome": ["Alice", "Bob", "Carlos", "Diana"],
    "email": ["alice@example.com", "bob@example.com", "carlos@example.com", "diana@example.com"]
})
# DataFrame de pedidos
pedidos = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer_id": [101, 102, 101, 103, 104],
    "valor": [150.00, 200.50, 75.00, 300.00, 120.00]
})
result = pd.merge(clientes, pedidos, on='customer_id')
print(f"{result}\n\n")


# Dados de pedidos para dois meses
pedidos_jan = pd.DataFrame({
    "order_id": [1001, 1002],
    "customer_id": [101, 102],
    "valor": [150.00, 200.50]
})

pedidos_fev = pd.DataFrame({
    "order_id": [1003, 1004, 1005],
    "customer_id": [101, 103, 104],
    "valor": [75.00, 300.00, 120.00]
})
result = pd.concat([pedidos_jan, pedidos_fev])
print(f"{result}\n\n")