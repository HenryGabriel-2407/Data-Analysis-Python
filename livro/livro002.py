"""     Formatação de Espaço em Branco      """
for i in [1,2,3,4,5]:
    print(i)
    for j in  [1,2,3,4,5]:
        print(j)
        print(i+j)
    print(i)
    print()
print("done")

from collections import defaultdict, Counter

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"),
    (3, "Python"), (3, "R"), (3, "machine learning"), (3, "data science"),
    (4, "machine learning"), (4, "Big Data"), (4, "Hadoop"),
    (5, "Java"), (5, "Spark"), (5, "Hadoop"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "data science"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"),
    (9, "Java"), (9, "Spark"), (9, "Cassandra")
]

user_interest =  defaultdict(list)
contador = []
for user_id, interestes, in interests:
    user_interest[user_id].append(interestes)
print(dict(user_interest))
print("\n\n")

x = [5,2,7,9,1,3]
print(sorted(x))
print("\n\n")

even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)
squares = [x*x for x in range(5)]
print(squares)
even_squares = [x*x for x in even_numbers]
print(even_numbers)
print("\n\n")

squares_dict = {x: x*x for x in range(5)}
print(squares_dict)
paris = [(x,y) for x in range(10)
         for y in range(5)]
print(paris)

"""     Geradores e Iteradores      """
# Um gerador é algo sobre o qual você pode iterar mas cujos valores são produzidos apenas quando necessários
def contador(num):
    i = 0
    while i < num:
        yield i
        i += 1

for n in contador(5):
    print(n)
print("\n\n")

"""     Enumeração      """
frutas = ["Maça", "Banana", "Abacaxi", "Laranja"]
for index, fruta in enumerate(frutas):
    print(f"O index é {index} e a fruta é {fruta}")

print("\n\n")

"""     Descompactação de Zip e Argumentos"""
lista1 = ['a', 'b', 'c', 'd']
lista2 =  [1, 2, 3, 4]
print(list(zip(lista1, lista2)))
print("\n\n")

#args e kwargs
def somar(*args):
    return sum(args)

print(somar(3,6,4,9,1)) # 23
print(somar(1.5,2,9.5,1.4)) #  14.4

def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")
print(exibir_info(nome="Henry Gabriel", idade=20, cidade="Itapema"))