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
        stack = []  # stack
        stack.append(start)
        visited = set(stack)  # visited

        while stack:
            current = stack.pop()  # current
            if current == target:
                break

            visited.add(current)
            stack.extend(self.vertices[current] - visited)

        return visited

    def graph_rec(self, start, visited=set(), target=None):
        visited.add(start)
        for vertex in self.vertices[start]:
            if vertex not in visited:
                self.graph_rec(vertex, visited)
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
