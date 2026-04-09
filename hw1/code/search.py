from data_structures import Stack, Queue, PriorityQueue

def reconstruct_path(parents, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path

def dfs(graph, start, goal):
    if not graph.has_node(start) or not graph.has_node(goal):
        return {
            "found": False,
            "path": [],
            "cost": None,
            "explored_order": []
        }
    
    stack = Stack()
    stack.push(start)

    visited = set()
    parents = {start: None}
    explored_order = []

    while not stack.is_empty():
        current = stack.pop()
        
        if current in visited:
            continue

        visited.add(current)
        explored_order.append(current)

        if current == goal:
            path = reconstruct_path(parents, goal)
            return {
                "found": True,
                "path": path,
                "cost": len(path) - 1,
                "explored_order": explored_order
            }
        
        neighbors = graph.neighbors(current)

        for neighbor, cost in reversed(neighbors):
              if neighbor not in visited and neighbor not in parents:
                parents[neighbor] = current
                stack.push(neighbor)

    return {
        "found": False,
        "path": [],
        "cost": None,
        "explored_order": explored_order
    }


def bfs(graph, start, goal):
    if not graph.has_node(start) or not graph.has_node(goal):
        return {
            "found": False,
            "path": [],
            "cost": None,
            "explored_order": []
        }

    queue = Queue()
    queue.enqueue(start)

    visited = set([start])
    parents = {start: None}
    explored_order = []

    while not queue.is_empty():
        current = queue.dequeue()
        explored_order.append(current)

        if current == goal:
            path = reconstruct_path(parents, goal)
            return {
                "found": True,
                "path": path,
                "cost": len(path) - 1,
                "explored_order": explored_order
            }

        neighbors = graph.neighbors(current)

        for neighbor, cost in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.enqueue(neighbor)

    return {
        "found": False,
        "path": [],
        "cost": None,
        "explored_order": explored_order
    }


def ucs(graph, start, goal):
    if not graph.has_node(start) or not graph.has_node(goal):
        return {
            "found": False,
            "path": [],
            "cost": None,
            "explored_order": []
        }

    pq = PriorityQueue()
    pq.push(0, start)

    parents = {start: None}
    best_cost = {start: 0}
    explored_order = []

    while not pq.is_empty():
        current_cost, current = pq.pop()

        if current_cost > best_cost[current]:
            continue

        explored_order.append(current)

        if current == goal:
            path = reconstruct_path(parents, goal)
            return {
                "found": True,
                "path": path,
                "cost": current_cost,
                "explored_order": explored_order
            }

        neighbors = graph.neighbors(current)

        for neighbor, edge_cost in neighbors:
            new_cost = current_cost + edge_cost

            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                parents[neighbor] = current
                pq.push(new_cost, neighbor)

    return {
        "found": False,
        "path": [],
        "cost": None,
        "explored_order": explored_order
    }