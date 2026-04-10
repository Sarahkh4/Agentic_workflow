from typing_extensions import TypedDict


class State(TypedDict):
    topic: str
    joke: str
    improved_joke: str
    final_joke: str