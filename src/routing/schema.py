from typing_extensions import Literal
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage, SystemMessage
from src import get_llm

# Schema for structured output to use as routing logic
#Literal means that the step variable can only store these three values
#Field(None, means default value)


class Route(BaseModel):
    step: Literal["poem", "story", "joke"] = Field(
        None, description="The next step in the routing process"
    )


