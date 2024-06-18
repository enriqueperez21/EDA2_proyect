from console_input  import console_input
from file_input     import file_input
from graph          import create_graph

graph1 = {
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

my_graph = create_graph(graph1, 'S')
print(my_graph.get_bfs_path('G'))
print(my_graph.get_dfs_path('G'))