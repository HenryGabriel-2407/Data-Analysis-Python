import random

"""     Probabilidade       """
def random_kid():
    return random.choice(['Menino', 'Menina'])

random.seed(0)
both_girls, older_girls, eitheir_girl =  0, 0, 0

for _ in range(10000):
    younger =  random_kid()
    older = random_kid()
    if older == "Menina":
        older_girls += 1
    if older == "Menina" and  younger == "Menina":
        both_girls += 1
    if older == "Menina" or younger == "Menina":
        eitheir_girl += 1

print("P(both | older ) =", both_girls / older_girls)
print("P(both | either): ", both_girls / eitheir_girl)