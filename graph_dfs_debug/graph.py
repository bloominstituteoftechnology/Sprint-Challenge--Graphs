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
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        nodes = []
        nodes.append(start)
        visited = set()

        while nodes:
            node = nodes.pop()
            if node not in visited:
                visited.add(node)
                nodes.extend(self.vertices[node])
                if node == target:
                    return True

        if target:
            return False
        else:
            return visited

    def graph_rec(self, start, target=None, visited=None):
        if visited == None:
            visited = set()

        if start not in visited:
            visited.add(start)
            for vertex in self.vertices[start]:
                if vertex == target:
                    return True
                self.graph_rec(vertex, target, visited)
        if target == None:
            return visited
        else:
            return False

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
