import ollama
from rag.rag import search_docs # type: ignore
from tools.calculator import calculate

print("Agentic AI Assistant (type 'exit' to quit)\n")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # 🔥 STEP 1: Tool decision
    if "calculate" in user_input.lower():
        expression = user_input.lower().replace("calculate", "").strip()
        tool_result = calculate(expression)

        print("\n[TOOL USED: Calculator]")
        print("AI:", tool_result)
        print()
        continue

    # 🔥 STEP 2: RAG flow
    context = search_docs(user_input)

    print("\n[DEBUG CONTEXT]:", context)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{user_input}
"""

    messages.append({"role": "user", "content": prompt}) # type: ignore

    response = ollama.chat(
        model="llama3",
        messages=messages # type: ignore
    )

    ai_reply = response["message"]["content"]

    messages.append({"role": "assistant", "content": ai_reply}) # type: ignore

    print("\nAI:", ai_reply)
    print()