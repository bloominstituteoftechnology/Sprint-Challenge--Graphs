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
        self.vertices[start].add(end)       #changed add(start) to add(end) 
        if bidirectional:
            self.vertices[end].add(start)    #changed add(end) to add(start)

    def dfs(self, start, target=None):
        x = []
        x.append(start)
        y = set(x)        #visited item set

        while x:
            z = x.pop()
            if x == target:
                break
            x.extend((edge for edge in self.vertices[z] if edge not in y))   #using comprehension set
            y.add(z)   #add item to visited
        return y

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
            if vertex not in visited:  # added not to check if vertex not presrent in visited
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
