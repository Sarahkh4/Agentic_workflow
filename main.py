from src.prompt_chaining.workflow import run_prompt_chaining_demo
from src.parallelization.workflow import run_parallelization_demo
from src.routing.workflow import run_routing_demo

def main():
    print("Prompt Chaining")
    run_prompt_chaining_demo()
    print("Parallelization")
    run_parallelization_demo()
    print("Routing")
    run_routing_demo()



if __name__ == "__main__":
    main()
