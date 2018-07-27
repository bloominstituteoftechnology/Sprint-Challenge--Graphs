"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return "Vertex: " + self.label

    """Trying to make this Graph class work..."""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)  # changed start to end
        if bidirectional:
            self.vertices[end].add(start)  # changed end to start

    def dfs(self, start, target=None):  # variable names made more descriptive
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop()
            if current == target:
                break
            visited.update(self.vertices[current])
            stack.extend(self.vertices[current] - visited)

        return visited

    def graph_rec(self, start, target=None):  # made variable names more descriptive
        visited = set()
        visited.append(start)
        for vertex in self.vertices[start]:
            self.graph_rec(vertex)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:  # added 'not'
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
