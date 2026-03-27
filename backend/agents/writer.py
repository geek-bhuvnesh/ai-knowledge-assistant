from langchain_ollama import OllamaLLM

llm = OllamaLLM(model = "llama3")

def writer_agent(context, user_input):
    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{user_input}
"""
    
    response = llm.invoke(prompt)
    return response.strip()
