import numpy as np

a= np.array([1,4,2,8,5,9,2,4,3,7,0])
print(type(a))
print(np.sort(a))

zeros = np.zeros((3,8))
print(zeros)

ones = np.ones((7, 8))
print(ones)

vazio = np.empty((2,4), dtype=bool)
print(vazio)

arr = np.arange(25)
print(arr)

linspace = np.linspace(-250,624, 40, endpoint=False, retstep=True)
print(linspace)

print(np.shape(ones))
print(np.size(ones))
print(np.ndim(ones))