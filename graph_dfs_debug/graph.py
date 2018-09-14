"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = label
        self.component = component
        self.edges = set()

    #def __repr__(self):
        #return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].edges.add(end)
        if bidirectional:
            self.vertices[end].edges.add(start)

    def dfs(self, start, target=None):
        #print(start.label)
        x = []
        x.append(start)
        #y = set(x)
        visited = []
        while len(x) > 0:
            z = x.pop()
            print(z.label)
            visited.append(z)
            print(target)
            if str(self.vertices[z].label) == target:
                print(True)
                break
            for child in self.vertices[z].edges:
                #print(child.label)
                if child not in visited:
                    x.append(child)
            #x.extend(self.vertices[z])
        print(False)
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
                reachable = self.dft(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

    def dft(self, node, visited=[]):
        print(node)
        visited.append(node)
        for child_node in self.vertices[node].edges:
            if child_node not in visited:
                self.dft(child_node, visited)
        return visited