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
        """Add an edge between two vertices"""
        # start need to add end and vice versa for didirectional
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        """Using dfs to search"""
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop()
            if current == target:
                break
            # need to add the current one to the stack
            visited.add(current)
            # need to subtract the visted one from the vertices and extend the remaining to the stack
            visited.extend(self.vertices[current] - visited)

        return visited

    def graph_rec(self, start, target=None):
        visited = set()
        # change from append to add
        visited.add(start)
        for vertex in self.vertices[start]:
            # add self in front of the method as it's invoked inside the class.
            self.graph_rec(vertex)
        return visited

    def find_components(self):
        """Identify components and update vertex component ids"""
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            # add `not`
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
