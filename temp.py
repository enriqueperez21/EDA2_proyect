def dfs(nodo, grafo, searched, componentR):
    componentR.append(nodo)
    searched[nodo] = True
    print(searched)
    print('Vecinos de',nodo,':',grafo[nodo])

    for vecino in grafo[nodo]:
        if not searched[vecino]:
            dfs(vecino, grafo, searched, componentR)
            print('Finaliza', vecino)
            print('Vuelve a',nodo)
            print()



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

nodoS='S'
searched = {}
for node in grafo_letras:
    searched[node] = False
componentR = []

dfs(nodoS, grafo_letras, searched, componentR)
print(f"La búsqueda DFS es: {componentR}")