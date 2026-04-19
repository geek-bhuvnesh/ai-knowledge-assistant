# from agents.langgraph_agent import run_agent # type: ignore //Day 4

from agents.multi_agent import run_multi_agent

print("Agentic AI Assistant (Day 4) (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # response = run_agent(user_input) # type: ignore //Day 4

    response = run_multi_agent(user_input)

    print("\nAI:", response) # type: ignore
    print()