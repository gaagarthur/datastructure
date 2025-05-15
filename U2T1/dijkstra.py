import math
import networkx as nx

def classic_dijkstra_path(G, source_node, target_node, weight="length"):
    # Initialize distances and predecessors
    dist = {node: math.inf for node in G.nodes}
    prev = {node: None for node in G.nodes}
    dist[source_node] = 0
    visited = set()

    while len(visited) < len(G):
        # Select the unvisited node with the smallest distance
        current = min(
            (node for node in G.nodes if node not in visited),
            key=lambda node: dist[node],
            default=None
        )

        if current is None or dist[current] == math.inf:
            break  # Remaining nodes are unreachable

        visited.add(current)

        # Use successors for directed graphs
        for neighbor in G.successors(current):
            if neighbor in visited:
                continue

            # Handle MultiDiGraph: choose the edge with the minimum weight
            min_weight = math.inf
            for _, edge_data in G[current][neighbor].items():
                w = edge_data.get(weight, 1)
                if w < min_weight:
                    min_weight = w

            alt = dist[current] + min_weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current

    # Reconstruct the path
    if dist[target_node] == math.inf:
        raise nx.NetworkXNoPath(f"No path from {source_node} to {target_node}")

    path = []
    current = target_node
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path