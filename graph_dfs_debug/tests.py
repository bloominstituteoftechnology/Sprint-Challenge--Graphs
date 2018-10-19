from random import sample

from graph import Graph
from graph import Vertex

graph = Graph()  # Instantiate your graph

v5 = Vertex(5)
v2 = Vertex(2)
v6 = Vertex(6)
v1 = Vertex(1)
v4 = Vertex(4)
v7 = Vertex(7)
v3 = Vertex(3)
v9 = Vertex(9)

graph.add_vertex(v5)
graph.add_vertex(v2)
graph.add_vertex(v6)
graph.add_vertex(v1)
graph.add_vertex(v4)
graph.add_vertex(v7)
graph.add_vertex(v3)
graph.add_vertex(v9)


graph.add_edge(v5, v2)
graph.add_edge(v5, v6)
graph.add_edge(v2, v1)
graph.add_edge(v2, v4)
graph.add_edge(v4, v3)
graph.add_edge(v6, v7)


# for vertex in graph.vertices:
#     print(vertex)
#     print(graph.vertices[vertex])

# print(graph.dfs(v5, v9))
print(graph.graph_rec(v5, v9))

