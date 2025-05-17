import math
import networkx as nx

def classic_dijkstra_path(G, source_node, target_node, weight="length"):
        # Initialize distances and predecessors
    dist = {node: math.inf for node in G.nodes}
    prev = {node: None for node in G.nodes}
    dist[source_node] = 0

    # Set of visited nodes
    visited = set()

    while len(visited) < len(G.nodes):
        # Find the unvisited node with the smallest distance
        min_dist = math.inf
        u = None
        for node in G.nodes:
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                u = node

        if u is None:  # All remaining nodes are unreachable
            break

        visited.add(u)

        # Relaxation step
        for v in G.successors(u):
            min_weight = math.inf
            for key in G[u][v]:
                edge_data = G[u][v][key]
                edge_weight = edge_data.get(weight, 1)  # default weight is 1
                if edge_weight < min_weight:
                    min_weight = edge_weight

            if dist[u] + min_weight < dist[v]:
                dist[v] = dist[u] + min_weight
                prev[v] = u

    # Reconstruct the path from source to target
    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()

    if path and path[0] == source_node:
        return path
    else:
        return []  # No path found