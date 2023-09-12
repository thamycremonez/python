import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializa o gerador de dados fictícios
fake = Faker()

# Cria uma lista para armazenar os dados
dados = []

# Gera 1000 linhas de dados fictícios
for _ in range(1000):
    nome_cliente = fake.company()
    cnpj_cliente = fake.unique.random_number(digits=14)
    id_cliente = random.randint(1000, 9999)
    data_cadastro = fake.date_between(start_date='-365d', end_date='today')

    dados.append([nome_cliente, cnpj_cliente, id_cliente, data_cadastro])

# Escreve os dados no arquivo CSV
with open('dados_clientes.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nome_cliente', 'cnpj_cliente', 'id_cliente', 'data_cadastro'])
    writer.writerows(dados)