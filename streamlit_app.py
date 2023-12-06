import logging

import streamlit as st

from tree_of_thoughts import TreeOfThoughts

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

st.title("Tree of Thoughts Interface")

initial_problem = st.text_input("Enter the initial problem:")

with st.expander("Advanced Options"):
    quality_threshold = st.slider(
        "Quality Threshold", min_value=1.0, max_value=10.0, value=8.0
    )
    max_iterations = st.slider("Max Iterations", min_value=1, max_value=20, value=3)

start_search = st.button("Start Search")

if start_search and initial_problem:
    progress_bar = st.progress(0)
    tot = TreeOfThoughts(
        model="gpt-4-1106-preview",
        max_depth=3,
        breadth_limit=5,
        initial_problem=initial_problem,
    )
    iterations_container = st.container()
    with iterations_container.expander("Iterations"):
        result, logs = tot.search(
            initial_problem, quality_threshold, max_iterations, progress_bar
        )
        for index, log in enumerate(logs):
            st.text_area(f"Log {index+1}", value=log, height=300, key=f"log_{index}")

    st.write("Solution:", result)
else:
    st.write("Please enter a problem to start the search.")
