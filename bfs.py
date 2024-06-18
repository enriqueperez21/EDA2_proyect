def get_bfs_tree(graph, start_node):
    visited = {start_node: None}
    queue = [start_node]
    tree = {}
    while queue:
        current_node = queue.pop()
        tree[current_node] = visited[current_node]
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited[neighbor] = current_node
                queue.append(neighbor)
    return tree

grafo_letras = {
    'S': ['A','B','C'],
    'A': ['D','B'],
    'B': ['F','E','C'],
    'C': ['G','H'],
    'D': ['F'],
    'F': [ ],
    'E': ['G'],
    'G': [ ],
    'H': []
}

if(__name__ == "__main__"):
    tree = get_bfs_tree(grafo_letras, 'S')
    print(tree)