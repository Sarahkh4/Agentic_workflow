
from typing import TYPE_CHECKING
from langchain.chat_models import init_chat_model
if TYPE_CHECKING:
    from langchain_core.language_models.chat_models import BaseChatModel

import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(
    model: str = "gpt-4o-mini", **kwargs
) -> "BaseChatModel":
    return init_chat_model(
        model=model,
        model_provider="openai",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        **kwargs,
    )