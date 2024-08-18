import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações iniciais
num_registros = 50
produtos = ['Cooler', 'SSD', 'Fonte de Alimentação', 'Placa de Vídeo', 'Memória RAM']
nomes_vendedores = ['Carlos', 'Ana', 'Pedro', 'Mariana', 'João', 'Fernanda', 'Ricardo', 'Luciana', 'José', 'Patrícia']
precos = {
    'Cooler': 500.00,
    'SSD': 800.00,
    'Fonte de Alimentação': 600.00,
    'Placa de Vídeo': 1000.00,
    'Memória RAM': 400.00
}

# Função para gerar uma data aleatória
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# Gerando dados aleatórios
data = {
    'Data': [random_date(datetime(2024, 1, 1), datetime(2024, 7, 1)).strftime("%d-%m-%Y") for _ in range(num_registros)],
    'Produto': [random.choice(produtos) for _ in range(num_registros)],
    'Quantidade': [random.randint(1, 20) for _ in range(num_registros)],
    'Preço Unitário': [0] * num_registros,  # Temporário, será atualizado depois
    'Vendedor': [random.choice(nomes_vendedores) for _ in range(num_registros)]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Atualizando a coluna de preços unitários com os preços fixos
df['Preço Unitário'] = df['Produto'].map(precos)

# Ordenando a tabela por ordem de produtos
df_sorted = df.sort_values(by="Produto")


# Salvando a tabela ordenada em um arquivo CSV
file_path = 'tabela_vendas.csv'
df_sorted.to_csv(file_path, index=False)

print(f'Arquivo CSV salvo em: {file_path}')
