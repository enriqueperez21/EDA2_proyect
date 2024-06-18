def get_dfs_tree(graph, start_node):
    searched = {}
    for node in graph:
        searched[node] = False
    componentR = []
    tree = {}
    dfs(start_node, graph, searched, componentR, tree)
    return tree

def dfs(nodo, grafo, searched, componentR, tree):
    componentR.append(nodo)
    searched[nodo] = True

    for vecino in grafo[nodo]:
        if not searched[vecino]:
            tree[vecino] = nodo
            dfs(vecino, grafo, searched, componentR,tree)

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
    get_dfs_tree(grafo_letras, 'S')