"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vert_label, component=-1):
        self.vert_label = vert_label
        self.component = component
        self.edges = set()

    def __repr__(self):
        return ' {}'.format(self.edges)

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex_label):
        self.vertices[vertex_label] = Vertex(vertex_label)

    def add_edge(self, vert1, vert2, bidirectional=True):
        if vert1 in self.vertices and vert2 in self.vertices:
            self.vertices[vert1].edges.add(vert2)
        if bidirectional:
            self.vertices[vert2].edges.add(vert1)

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

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1', True)
# graph.add_edge('0', '3', True)
# print(graph.vertices)