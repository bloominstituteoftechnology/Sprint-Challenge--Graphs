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
        self.vertices[start].add(end)
        start.component += 1
        if bidirectional:
            self.vertices[end].add(start)
            end.component += 1

    def dfs(self, start, target=None):
        # x = []
        # x.append(start)
        # y = set(x)
        stack = [start]
        visited = set(stack)

        while stack:
            curr = stack.pop()
            if curr == target:
                break
            visited.add(curr)
            stack.extend(self.vertices[curr] - visited)
        return visited

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.add(start)
    #     for v in self.vertices[start]:
    #         self.graph_rec(v)
    #     return x

    def dfs_rec(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for other_vertex in self.vertices[start]:
            if other_vertex not in visited:
                self.dfs_rec(other_vertex, visited)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs_rec(vertex)  # change to dfs_rec
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

