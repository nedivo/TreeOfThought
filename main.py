import logging

from tree_of_thoughts import TreeOfThoughts

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# Example usage
def solve_problem(current_state, initial_problem, quality_threshold, max_iterations):
    logging.debug("Solve Problem")
    tot = TreeOfThoughts(
        model="gpt-4-1106-preview",
        max_depth=3,
        breadth_limit=5,
        initial_problem=initial_problem,
    )
    logging.debug("TreeOfThoughts")
    solution = tot.search(current_state, quality_threshold, max_iterations)
    logging.info("Solution: %s", solution)
    return solution


# Solve a specific problem
current_state = (
    "I need to find the way to transition a Twilio phone call to Twilio SMS."
)
initial_problem = (
    "I need to find the way to transition a Twilio phone call to Twilio SMS."
)
quality_threshold = 8.0  # For example, 8 out of 10
max_iterations = 10  # For example, max 10 iterations
result = solve_problem(
    current_state, initial_problem, quality_threshold, max_iterations
)
