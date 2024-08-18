# Análise de Vendas

Este projeto realiza a análise de dados de vendas utilizando Python em um Jupyter Notebook. A análise é feita com a biblioteca `pandas` para manipulação de dados e `matplotlib` para visualização dos resultados. O objetivo é analisar e apresentar informações sobre vendas, produtos e vendedores com base em um arquivo CSV de vendas.

## Funcionalidades

- **Importação de Dados**: Carregamento e visualização dos dados de vendas a partir de um arquivo CSV.
- **Manipulação de Dados**: Cálculo do total de vendas e análise por produto e vendedor.
- **Visualização**: Geração de gráficos para visualização das vendas por produto e por vendedor.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- `vendas.ipynb`: Notebook Jupyter que realiza a análise de dados e gera os gráficos.
- `tabela_vendas.csv`: Arquivo CSV contendo os dados de vendas.
- `tabela.py`: Gera um arquivo CSV  de vendas aleatorias.

## Geração do Arquivo `tabela_vendas.csv`

O arquivo `tabela_vendas.csv` é gerado por um script Python separado. Certifique-se de executar o script responsável pela criação desse arquivo para gerar os dados necessários para a análise. O script cria um DataFrame com dados de vendas e o salva em um arquivo CSV chamado `tabela_vendas.csv`.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `pandas`
- `matplotlib`

Você pode instalar as bibliotecas necessárias utilizando o seguinte comando:

```bash
pip install pandas matplotlib


## Descrição do Notebook

### Importações

O notebook importa as bibliotecas necessárias para a análise:

```python
import pandas as pd
import matplotlib.pyplot as plt

Carregamento dos Dados: Leitura do arquivo CSV contendo os dados de vendas.

python
Copiar código
df = pd.read_csv('tabela_vendas.csv')
Manipulação dos Dados:

Adiciona uma coluna com o total de vendas para cada linha.
Calcula o total de vendas por produto e por vendedor.
Identifica o melhor vendedor com base no total de vendas.
Visualização:

Gera gráficos de barras horizontais para o ranking de produtos vendidos e o ranking de vendedores.
python
Copiar código
plt.figure(figsize=(10, 5))
plt.barh(total_vendido_produto.index, total_vendido_produto.values, color='skyblue')
plt.xlabel('Vendas')
plt.ylabel('Produtos')
plt.title('Ranking de Produtos Vendidos')
plt.gca().invert_yaxis()
plt.show()

plt.figure(figsize=(10, 5))
plt.barh(total_vendas_vendedor.index, total_vendas_vendedor.values, color='navy')
plt.xlabel('Vendas')
plt.ylabel('Vendedores')
plt.title('Ranking de Vendedores')
plt.gca().invert_yaxis()
plt.show()