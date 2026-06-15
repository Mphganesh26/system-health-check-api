from collections import deque


def bfs_traversal(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order