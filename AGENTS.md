# Repository Guidelines

## Project Structure & Module Organization
This repository is an Introduction to AI course-assignment workspace. Keep each assignment self-contained in its own numbered directory:

- `hw1/`: first assignment, including graph, tree, stack, queue, priority queue, DFS, BFS, and UCS implementations.
- `hw2/`: second assignment, including alpha-beta pruning and China map coloring requirements.
- `README.md`: repository-level overview and progress notes.

Current assignment-specific layout:

- `hw1/code/`: Python source for homework 1.
- `hw1/code/data_structures/`: `Graph`, `Tree`, `Stack`, `Queue`, and `PriorityQueue` implementations.
- `hw1/doc/`, `hw1/report.md`, `hw1/step.md`: homework 1 documentation and notes.
- `hw1/hw.jpg`: homework 1 original assignment image.
- `hw2/README.md`: homework 2 assignment summary.
- `hw2/IMPLEMENTATION_GUIDE.md`: suggested implementation plan for homework 2.
- `hw2/hw.png`: homework 2 original assignment image.

For new homework 2 implementation files, prefer the documented layout:

- `hw2/src/alpha_beta.py`: game-tree modeling and alpha-beta pruning.
- `hw2/src/map_coloring.py`: China map coloring, backtracking search, and arc consistency.
- `hw2/src/main.py`: local entry point for running homework 2 tasks.
- `hw2/tests/`: pytest tests for homework 2 algorithms.

## Build, Test, and Development Commands
There is no build system yet. Run commands from the repository root unless a homework README says otherwise.

Homework 1:

- `python hw1/code/main.py`: run DFS, BFS, and UCS examples.
- `python -m py_compile hw1/code/*.py hw1/code/data_structures/*.py`: quick syntax check.

Homework 2, once implementation files are added:

- `python hw2/src/main.py`: run both homework 2 tasks.
- `python -m py_compile hw2/src/*.py`: quick syntax check.
- `python -m pytest hw2/tests`: run homework 2 tests once present.

General:

- `python -m pytest`: run all tests once test directories exist.

Keep commands cross-machine friendly and avoid hard-coded absolute paths.

## Coding Style & Naming Conventions
Use Python 3 with 2-space indentation and UTF-8 file encoding. Prefer:

- `snake_case` for files, functions, and variables.
- `PascalCase` for classes.
- Clear names such as `graph_search.py`, `priority_queue.py`, `test_bfs.py`.

Write short docstrings for non-trivial functions. Keep each module focused on one concept.

When adding new homework 2 modules, use clear names aligned with the assignment, such as `alpha_beta.py`, `map_coloring.py`, `arc_consistency.py`, and `test_alpha_beta.py`.

## Testing Guidelines
No full test suite is present yet. When adding tests, use `pytest` and place them under the relevant homework directory, for example `hw2/tests/test_alpha_beta.py`.

For homework 1, focus on:

- correctness of DFS, BFS, and UCS traversal/output;
- edge cases such as empty graphs, disconnected nodes, and repeated states;
- basic complexity-sensitive cases for queue and stack behavior.

For homework 2, focus on:

- alpha-beta pruning final value, selected path, and pruned nodes for the exact tree in `hw2/README.md`;
- preservation of the left-to-right search order from the assignment image;
- map-coloring constraint correctness for adjacent provincial regions;
- arc consistency behavior and cases where domains are reduced or conflicts are detected.

## Commit & Pull Request Guidelines
Use short, imperative commit messages, for example:

- `Add UCS implementation`
- `Add homework 2 alpha-beta pruning`
- `Test map coloring constraints`

Keep commits scoped to one change. Include a brief PR description, affected files, and test evidence. Attach screenshots only when updating assignment images or visual outputs.

## Agent-Specific Notes
Do not overwrite assignment source images such as `hw1/hw.jpg` or `hw2/hw.png`. Treat them as source references.

Keep homework-specific code and documentation inside the matching `hwN/` directory unless a repository-level change is explicitly needed.

Update `README.md` when adding a new homework directory or changing repository-level progress. Update each homework README only when that homework's requirements, structure, or run instructions change.
