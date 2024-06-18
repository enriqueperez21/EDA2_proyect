def console_input():
    graph = {}
    graph_len = input_cantidad("Ingrese la cantidad de nodos: ")
    for num in range(graph_len):
        print(f"Ingresa los datos del grafo N {num}: ")
        node = input_node(graph)
        graph[node] = []
    for node in graph:
        graph[node] = input_neighbor(node, graph)
    return graph

def input_option(message):
    answer = ''
    while(True):
        answer = input(message)
        if(answer.lower() in ['yes','y']): answer = True
        elif(answer.lower() in ['no','n']): answer = False
        else: 
            print("debe ingresar un respuesta indicada")
            continue
        break
    return answer

def input_cantidad(message):
    cantidad = 0
    while(True):
        cantidad = input(message)
        try: cantidad = int(cantidad)
        except:
            print("debe ingresar un respuesta indicada")
            continue
        break
    return cantidad

def input_node(graph):
    node = None
    while(True):
        try:
            node = input("")
            try: node = int(node)
            except: pass
            if(node in graph): raise IndexError
            break
        except ValueError:
            print("valor no correcto")
        except IndexError:
            print("El nodo ya existe en el grafo")
    return node

def input_neighbor(node, graph):
    neighbors = []
    run = True
    while(run):
        try:
            neighbor = input(f"Ingrese el vecino del nodo {node} \n")
            try:
                neighbor = int(neighbor)
            except:
                pass
            if(type(neighbor) != type(node) and neighbor != ''): raise ValueError
            if(neighbor not in graph and neighbor != ''): raise IndexError
            if(neighbor != ''):
                neighbors.append(neighbor)
            run = input_option("Quieres añadir más vecinos? (yes?)\n")
        except ValueError:
            print("El nodo padre y el nodo hijo son de distintos tipos")
        except IndexError:
            print("El nodo vecino no está en el grafo")
    return neighbors

if(__name__ == "__main__"):
    result = console_input()
    print(result)