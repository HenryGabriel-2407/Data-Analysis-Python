def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_sub(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

v = [1,2]
w = [2,1]
print(vector_add(v,w))  # Output: [3, 3]
print(vector_sub(v,w))  # Output: [-1, 1]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,  vector)
    return result
a = [1,3,5,7]
b = [2,4,6,8]
print(vector_sum((a,b)))   # Output: [3, 7, 11, 15]

def mult_vetor(n, v):
    return [n * v_i for v_i in v]
print(mult_vetor(3, a))   # Output: [3, 9, 15, 21]

def mean(n, v):
    return sum(v) / n
print(mean(8, a))   # Output: 2.0

def produtos_vetores(v,w):
    return [v_i * w_i for v_i, w_i in zip(v,w)]
print(produtos_vetores(a,b))

import math

def magnitude(v):
    return math.sqrt(sum(produtos_vetores(v,v)))
print(magnitude(a))

def distance(v, w):
    return magnitude(vector_sub(v,w))
print(distance(a,b))

"""         MATRIZES        """
a = [[1,2,3],[4,5,6]]
b  = [[7,8],[9,10],[11,12]]

def matrix_lenght(a):
    num_rows = len(a)
    num_cols = len(a[0])
    return num_rows, num_cols
print(matrix_lenght(a))

def make_the_M(num_linha, num_col, valor):
    return [[valor
            for j in range(num_col)]
            for i in range(num_linha)]
print(make_the_M(4,6,2))

def matrix_diagonal(i,j):
    for a in range(i):
        for b in range(j):
            print('1 ' if a == b else '0 ', end='')
        print()
print(matrix_diagonal(4,4))