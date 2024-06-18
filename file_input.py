import csv

""" The csv file needs the node,edge first line like this:
node,edge
A,"B,C,D"
B,"C,D"
C,"D"
D,""
 """

def file_input(file_path):
    graph = {}
    try:
        with open(file_path) as file:
            directory = csv.DictReader(file)
            for row in directory:
                edges = row["edge"].split(",")
                if(edges[0] == ""):
                    graph[row["node"]] = []
                else:
                    graph[row["node"]] = edges
        return graph
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    

if(__name__ == "__main__"):
    result2 = file_input("graph.csv")
    print(result2)
    result3 = file_input("catedrales.csv")
    print(result3)

