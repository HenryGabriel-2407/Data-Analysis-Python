from datetime import time, datetime, date
import numpy as np

for n in range(10):
    i = np.random.randn()
    print(i, end=' ')

print()
print(isinstance(i, int))

valor = 'Campeão é Botafogo em Brasília.'
print(valor.encode("utf-8"))
print(valor.encode("utf-16"))

data = datetime.now()
print(data)
print(data.day)