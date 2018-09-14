"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = label
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

"""Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        print(start)
        visited = []
        stack = []
        stack.append(start)
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                for next_vert in self.vertices[current]:
                    stack.append(next_vert)
        return visited

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
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

    def dft(self, node, visited=[]):
        print(node)
        visited.append(node)
        for child_node in self.vertices[node]:
            if child_node not in visited:
                self.dft(child_node, visited)
        return visited

    def dfs_rec(self, start, target=None, visited=[]):
        visited.append(start)
        for child in self.vertices[start]: #.edges
            if child not in visited:
                self.dft_rec(child, target, visited)
        return visited