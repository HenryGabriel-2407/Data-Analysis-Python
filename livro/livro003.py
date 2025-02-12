import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.6, 5979.6, 10289.7, 14958.3]

plt.plot(years,  gdp, marker='o', color='red', linewidth=3)
plt.title('GDP of the United States Over Time')
plt.xlabel('Year')
plt.ylabel('GDP ($ billions)')

plt.show()


"""     Gráfico de Barra        """
movies = ["Harry Porta",  "El Señor de los Anillos", "El Padrino", "Gandhi", "West Side Story"]
num_oscars = [5,  4, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.ylabel("N de premiações")
plt.title("Filmes")
plt.xticks([i for i, _ in enumerate(movies)], movies)
plt.show()

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
proximidade = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
frequencia = [0] * len(proximidade)
# Cria um histograma
for grade in grades:
    for i, limites in enumerate(proximidade):
        if grade <= limites:
            frequencia[i] += 1
            break

plt.bar(proximidade, frequencia,  color='skyblue', width=5)
plt.xlabel("Intervalo de Notas")
plt.xticks(proximidade)
plt.ylabel("Frequência")
plt.title("Histograma de Notas com plt.bar")
plt.show()

"""     Gráfico de Linhas       """
variance =  [1, 2, 4, 8, 16, 32, 64,  128, 256, 512]
bias_squared = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x +  y for x, y in zip(variance, bias_squared)]
xs =  [i for i, _ in enumerate(variance)]

plt.plot(xs, variance,  label='Variance', color='green')
plt.plot(xs, bias_squared, label='bias**2',  color='red')
plt.plot(xs,  total_error, label='total error', color='blue')

plt.legend(loc=9)
plt.title('Erro de aprendizado')
plt.xlabel('Iterações')
plt.show()


"""     Gráfico de Dispersão        """
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 190, 145,  150, 190, 170]
labels =  ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank',  'George', 'Hannah', 'Ivan']
plt.scatter(friends, minutes)
for label , friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, 
                 xy = (friend_count, minute_count),
                 xytext=(5,-5),  
                 textcoords='offset points')
plt.xlabel("# de amigos")
plt.ylabel("# de minutos")
plt.show()