from collections import deque
import networkx as nx


def shortest_path(
        graph: nx.Graph,
        source: str,
        target: str
) -> list[str]:
    queue = deque([source])
    visited = {source}
    parent = {source: None}

    while queue:
        current = queue.popleft()
        if current == target:
            break
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    if target not in parent:
        raise nx.NetworkXNoPath(
            f"No path between '{source}' and '{target}'."
        )

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path