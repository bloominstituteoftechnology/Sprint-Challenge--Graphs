"""
Simple graph implementation compatible with BokehGraph class.
"""
from draw import BokehGraph
from sys import argv


class Vertex:
    def __init__(self, label, component=-1, **pos):
        self.label = str(label)
        self.component = component
        self.pos = pos
        self.edges = set()

    def __repr__(self):
        return "Vertex: " + self.label + self.edges

    def __str__(self):
        if not self.pos:
            pos = dict(x=None, y=None)

    """Trying to make this Graph class work..."""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
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
