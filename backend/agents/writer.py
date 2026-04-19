from langchain_ollama import OllamaLLM

llm = OllamaLLM(model = "llama3")

def writer_agent(context, user_input, memory):
    prompt = f"""
Conversation history:
{memory}    
Answer the question using the context below.

Context:
{context}

Question:
{user_input}
"""
    
    response = llm.invoke(prompt)
    return response.strip()
