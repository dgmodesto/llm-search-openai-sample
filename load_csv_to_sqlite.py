import sqlite3
import pandas as pd

class LoadCSVToSQLite:
    def __init__(self, db_file):
        """Inicializa a conexão com o banco de dados SQLite3."""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, schema):
        """Cria uma tabela no banco de dados com base no schema fornecido."""
        columns = ', '.join(f"{col} {dtype}" for col, dtype in schema.items())
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        self.cursor.execute(create_table_query)

    def load_csv(self, csv_file, table_name):
        """Carrega os dados do arquivo CSV para a tabela especificada."""
        # Lê os dados do CSV
        data = pd.read_csv(csv_file)

        # Insere os dados no banco de dados
        data.to_sql(table_name, self.connection, if_exists='append', index=False)

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

# # Exemplo de uso
# if __name__ == "__main__":
#     db = CSVToSQLite("meu_banco_de_dados.db")

#     # Define o esquema da tabela
#     schema = {
#         "id": "INTEGER PRIMARY KEY",
#         "nome": "TEXT",
#         "idade": "INTEGER",
#         "email": "TEXT"
#     }

#     # Cria a tabela
#     db.create_table("usuarios", schema)

#     # Carrega os dados do CSV
#     db.load_csv("dados.csv", "usuarios")

#     # Fecha a conexão
#     db.close()
