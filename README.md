# SQL Script Generator from Free Text

This project aims to generate an SQL script based on a free-text request received via a REST API. The API takes a string of text that describes a query, and from this input, the system creates an appropriate SQL script.

## Description

This system was developed to transform free-text input into automated SQL queries, simplifying the construction of queries in databases. The input is provided via a REST API, allowing any system or user to send a request in JSON format, describing their need in natural language. The system processes this input and returns a corresponding SQL script.

**Example Input**:  
Free-text input like:  
"Show me the RBCB005 assets of the C# technology that are obsolete"

**Example Output**:  
An SQL script generated based on the text analysis.

## Features

- **Free Text Reception**: The API allows a user to send a text describing the desired query.
- **SQL Script Generation**: The system interprets the text and generates an SQL script based on the expressed query.
- **REST API**: The project exposes a RESTful API, making it easy to integrate with other systems or tools.
- **Customization**: The system can be adjusted to recognize specific business terms and generate more complex queries according to the user's needs.

## How to Run

1. **Clone the repository**

   First, clone the repository to your local machine:

   ```bash
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_FOLDER>

   ```
  
2. Install the dependencies

The project was developed with Python. Make sure you have Python 3.8+ installed. Use pip to install the dependencies:

  ```bash
  pip install -r requirements.txt
  Executar o servidor
  ```

3. Run the Flask server to start the API:

```bash
python app.py
```

The server will be available at http://127.0.0.1:5000/docs.

4. Testing the API

After starting the server, you can test the API using cURL or any tool of your choice (such as Postman or Insomnia).

Example request with cURL:
```bash
curl -X 'POST' \
  'http://127.0.0.1:5000/text/process' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "texto": "Mostre me os ativos RBCB005 da tecnologia C# que estejam obsoletos"
}'
```

5. Example response:

```json

{
  "result": [
    {
      "arquivo": "nome_arquivo",
      "ativo": "XPTOYZ005",
      "data_ingestao": "03/07/2024",
      "sigla": "XPTO",
      "situacao_ativo": "Obsoleta",
      "subcategoria": "Linguagem",
      "superintendente": "DOUGLAS MODESTO",
      "tecnologia": "C#",
      "versao_tecnologia": "1.1.0"
    }
  ]
}
```

## Architecture
The system consists of a simple REST API, implemented with Flask. It receives a request with text in JSON format, processes the text string, and generates an SQL script based on the parameters described in the input.

The input text is analyzed by a natural language processing module that interprets the keywords and structures the necessary parameters to form an SQL query.

How it Works
The API receives an HTTP POST request containing a "texto" field with the free-text query.

The server processes the text, identifying parameters like:

- Asset code (e.g., "XPTO005")
- Technology (e.g., "C#")
- Status (e.g., "obsolete")

Based on this information, the system generates an SQL script, like in the example:

```sql
SELECT * FROM ativos WHERE codigo = 'RBCB005' AND tecnologia = 'C#' AND status = 'obsoleto';
```

## Project Structure
- app.py: The main script containing the logic for the Flask server.
- requirements.txt: Contains the project's dependencies.
- /datasource: Here you will find a csv file used to load data in sqlity
- load_csv_to_sqlit_py: Contains logic to get data from csv and input inside sqlite db
- repository: Contains logic to integrate with sqlite database and open ai LLM
- search_service: Contains logic to orchestrate the lifecycle of the request
- README.md: This documentation file.

## Technologies Used
- Python: The main language used to develop the application.
- Flask: Framework for building the REST API.
- NLP (Natural Language Processing): Used to interpret and process free-text input.

## Contributing
- Contributions are welcome! Feel free to submit pull requests or report issues.

License
- This project is licensed under the MIT License - see the LICENSE file for more details.






