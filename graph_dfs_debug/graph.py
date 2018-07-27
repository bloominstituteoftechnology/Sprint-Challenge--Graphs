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
        #error - edge has to be connected with a different Vertex no the same one
        # start connects with end
        # self.vertices[start].add(start)
        self.vertices[start].add(end)
        #error - edge has to be connected with a different Vertex no the same one
        # end connects with start if is bidirectional
        # if bidirectional:
        #     self.vertices[end].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        x = []
        x.append(start)
        #error - unused vaiable y, and set with initial value of x, should be empty
        # y = set(x)
        y = set()
        while x:
            z = x.pop()
            #error - x is a list of vertices, should be the current vertex to compare with the target
            # if x == target:
            if z == target:
                break
            #error - we have to add to y the visited Vertex(z)
            y.add(z)
            #error - we add to the x queue all the vertices connected with this current vertex z excludind the ones already visited
            # x.extend(self.vertices[z])            
            x.extend(self.vertices[z]- y)

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
