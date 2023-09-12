import random

# Gere uma lista de 1000 números aleatórios entre 1 e 4
coluna = [random.randint(1, 4) for _ in range(1000)]

# Imprima a coluna
for numero in coluna:
    print(numero)