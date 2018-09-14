"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1, color='white'):
        self.label = str(label)
        self.component = component
        self.color = color
        self.edges = set()

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)
        else:
            IndexError('This vertex already exists')

    def add_edge(self, start, end, bidirectional=True):
        if start in self.vertices and end in self.vertices:
            if bidirectional:
                self.vertices[start].edges.add(end)
                self.vertices[end].edges.add(start)
            else:
                self.vertices[start].edges.add(end)
        else:
            IndexError('Both ends of an edge must be in the list of vertices')

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
