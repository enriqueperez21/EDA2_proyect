from dfs            import get_dfs_tree
from bfs            import get_bfs_tree

class Node:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, fuente, destino):
        self.fuente = fuente
        self.destino = destino

    def get_destino(self):
        return self.destino.value

class Graph:
    def load_nodes(self,grafo_dictionary):
        for node in grafo_dictionary:
            node_object = self.dictionary_graph[node]
            aristas = []
            if grafo_dictionary[node] == None:
                self.graph[node_object] = None
                continue
            for conected_node in grafo_dictionary[node]:
                if conected_node not in self.dictionary_graph:
                    node_object_dest = Node (conected_node)
                else:
                    node_object_dest = self.dictionary_graph[conected_node]
                arista = Edge(node_object, node_object_dest)
                aristas.append(arista)
                self.edges.append(arista)
            self.graph[node_object] = aristas

    def __init__(self, grafo_dictionary):
        self.graph = {}
        self.dictionary_graph = {}
        self.edges = []
        for node in grafo_dictionary:
            new_node = Node(node)
            self.dictionary_graph[node] = new_node
            self.graph[new_node] = []
        
        self.load_nodes(grafo_dictionary)

    def get_value(self,node):
        node_object = self.dictionary_graph[node]
        return self.graph[node_object]


# Programa principal
class Graph_search:
    def __init__(self,graph, start):
        self.graph    = Graph (graph)
        self.start    = start
        self.bfs_tree = Graph (get_bfs_tree(graph, start))
        self.dfs_tree = Graph (get_dfs_tree(graph, start))

    def __str__(self):
        return f"{self.graph}, bfs = {self.bfs_tree}"
    
    def get_dfs_path(self, target):
        return self.get_path(target, self.dfs_tree)
    
    def get_bfs_path(self, target):
        return self.get_path(target, self.bfs_tree)

    def get_path(self,target_node, tree):
        path = [target_node]
        while(target_node != self.start):
            for edge in tree.edges:
                if edge.fuente.value == target_node:
                    path.append(edge.destino.value)
                    target_node = edge.destino.value
        path = path[::-1]
        return path

def create_graph(graph, start):
    my_graph = Graph_search(graph, start)
    return my_graph