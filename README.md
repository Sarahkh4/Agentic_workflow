# Agentic_workflow

This project demonstrates three core LangGraph / LangChain patterns using `gpt‑4o‑mini` (or any OpenAI‑compatible model):  
- **Prompt chaining** (sequential LLM calls)  
- **Parallelization** (multiple LLM calls in parallel, then aggregation)  
- **Routing** (LLM‑driven routing to different branches).

All code runs cleanly from the terminal using `uv`.

## 🛠 Requirements

You need:
- Python ≥ 3.10
- `uv` (fast Python package manager)

Install `uv` (Linux/macOS):

```bash
curl --proto '=https' --tlsv1.2 -sSf https://install.astral.sh/uv | sh
source $HOME/.cargo/env
uv --version
```

Then install dependencies in the project root:

```bash
cd langgraph_workshop
uv add langgraph langchain
```

Or create a `requirements.txt`:

```txt
langgraph
langchain
python-dotenv  # optional, if you want .env
```

and run:

```bash
uv add -r requirements.txt
```

[web:12][web:19]

## 🔐 API key

Copy your OpenAI API key into `.env`:

```bash
# .env
OPENAI_API_KEY="your-api-key-here"
OPENAI_BASE_URL="https://api.openai.com/v1"
```

## 🚀 Run from terminal with `uv`

Start your project:

```bash
cd langgraph_workshop
uv run main.py
```

This will:
- Run the **prompt chaining** demo (joke → improve → polish).
- Run the **parallelization** demo (joke + story + poem in parallel).
- Run the **routing** demo (LLM decides whether to generate poem/story/joke).

Example behavior:

```bash
=== Prompt chaining demo ===
Initial joke:
Why are cats great at math? Because they already know how to count to purr…

... (improved and polished joke follows)

=== Parallelization demo ===
Here's a story, joke, and poem about cats!

STORY:
...

JOKE:
...

POEM:
...

=== Routing demo ===
Once upon a time, there was a cat named Mittens who decided to become a comedian...
```

You can also run individual workflows directly:

```bash
uv run "src/prompt_chaining/workflow.py"
uv run "src/parallelization/workflow.py"
uv run "src/routing/workflow.py"
```

(But `main.py` is the recommended entrypoint.)

[web:11][web:17]

## 📝 Code notes

- `src/config/__init__.py` exports `get_llm()` so all three patterns reuse the same `init_chat_model`.  
- Type hints use `if TYPE_CHECKING:` to avoid importing `BaseChatModel` at runtime, improving startup time and avoiding circular‑import issues during type checking. [web:24][web:26]

This project is a minimal playground for learning LangGraph workflows, prompt chaining, parallelization, and routing in a structured, editable VS Code layout.
