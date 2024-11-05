from repository import Repository

class SearchService:
  
  def __init__(self):
    # Initialize a database instance
    self.repository = Repository()
    
  
  def Query(self, user_input):
    # Apply LLM to build query to databse
    sql_query = self.repository.generate_query_with_llm(user_input)
    
    # Input query to repository and retrieve informations
    result = self.repository.execute_query(sql_query)
    
    # Return information
    return result
    