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
        # end and start positions were swapped
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=0):
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop(-1)
            if current.label == str(target): # target should be looking at the current node
                print("\nTarget Found: {}".format(target))
            visited.add(current) # need to add visited nodes to overall set
            stack.extend(self.vertices[current] - visited)

        return visited

    def graph_rec(self, start, visited = set(), target=None):
        visited.add(start) # set has no append method changing to add
        for v in (self.vertices[start]):
            if v not in visited:
               self.graph_rec(v, visited) # needed to call self
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.graph_rec(vertex, visited = set())
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
