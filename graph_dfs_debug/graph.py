"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('ERROR: This Vertex Already Exisits')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        q = [start]
        index = -1
        visited = set()

        while q:
            current = q.pop(index)
            print("current: ", current)
            if current == target:
                break
            visited.add(current)
            print("visited: ", visited)
            q.extend(self.vertices[current] - visited)
            print("queue: ", q)
        
        return visited

    def _recurs_helper(self, start, visited):
        visited[start] = True

        for other_verts in self.vertices[start]:
            if visited[other_verts] = False
                self._recurs_helper(other_verts, visited)

    def graph_rec(self, start):
        visited = [False] * (len(self.vertices))
        self._recurs_helper(start, visted)

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
