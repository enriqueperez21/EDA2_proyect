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

def display_menu():
    print("Menú de Opciones:")
    print("1. Leer archivo CSV y mostrar grafo")
    print("2. Salir")

def main():
    graph = {}
    start = ''
    run_menu = True
    print("---  PROYECTO EDA2   ---")
    while run_menu:
        display_menu()
        choice = input("Seleccione una opción (1-2): ")
        match(choice):
            case "1":
                file_path = input("Ingrese la ruta del archivo CSV: ")
                graph = file_input(file_path)
                run_menu = False
            case "2":
                graph = console_input()
                run_menu = False
            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")
    while(True):
        start = input("Ingrese el nodo Start:\n")
        try:
            start = int(start)
            if(start not in graph): raise ValueError

        except ValueError: print("El inicial no está en el grafo")

        except: continue
        break
    my_graph = create_graph(graph, start)
    print(f"BFS tree: {my_graph.bfs_result}")
    print(f"DFS tree: {my_graph.dfs_result}")
    nodo_target = ''
    while(True):
        nodo_target = input("Ingrese el nodo a buscar:\n")
        try:
            try:
                nodo_target = int(nodo_target)
            except: pass
            if(start not in graph): raise ValueError
        except ValueError: print("El inicial no está en el grafo")
        except: continue
        break
    print(my_graph.get_bfs_path(nodo_target))
    print(my_graph.get_dfs_path(nodo_target))

main()