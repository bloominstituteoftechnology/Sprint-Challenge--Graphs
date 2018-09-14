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
        stack = [start]
        visited = set()

        while stack:
            vertex = stack.pop()
            if vertex == target:
                return True
            visited.add(vertex)
            stack.extend(self.vertices[vertex] - visited)

        return visited

    def dfs_recursive(self, start, visited=None, target=None):
        if visited == None:
            visited = []
        visited.append(start)
        if start == target:
            return True
        for child in self.vertices[start]:
            if child not in visited:
                self.dfs_recursive(child, visited)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs_recursive(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
