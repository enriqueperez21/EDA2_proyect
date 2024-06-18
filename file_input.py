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
    with open(file_path) as file:
        directory = csv.DictReader(file)
        for row in directory:
            edges = row["edge"].split(",")
            if(edges[0] == ""):
                graph[row["node"]] = []
            else:
                graph[row["node"]] = edges
    return graph

if(__name__ == "__main__"):
    result2 = file_input("graph.csv")
    print(result2)