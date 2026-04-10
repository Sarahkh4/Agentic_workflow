from langgraph.graph import StateGraph, START, END
from .state import State
from .nodes import (
    generate_joke,
    check_punchline,
    improve_joke,
    polish_joke,
)


def build_prompt_chaining_workflow():
    builder = StateGraph(State)

    builder.add_node("generate_joke", generate_joke)
    builder.add_node("improve_joke", improve_joke)
    builder.add_node("polish_joke", polish_joke)

    builder.add_edge(START, "generate_joke")
    builder.add_conditional_edges(
        "generate_joke",
        check_punchline,
        {"Fail": "improve_joke", "Pass": END},
    )
    builder.add_edge("improve_joke", "polish_joke")
    builder.add_edge("polish_joke", END)

    return builder.compile()

def run_prompt_chaining_demo():
    chain = build_prompt_chaining_workflow()
    state = chain.invoke({"topic": "cats"})
    print("Initial joke:")
    print(state["joke"])
    print("\n--- --- ---\n")
    if "improved_joke" in state:
        print("Improved joke:")
        print(state["improved_joke"])
        print("\n--- --- ---\n")
        print("Final joke:")
        print(state["final_joke"])
    else:
        print("Final joke:")
        print(state["joke"])

