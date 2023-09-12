

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
    id_cliente = random.randint(1000, 9999)
    data_pagamento = fake.date_between(start_date='-30d', end_date='today')
    valor_pagamento = round(random.uniform(10.00, 1000.00), 2)
    id_pagamento = random.randint(1, 1000)

    dados.append([id_cliente, data_pagamento, valor_pagamento, id_pagamento])

# Escreve os dados no arquivo CSV
with open('dados_pagamento.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id_cliente', 'data_pagamento', 'valor_pagamento', 'id_pagamento'])
    writer.writerows(dados)