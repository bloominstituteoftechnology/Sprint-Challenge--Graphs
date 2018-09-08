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
        if start not in self.vertices and end not in self.vertices:
            raise ValueError("No Entries.")

        self.vertices[start].add(end) # start and start? its start node to end node to create the vertex
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):

        # DFS works with stacks

        stack = [start] # the stack

        visited = set() # visited node

        while stack:
            current = stack.pop() # why a z?
            if current == target:
                break
            visited.add(current)
            stack.extend(self.vertices[current])

        return visited

    def graph_rec(self, start, target=None):
        x = set()
        visited.append(start)
        for v in self.vertices[start]:
            self.graph_rec(v)
        return visited

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
