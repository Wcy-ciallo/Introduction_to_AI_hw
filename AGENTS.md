# Repository Guidelines

## Project Structure & Module Organization
This repository is currently a small course-assignment workspace. The root directory contains:

- `作业内容.jpg`: the original assignment image.
- `作业内容总结.txt`: a text summary extracted from the image.

If you add implementation files, keep the layout simple:

- `src/`: Python source files such as graph, queue, stack, DFS, BFS, and UCS implementations.
- `tests/`: automated tests for search algorithms and data structures.
- `assets/`: images or sample input data if more assignment material is added.

## Build, Test, and Development Commands
There is no build system yet. For Python-based additions, use these commands from the repository root:

- `python -m py_compile src\\*.py`: quick syntax check.
- `python -m pytest tests`: run automated tests once a `tests/` folder exists.
- `python src\\main.py`: run a local entry point if one is added.

Keep commands cross-machine friendly and avoid hard-coded absolute paths.

## Coding Style & Naming Conventions
Use Python 3 with 4-space indentation and UTF-8 file encoding. Prefer:

- `snake_case` for files, functions, and variables.
- `PascalCase` for classes.
- Clear names such as `graph_search.py`, `priority_queue.py`, `test_bfs.py`.

Write short docstrings for non-trivial functions. Keep each module focused on one concept.

## Testing Guidelines
No test suite is present yet. When adding tests, use `pytest` and place them in `tests/` with names matching `test_*.py`.

Focus on:

- correctness of DFS, BFS, and UCS traversal/output;
- edge cases such as empty graphs, disconnected nodes, and repeated states;
- basic complexity-sensitive cases for queue and stack behavior.

## Commit & Pull Request Guidelines
This folder is not currently a Git repository, so no local commit history is available to infer conventions. If version control is added:

- use short, imperative commit messages, for example: `Add UCS implementation`;
- keep commits scoped to one change;
- include a brief PR description, affected files, and test evidence;
- attach screenshots only when updating assignment images or visual outputs.

## Agent-Specific Notes
Do not overwrite `作业内容.jpg`. Treat it as the source reference. Update `作业内容总结.txt` only when the image-based assignment content changes.
