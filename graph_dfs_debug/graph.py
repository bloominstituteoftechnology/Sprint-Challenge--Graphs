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
        # was self.vertices[start].add(start)
        self.vertices[start].add(end)
        if bidirectional:
            # was self.vertices[start].add(end)
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        vertices = []
        visited = {}
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited[vertex] = 1
            else:
                continue

            vertices.append(vertex)
            if vertex == target:
                break
            stack.extend(self.vertices[vertex])

        return vertices

    def graph_rec(self, start, target=None, visited={}):
        if start not in visited:
            visited[start] = 1
        if start == target:
            return visited
        
        for next_vertex in self.vertices[start]:
            if next_vertex not in visited:
                self.graph_rec(next_vertex, target, visited)
        return visited

        # boilerplate
        # x = set()
        # x.append(start)
        # for v in self.vertices[start]:
        #     graph_rec(v)
        # return x

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
