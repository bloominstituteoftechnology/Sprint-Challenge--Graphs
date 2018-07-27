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
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        to_visit = [start]
        visited = set(to_visit)

        while to_visit:
            current_vertex = to_visit.pop()
            if current_vertex == target:
                break
            to_visit.extend(self.vertices[current_vertex] - visited)
            visited.update(self.vertices[current_vertex])
        
        return visited

    def graph_rec(self, start, target=None):
        to_visit = set()
        to_visit.append(start)
        for vertex in self.vertices[start]:
            self.graph_rec(vertex)
        return to_visit

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
