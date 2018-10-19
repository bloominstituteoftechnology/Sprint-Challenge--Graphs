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
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)

    # maybe just redoing this whole thing with recursion would be better
    # looking at the connected components method it seems like the vertex being
    # the input
    # and it looks for verticed to parse, not boleans
    # so I think I need to swtich to a stack like it was before.
    def dfs(self, start, target=None, visited=None):
        x = []
        x. append(start)
        y = set()
        while x:
            z = x.pop()
            if z == target:
                break
            x.extend(self.vertices[z])
        return y

    def graph_rec(self, start, target=None):
        visited = set()
        visited.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return visited

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
        one = Vertex(1)
        graph.add_vertex(one)

        print('hell', self.vertices)
