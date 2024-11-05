from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.sql_database import SQLDatabase
from langchain_openai import OpenAI
import os
import json

class Repository:
    def __init__(self):
        """Inicializa a conexão com o banco de dados SQLite3 usando LangChain."""
        # Inicializa o modelo OpenAI
        self.llm = OpenAI(temperature=0.0, openai_api_key=os.getenv("OPENAI_API_KEY"))
        database_name = os.getenv('DATABASE_NAME')
        
        # Inicializa a conexão com o banco de dados usando LangChain
        self.database = SQLDatabase.from_uri(f"sqlite:///{database_name}")
        
        # Define o prompt para gerar consultas SQL
        self.query_prompt = PromptTemplate(
            input_variables=["user_input"],
            template="""
            A partir da seguinte entrada do usuário, gere uma consulta SQL para buscar informações no banco de dados.
            A entrada do usuário pode conter os seguintes parâmetros: sigla, superintendente, ativo, tecnologia, versao_tecnologia, subcategoria, arquivo, situacao_ativo, data_ingestao.

            Exemplo de query sql: SELECT * FROM ativos WHERE ativo = 'RBCB005' AND tecnologia = 'C#' AND situacao_ativo = 'Obsoleta' AND subcategoria = 'Linguagem' AND arquivo = 'nome_arquivo' AND superintendente = 'DOUGLAS MODESTO' ;

            Entrada do usuário: "{user_input}"

            Gere uma consulta SQL baseada nos parâmetros mencionados acima.
            """
        )


    def generate_query_with_llm(self, usuario_input):
        """Gera uma consulta SQL usando LangChain a partir da entrada do usuário."""
        chain = LLMChain(llm=self.llm, prompt=self.query_prompt)
        sql_query = chain.run(user_input=usuario_input)
        return sql_query.strip()

    def execute_query(self, query):
        """Executa uma consulta no banco de dados e retorna os resultados."""
        results = self.database.run(query, include_columns=True)
    
        # Replace single quotes with double quotes
        formatted_string = results.replace("'", '"')

        # Convert string to JSON object
        json_object = json.loads(formatted_string)
        # Convertendo os resultados para JSON
        return json_object
