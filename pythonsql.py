import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-5SO7F5F;"
    "Database=cadastro;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id = 2
cliente = "Caligula"
produto = "Charrete"
data = "22/12/2021"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()