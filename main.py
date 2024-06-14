# Programa principal
class Graph_search:
    def __init__(self,graph, start) :
        self.graph = graph
        self.start = start
        self.bfs_tree = self.create_bfs_tree()

    def __str__(self):
        return f"{self.graph}, bfs = {self.bfs_tree}"

    def create_bfs_tree(self):
        visited = {self.start: None}
        queue = [self.start]
        tree = {}
        while queue:
            current_node = queue.pop()
            tree[current_node] = visited[current_node]
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited[neighbor] = current_node
                    queue.append(neighbor)
        return tree
    
def create_graph(graph, start):
    graph_search = Graph_search(graph, start)
    print(graph_search)


graph1 = {
    'A' : {"C"},
    'B' : {"A"},
    'C' : {"E"},
    'D' : {"F"},
    'E' : {"B"},
    'F' : {"D"}
}

create_graph(graph1, 'A')