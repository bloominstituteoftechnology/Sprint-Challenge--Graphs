"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, edgeStart, edgeEnd):
        if edgeStart in self.vertices and edgeEnd in self.vertices:
            self.vertices[edgeStart].edges.add(edgeEnd)
            self.vertices[edgeEnd].edges.add(edgeStart)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directional_edge(self, edgeStart, edgeEnd):
        if v1 in self.vertices:
            self.vertices[edgeStart].edges.add(edgeEnd)
        else:
            raise IndexError("That vertex does not exist!")

    # def dfs(self, start, target=None):
    #     x = []
    #     x.append(start)
    #     y = set(x)

    #     while x:
    #         z = x.pop()
    #         if x == target:
    #             break
    #         x.extend(self.vertices[z])

    #     return x

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x

    # def find_components(self):
    #     visited = set()
    #     current_component = 0

    #     for vertex in self.vertices:
    #         if vertex in visited:
    #             reachable = self.dfs(vertex)
    #             for other_vertex in reachable:
    #                 other_vertex.component = current_component
    #             current_component += 1
    #             visited.update(reachable)
    #     self.components = current_component

class Vertex:
    def __init__(self, vertex, x=None, y=None):
        self.id = vertex
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    def __repr__(self):
        return 'Vertex: ' + self.label
