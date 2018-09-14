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

    def add_vertex(self, vertex): #removed edges from method parameters
        self.vertices[vertex] = set() #initialized set without edges

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end) #start and end variables updated
        if bidirectional:
            self.vertices[end].add(start) #start and end variables updated

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

test = Graph()
test.add_vertex(4)
test.add_vertex(6)
test.add_vertex(8)
test.add_vertex(10)
# test.add_edge(4,6, bidirectional=False) #unidirectional edge
# test.add_edge(4, 8, bidirectional=True)  # bbidirectional edge
print(test.vertices)
