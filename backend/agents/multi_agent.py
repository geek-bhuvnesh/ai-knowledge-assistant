from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.writer import writer_agent

memory = []
def run_multi_agent(user_input):

    global memory
    # 1. Planner 
    plan = planner_agent(user_input, memory)
    print("\n[PLANNER]:", plan)

    # 2. Research
    context = researcher_agent(plan)
    print("\n[RESEARCH]:", context)

    # 3. Writer
    answer = writer_agent(context, user_input, memory)
    print("\n[WRITER]: generating response...")

    # 4. Update memory 
    memory.append({"user": user_input})
    memory.append({"ai": answer})

    return answer


