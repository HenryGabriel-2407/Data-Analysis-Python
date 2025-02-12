users=[{"id": 0, 'name':"Henry Gabriel"},
        {"id": 1, 'name':"Alessandra Bregadioli"},
        {"id": 2, 'name':"Brunno"},
        {"id": 3, 'name':"Giullia"},
        {"id": 4, 'name':"Pedro"},
        {"id": 5, 'name':"Nobara"},
        {"id": 6, 'name':"Satoru Gojo"},
        {"id": 7, 'name':"Makima"},
        {"id": 8, 'name':"Inosuke"},
        {"id": 9, 'name':"Takemichi"}]

friendship = [(0,1),(0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8),  (8,9)] # relacionamentos dos users

for user in users: # para cada usuario uma lista vazia de amigos
    user["friends"] =  []
for i, j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_for_friends(user):
    return len(user["friends"])
print(sum(number_for_friends(user) for user in users))  # 24

for user in users:
    print(f"{user['name']} possui {len(user['friends'])} amigos: {[friend['name'] for friend in user['friends']]}")  # imprime o nome do usuario e a quantidade de amigos que ele tem e os nomes dos amigos

print("\n\n")
def friends_de_friends(user):
    return [foaf["id"] for friend in user["friends"]
                        for foaf in friend["friends"]]
for user in users:
    print(f'Rede de contato de {user["name"]}: {[users[foaf]["name"] for foaf in friends_de_friends(user)]}')

# Lista de interesses dos usuários
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

def  common_interests(interesses, target_interese):
    return [user_id for user_id, user_interest in interesses if user_interest == target_interese ] 

usuarios_comum = common_interests(interests, 'Java')
print(f"{[users[user_id]['name'] for user_id in usuarios_comum]}")
print("\n\n")

# Interesses mais comuns e sua quantidade
lista_interesse = {}
for user_id, interesse in interests:
    if interesse in lista_interesse:
        lista_interesse[interesse] += 1
    else:
        lista_interesse[interesse] = 1

for interesse, quantidade in lista_interesse.items():
    if quantidade > 1:
        print(f"{interesse}: {quantidade}")