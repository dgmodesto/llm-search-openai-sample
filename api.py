from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from search_service import SearchService
from load_csv_to_sqlite import LoadCSVToSQLite
import json
import os


# Criação da aplicação Flask
app = Flask(__name__)
api = Api(app, version='1.0', title='Text Processing API',
          description='API para processar texto',
          doc='/docs')


# Definindo o namespace
ns = api.namespace('text', description='Operações com texto')

# Modelo de entrada para o Swagger
text_model = api.model('TextInput', {
    'texto': fields.String(required=True, description='Texto para processamento')
})

# Endpoint POST para processar o texto
@ns.route('/process')
class TextProcessor(Resource):
    @ns.expect(text_model)
    def post(self):
        """Processa o texto recebido"""
        data = request.json
        texto = data.get('texto')
        service = SearchService()
        # Exemplo de processamento: transforma o texto para maiúsculas
        result =  service.Query(texto)  # Transformando o texto para maiúsculas como exemplo

        return jsonify({"result": result})

def loadDatabase():
  database_name = os.getenv('DATABASE_NAME')
  
  db = LoadCSVToSQLite(database_name)

  # Define o esquema da tabela
  schema = {
      "sigla": "TEXT",
      "superintendente": "TEXT",
      "ativo": "TEXT",
      "tecnologia": "TEXT",
      "versao_tecnologia": "TEXT",
      "subcategoria": "TEXT",
      "arquivo": "TEXT",
      "situacao_ativo": "TEXT",
      "data_ingestao": "TEXT",
  }

  # Cria a tabela
  db.create_table("ativos", schema)

  # Carrega os dados do CSV
  db.load_csv("./datasource/dados.csv", "ativos")

  # Fecha a conexão
  db.close()


# Inicia a aplicação Flask
if __name__ == '__main__':
  loadDatabase()
  app.run(debug=True)
