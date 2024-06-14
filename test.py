class Nodo:
    def _init_(self, id):
        self.id = id
        self.vecinos = []

    def agregar_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)


class Arista:
    def _init_(self, nodo1, nodo2):
        self.nodo1 = nodo1
        self.nodo2 = nodo2


class Grafo:
    def _init_(self):
        self.nodos = {}
        self.aristas = []

    def agregar_nodo(self, id):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id)

    def agregar_arista(self, id1, id2):
        if id1 in self.nodos and id2 in self.nodos:
            self.nodos[id1].agregar_vecino(self.nodos[id2])
            self.nodos[id2].agregar_vecino(self.nodos[id1])
            self.aristas.append(Arista(self.nodos[id1], self.nodos[id2]))

    def bfs(self, inicio_id):
        if inicio_id not in self.nodos:
            return []

        inicio = self.nodos[inicio_id]
        visitados = set()
        cola = [inicio]
        resultado = []

        while cola:
            nodo_actual = cola.pop(0)
            if nodo_actual.id not in visitados:
                visitados.add(nodo_actual.id)
                resultado.append(nodo_actual.id)
                for vecino in nodo_actual.vecinos:
                    if vecino.id not in visitados:
                        cola.append(vecino)
        
        return resultado

    def dfs(self, inicio_id):
        if inicio_id not in self.nodos:
            return []

        inicio = self.nodos[inicio_id]
        visitados = set()
        pila = [inicio]
        resultado = []

        while pila:
            nodo_actual = pila.pop()
            if nodo_actual.id not in visitados:
                visitados.add(nodo_actual.id)
                resultado.append(nodo_actual.id)
                for vecino in nodo_actual.vecinos:
                    if vecino.id not in visitados:
                        pila.append(vecino)
        
        return resultado


# Ejemplo de uso:
grafo = Grafo()
grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)
grafo.agregar_nodo(4)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(3, 4)

print("BFS desde el nodo 1:", grafo.bfs(1))
print("DFS desde el nodo 1:", grafo.dfs(1))