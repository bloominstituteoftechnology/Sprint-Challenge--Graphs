"""
Simple graph implementation compatible with BokehGraph class.
"""
from draw import BokehGraph

"""Trying to make this Graph class work..."""

class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            raise Exception("Error: Cannot have edge to nonexistent vertices")
        if vertex in self.vertices:
            raise Exception("Error: Vertex already exists.")
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        # check to see if we have a starting or ending node
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error: No vertices found")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        x = []
        x.append(start)
        y = set(x)

        while x:
            z = x.pop()
            if x == target:
                break
            x.extend(self.vertices[z])

        return x

    def graph_rec(self, start, target=None):
        x = set()
        x.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

        
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label
