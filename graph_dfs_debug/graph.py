"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = label
        self.component = component
        self.edges = set()

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].edges.add(end)
        if bidirectional:
            self.vertices[end].edges.add(start)

    def dfs(self, start, target):  
        # Uses self.vertices indexes (which are the same as each vertex's label) to find if value in graph
        stack = []
        stack.append(start)
        visited = []

        while stack:
            current = stack.pop()
            visited.append(current)
            if current == target:
                return True
            for child in self.vertices[current].edges:
                if child not in visited:
                    stack.append(child)

        return False

    def dfs_recursive(self, start, target=None, visited=[]):
        visited.append(start)
        if self.vertices[start].label == target:
            return True
        for child in self.vertices[start].edges:
            if child not in visited:
                return self.dfs_recursive(child, target, visited)
        return False

    def dft_stack(self, starting_vertex_id):
        stack = []
        stack.append(starting_vertex_id)
        visited = []
        while len(stack) > 0:
            v = stack.pop()
            if v not in visited:
                visited.append(v) 
                for next_vert in self.vertices[v].edges:
                    stack.append(next_vert)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:                  # Changed to not in (we want to perform this operation on vertices we HAVENT visited)
                reachable = self.dft_stack(vertex)
                for other_vertex in reachable:
                    self.vertices[other_vertex].component = current_component   # 
                current_component += 1
                visited.update(reachable)
        self.components = current_component


