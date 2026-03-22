import ollama
from rag.rag import search_docs

print("RAG AI Assistant (type 'exit' to quit)\n")

messages = []   # ✅ ADD THIS LINE

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Get context from docs
    context = search_docs(user_input)
    print("\n[DEBUG CONTEXT]:", context)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{user_input}
"""

    messages.append({"role": "user", "content": prompt})

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    messages.append({"role": "assistant", "content": ai_reply})

    print("\nAI:", ai_reply)
    print()