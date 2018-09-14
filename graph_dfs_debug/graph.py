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
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[start].add(end)
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        x = []
        x.append(start)
        y = set(x)

        while len(x) > 0:
            z = x.pop()
            if z == target:
                print(f'Visited: {y}')
                return True 
            # x.extend(self.vertices[z])
            for e in self.vertices[z]:
                x.append(e)
                y.add(e)
            x.pop()

        print(f'Visited: {y}')
        return False 

    def graph_rec(self, start, target=None, y=set()):
        # x = set() 
        x = []
        x.append(start)
        y.add(start)

        while len(x) > 0:
            z = x.pop()
            if z == target:
                print(f'Visited: {y}')
                return True 
            for v in self.vertices[z]:
                self.graph_rec(v, target, y)
            x.pop()

        print(f'Visited: {y}')
        return False 

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

g = Graph()
g.add_vertex('0', ('1','3'))
g.add_vertex('1', ('0'))
g.add_vertex('2')
g.add_vertex('3', ('0'))
# print(g.vertices)
# print(g.components)
# print(g.dfs('0', '1'))
# print(g.dfs('0', '2'))
# g.graph_rec('0', '1')
