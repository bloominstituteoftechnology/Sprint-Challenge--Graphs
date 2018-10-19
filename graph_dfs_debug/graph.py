"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component
        self.edges = set()

    def __repr__(self):
        return f"Vertex: {self.label}, Edges: {self.edges}"

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, start, end, bidirectional=True):
        if end not in self.vertices[start].edges:
            self.vertices[start].edges.add(end)
            if bidirectional:
                self.vertices[end].edges.add(start)

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

    def graph_rec(self, start, target=None, x=[]):
        x = x
        x.append(start)
        if start.edges:
            for edge in start.edges:
                if edge not in x:
                    self.graph_rec(self.vertices[edge], x)
            return self.answer

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

test = Graph()
test.add_vertex(0)
test.add_vertex(1)
test.add_vertex(2)
test.add_edge(0, 1)
test.add_edge(1, 2, False)
test.add_edge(2, 0, False)
print()