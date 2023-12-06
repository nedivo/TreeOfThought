# Tree of Thoughts Implementation

This project implements the "Tree of Thoughts" (ToT) framework, as described in the paper ["Tree of Thoughts: Deliberate Problem Solving with LM."](https://arxiv.org/abs/2305.10601) The ToT framework is a novel approach to problem-solving using Language Models (LM), allowing for more structured and deliberate decision-making processes.

## Key Features

**Thought Generation:** Utilizing OpenAI's chat completion API, the **`TreeOfThoughts`** class generates potential next steps or "thoughts" from the current state, aligning with the ToT concept of exploring multiple reasoning paths.

**State Evaluation:** The class includes methods (`'evaluate_state'` and `'evaluate_state'`) for heuristic evaluation of states, reflecting the ToT suggestion of using heuristics to guide problem-solving.

**Search Algorithm:** A breadth-first search (BFS) approach is implemented, consistent with the ToT framework's discussion on using various search algorithms.

**Modularity and Generality:** The implementation showcases modularity with independent, cohesive components. It's adaptable to various types of problem-solving tasks.

## Setup and Installation

#### Prerequisites

- Python 3.8+
- Poetry package manager

### Development Environment Setup

To set up the development environment, use the following Makefile commands:

```bash
Copy code
make dev-env
```

This command will install necessary dependencies, set up pre-commit hooks, and create a **`.env`** file for environment variables.

### Running Locally

To run the implementation locally:

```bash
Copy code
make run-local
```

This will execute the **`main.py`** script using Poetry.

### Usage

To use the **`TreeOfThoughts`** class:

Define the initial problem and current state.
Create an instance of **`TreeOfThoughts`**.
Use the **`search`**` method to find a solution.

Example:

```python
from tree_of_thoughts import TreeOfThoughts

# Define the problem

initial_problem = "Describe your problem here."

# Define the quality threshold
quality_threshold = 8

# Define the maximum iterations
max_iterations = 3

# Create a TreeOfThoughts instance

tot = TreeOfThoughts(model="gpt-3.5-turbo", max_depth=3, breadth_limit=5, initial_problem=initial_problem)

# Find a solution

solution = tot.search(current_state=initial_problem, quality_threshold=quality_threshold, max_iterations=max_iterations)
print("Solution:", solution)
```
