import sqlite3
from pyDatalog import pyDatalog

# Inicializando o pyDatalog
pyDatalog.create_terms('cliente_pedido, Cliente, Pedido, fez_pedido')

# Função para se conectar ao banco de dados SQLite e carregar os dados
def carregar_dados_do_banco(nome_banco):
    # Conectando ao banco de dados
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

    # Selecionando todos os dados da tabela 'clientes'
    cursor.execute("SELECT cliente, pedido FROM clientes")
    registros = cursor.fetchall()

    # Fechando a conexão com o banco
    conexao.close()

    # Adicionando os fatos no pyDatalog
    for cliente, pedido in registros:
        +cliente_pedido(cliente, pedido)  # Corrigido para garantir que os fatos sejam adicionados
        print(f"Fato adicionado: cliente_pedido({cliente}, {pedido})")  # Debugging

# Definindo uma regra para verificar se um cliente fez um pedido específico
fez_pedido(Cliente, Pedido) <= cliente_pedido(Cliente, Pedido)

# Carregar os dados do banco de dados
carregar_dados_do_banco('clientes.db')

# Consulta: Quais clientes pediram um 'Notebook'?
clientes_notebook = fez_pedido(Cliente, 'Notebook')

# Exibindo o resultado da consulta
print("\nClientes que pediram um Notebook:")
for resultado in clientes_notebook:
    print(f"{resultado[0]} pediu Notebook")

# Consulta: Quais clientes pediram um 'Livro'?
clientes_livro = fez_pedido(Cliente, 'Livro')

# Exibindo o resultado da consulta
print("\nClientes que pediram um Livro:")
for resultado in clientes_livro:
    print(f"{resultado[0]} pediu Livro")
