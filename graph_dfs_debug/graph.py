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
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set()
        while stack:
            current = stack.pop()
            if current == target:
                break
            stack.extend((i for i in self.vertices[current] if i not in visited))
            visited.add(current)
        return visited

    def graph_rec(self, start, target=None):
        queue = set()
        queue.set(start)
        visited = []
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



# g = Graph()
# one = Vertex(1)
# two = Vertex(2)
# three = Vertex(3)
# four = Vertex(4)
# five = Vertex(5)
# six = Vertex(6)
# seven = Vertex(7)
# eight = Vertex(8)
# nine = Vertex(9)
# g.add_vertex(one)
# g.add_vertex(two)
# g.add_vertex(three)
# g.add_vertex(four)
# g.add_vertex(five)
# g.add_vertex(six)
# g.add_vertex(seven)
# g.add_vertex(eight)
# g.add_vertex(nine)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(2,5)
# g.add_edge(3,6)
# g.add_edge(3,7)

# print('vertices', g.vertices)
# print('dfs', g.dfs(1))
# g.find_components()
# print('components', g.components)