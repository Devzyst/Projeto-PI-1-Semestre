import mysql.connector

def conectar():
    """
    Cria uma conexao com o banco de dados MySQL do projeto.

    Args:
        None.

    Returns:
        mysql.connector.connection.MySQLConnection: Conexao ativa com o banco.
    """
    
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="#Dukduk02",
        database="projetointegrador_db")
