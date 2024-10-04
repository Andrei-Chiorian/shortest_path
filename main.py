my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


def shortest_path(graph, start, target=''):
    """
    Computes the shortest distances from the start node to each node in the graph
    and builds the shortest path from the start to each node.

    Parameters
    ----------
    graph : dict
        Adjacency list for the graph, where each key is a node and the value
        is a list of tuples of the form (neighbour, distance).
    start : str
        The node from which to start the search.
    target : str (optional)
        The target node for which to print the shortest path.

    Returns
    -------
    distances : dict
        A dictionary mapping each node to its shortest distance from the start.
    paths : dict
        A dictionary mapping each node to a list of all nodes in the shortest
        path from the start to that node.
    """
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    # Iterate through the nodes, always choosing the one with the shortest
    # distance from the start
    while unvisited:
        current = min(unvisited, key=distances.get)
        # Iterate through the neighbours of the current node
        for node, distance in graph[current]:
            # If a shorter path to this neighbour is found, update the distance
            # and the path
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    return distances, paths


shortest_path(my_graph, 'A')

shortest_path(my_graph, 'A', 'F')