import json
import random

# Função para gerar uma lista de temperaturas aleatórias
def generate_random_temperatures(size):
    return [random.randint(15, 35) for _ in range(size)]

# Conjunto de dados ordenado
ordered_data = generate_random_temperatures(100)
ordered_data.sort()

# Conjunto de dados inversamente ordenado
reversed_data = generate_random_temperatures(100)
reversed_data.sort(reverse=True)

# Conjunto de dados aleatório
random_data = generate_random_temperatures(100)

# Criando o arquivo JSON
data = {
    "ordered": ordered_data,
    "reversed": reversed_data,
    "random": random_data
}

with open('temperaturas_100.json', 'w') as f:
    json.dump(data, f, indent=4)