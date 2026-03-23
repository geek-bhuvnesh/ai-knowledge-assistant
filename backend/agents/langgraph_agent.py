from langchain_community.llms import Ollama # type: ignore
from tools.calculator import calculate # type: ignore
from rag.rag import search_docs # type: ignore

llm = Ollama(model="tinyllama") # type: ignore
# def agent_decision(user_input):
#     prompt = f"""
# You are an AI agent.

# Decide what to do:
# - If it's a math problem → respond with: CALCULATE: expression
# - If it's a knowledge question → respond with: RAG: query

# User input:
# {user_input}
# """

def agent_decision(user_input): # type: ignore
    prompt = f"""
You are a strict decision-making AI.

You MUST respond in ONLY ONE of the following formats:

1. CALCULATE: <math expression>
2. RAG: <search query>

DO NOT explain.
DO NOT add extra text.
ONLY output one line.

Examples:
User: What is 25 * 10?
Output: CALCULATE: 25 * 10

User: Explain embeddings
Output: RAG: embeddings

Now decide:

User: {user_input}
Output:
"""

    
    decision = llm.invoke(prompt) # type: ignore
    # Clean output
    decision = decision.strip().split("\n")[0] # type: ignore

    print("[AGENT DECISION]:", decision) # type: ignore

    return decision # type: ignore



def run_agent(user_input): # type: ignore

    decision = agent_decision(user_input) # type: ignore

    print("\n[AGENT DECISION]:", decision) # type: ignore

    # Tool path
    if decision.startswith("CALCULATE"): # type: ignore
        expression = decision.replace("CALCULATE:", "").strip() # type: ignore
        result = calculate(expression) # type: ignore
        return f"Result: {result}"
    
    # RAG path
    elif decision.startswith("RAG"): # type: ignore
        query = decision.replace("RAG:", "").strip() # type: ignore
        context = search_docs(query) # type: ignore

        prompt = f"""
Use the context below to answer:

Context:
{context}

Question:
{user_input}
"""
        return llm.invoke(prompt) # type: ignore
    
    else:
        return "I couldn't decide what to do."

