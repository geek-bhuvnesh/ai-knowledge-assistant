from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.writer import writer_agent

def run_multi_agent(user_input):

    # 1. Planner 
    plan = planner_agent(user_input)
    print("\n[PLANNER]:", plan)

    # 2. Research
    context = researcher_agent(plan)
    print("\n[RESEARCH]:", context)

    # 2. Research
    answer = writer_agent(context, user_input)
    print("\n[WRITER]: generating response...")

    return answer




