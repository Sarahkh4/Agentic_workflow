from .state import State
from langgraph.graph import StateGraph, START, END
from .nodes import (
    call_llm_1,
    call_llm_2,
    call_llm_3,
    aggregator,
)

def build_parallelization_workflow():
    # Build workflow
    parallel_builder = StateGraph(State)

    # Add nodes
    parallel_builder.add_node("call_llm_1", call_llm_1)
    parallel_builder.add_node("call_llm_2", call_llm_2)
    parallel_builder.add_node("call_llm_3", call_llm_3)
    parallel_builder.add_node("aggregator", aggregator)

    parallel_builder.add_edge(START, "call_llm_1")
    parallel_builder.add_edge(START, "call_llm_2")
    parallel_builder.add_edge(START, "call_llm_3")
    parallel_builder.add_edge("call_llm_1", "aggregator")
    parallel_builder.add_edge("call_llm_2", "aggregator")
    parallel_builder.add_edge("call_llm_3", "aggregator")
    parallel_builder.add_edge("aggregator", END)

    return parallel_builder.compile()


def run_parallelization_demo():
    workflow = build_parallelization_workflow()
    state = workflow.invoke({"topic": "space exploration"})
    print(state["combined_output"])

