from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def planner_agent(user_input, memory):
    prompt = f"""
You are a planner.

Conversation history: 
{memory}

Convert the user question into a short search query.

Only return the query.

User: {user_input}
"""
    
    response = llm.invoke(prompt)
    return response.strip()



