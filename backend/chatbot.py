from agents.langgraph_agent import run_agent # type: ignore

print("Agentic AI Assistant (Day 4) (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = run_agent(user_input) # type: ignore

    print("\nAI:", response) # type: ignore
    print()