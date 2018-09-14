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
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        visited = []
        stack.append(start)
        while len(stack) > 0:
            current_node = stack.pop(0)
            if current_node == target:
                return visited
            if current_node not in visited:
                visited.append(current_node)
            for next_verts in self.vertices[current_node]:
                if next_verts not in visited:
                    stack.append(next_verts)
        return visited

    def graph_rec(self, start, target=None, visited=set()):
        visited.add(start)
        if self.vertices[start] == target:
            return visited
        for child_vertex in self.vertices[start]:
            if child_vertex not in visited:
                self.graph_rec(child_vertex, target)
        return visited

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
