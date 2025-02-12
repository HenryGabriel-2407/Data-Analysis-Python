from random import randint
import matplotlib.pyplot as plt
from collections import Counter
import math

num_friendo = [11, 20, 16, 16, 9, 8, 18, 6, 4, 6, 9, 12, 20, 16, 7, 0, 8, 12, 13, 20, 8, 0, 7, 7, 14]
print(num_friendo)

friendo_count = Counter(num_friendo)
xs = range(101)
ys = [friendo_count[x] for x in xs]
plt.bar(xs, ys)
plt.axis([-2,101,0,6])
plt.title("Histograma da Contagem de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")
#plt.show()

"""     Estatísticas        """
num_points = len(num_friendo)
print(num_points)
maior_valor = max(num_friendo)
menor_valor = min(num_friendo)
print(f"O maior valor é {maior_valor} e o menor valor é {menor_valor}")
print(f"Lista ordenada: {sorted(num_friendo)}")

# Tendências Centrais
media = sum(num_friendo) / len(num_friendo)
print(f"Media: {media}")

def mediana(vetor):
    n = len(vetor)
    sorted_v =  sorted(vetor)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        return (sorted_v[lo] + sorted_v[midpoint]/2)
print(f"Mediana: {mediana(num_friendo)}")

def quartil(vetor, p):
    p_index = int(p*len(vetor))
    return sorted(vetor)[p_index]
print(f"Quatil do vetor (0.1): {quartil(num_friendo, 0.1)}")
print(f"Quatil do vetor (0.25): {quartil(num_friendo, 0.25)}")
print(f"Quatil do vetor (0.5): {quartil(num_friendo, 0.5)}")
print(f"Quatil do vetor (0.75): {quartil(num_friendo, 0.75)}")
print(f"Quatil do vetor (0.9): {quartil(num_friendo, 0.9)}")

def moda(vetor):
    counts = Counter(vetor)
    max_counts = max(counts.values())
    moda = [x_i for x_i, count in counts.items()
            if  count == max_counts]
    return moda
print(f"Moda: {moda(num_friendo)}")

"""     Dispersão       """
# Amplitude:
print(f"Amplitude: {max(num_friendo) - min(num_friendo)}")

# Variância:
def de_mean(x):
    x_bar = sum(x) / len(x)
    return [x_i - x_bar for x_i in x]

def variancia(vetor):
    n = len(vetor)
    deviations = de_mean(vetor)
    return  sum([x_i**2 for x_i in deviations]) / (n - 1)

print(variancia(num_friendo))

#desvio padrão
print(f"Desvio padrão: {math.sqrt(variancia(num_friendo))}")

# difereça entre os percentos 75% e 25%
def interquartile_range(vetor):
    return quartil(vetor, 0.75) - quartil(vetor, 0.25)
print(f"Percentos: {interquartile_range(num_friendo)}")

# Covariância
vetor_daily_site = [20,3,0,8,7,7,4,3,17,2,18,13,1,0,2,6,7,16,19,0,17,6,20,17,13]
def covarience(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    return  sum([(x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y)]) / (n - 1)
print(f"Covariância: {covarience(num_friendo, vetor_daily_site)}")

# Correlação
def correlacao(x, y):
    stdev_x =  math.sqrt(variancia(x))
    stdev_y =  math.sqrt(variancia(y))
    if stdev_x > 0 and stdev_y > 0:
        return covarience(x, y) / stdev_x /  stdev_y
    else:
        return 0 # se não tiver amplitude, a correlção é zero
    
print(f"Correlação: {correlacao(num_friendo, vetor_daily_site)}")

