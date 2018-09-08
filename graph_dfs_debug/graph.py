"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    # so why is component default value -1?
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

v = Vertex("me")
print(v.component)
print(v.label)
print(v)

    #Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        # so again graph is just a dictionary of sets
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[Vertex(vertex)] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(Vertex(end))
        if bidirectional:
            self.vertices[start].add(Vertex(end))

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



my_graph = Graph()
my_graph.add_vertex('Smurf')
# my_graph.add_edge('Smurf', 'Gizmo')

print(my_graph.vertices)
for key in my_graph.vertices.keys():
    print(type(key))
