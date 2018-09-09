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

    def __repr__(self):
        return str(self.vertices)

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
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.vertices[vertex] - visited) 
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

graph = Graph()
v1 = Vertex('John')
v2 = Vertex('Steve')
v3 = Vertex('Bob')
v4 = Vertex('Jill')
v5 = Vertex('Jane')
graph.add_vertex(v1)
graph.add_vertex(v2)
graph.add_vertex(v3)
graph.add_vertex(v4)
graph.add_vertex(v5)
graph.add_edge(v1,v2)
graph.add_edge(v1,v3)
graph.add_edge(v2,v3)
graph.add_edge(v4,v5)
graph.add_edge(v2,v5)

print(graph)