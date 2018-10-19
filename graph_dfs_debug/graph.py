"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)

    # maybe just redoing this whole thing with recursion would be better

    def dfs(self, start, target, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        if start == target:
            return True
        for vert in self.vertices[start].edges:
            if vert not in visited:
                if self.dfs(vert, target, visited):
                    return True
        return False

    def graph_rec(self, start, target=None):
        visited = set()
        visited.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return visited

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
