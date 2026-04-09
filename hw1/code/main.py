from data_structures.Graph import Graph
from search import bfs, dfs, ucs


def build_sample_graph():
    graph = Graph()

    edges = [
        ("A", "B", 2),
        ("A", "C", 1),
        ("B", "D", 4),
        ("B", "E", 2),
        ("C", "F", 5),
        ("C", "G", 2),
        ("D", "H", 1),
        ("E", "H", 3),
        ("E", "I", 6),
        ("F", "I", 2),
        ("G", "J", 4),
        ("H", "J", 2),
        ("I", "J", 1),
    ]

    for source, target, cost in edges:
        graph.add_edge(source, target, cost)

    return graph


def print_result(name, result):
    print(f"{name}:")
    print(f"  Found: {result['found']}")
    print(f"  Path: {' -> '.join(result['path']) if result['path'] else 'None'}")
    print(f"  Cost: {result['cost']}")
    print(f"  Explored order: {result['explored_order']}")
    print()


def main():
    graph = build_sample_graph()

    print("Graph nodes:", graph.nodes())
    print()

    dfs_result = dfs(graph, "A", "J")
    bfs_result = bfs(graph, "A", "J")
    ucs_result = ucs(graph, "A", "J")

    print_result("DFS", dfs_result)
    print_result("BFS", bfs_result)
    print_result("UCS", ucs_result)


if __name__ == "__main__":
    main()
