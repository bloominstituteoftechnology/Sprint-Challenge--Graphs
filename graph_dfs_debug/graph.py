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
        stack = [start]
        visited = set()

        while stack:
            current = stack.pop()
            visited.add(current)
            if current not in visited:
                if current == target:
                    break      # return visited
                visited.append(current)
                for next_el in self.vertices[current]:
                    stack.push(next_el)
        return visited

    # def graph_rec(self, start, target=None, visited=[]):
    #     if visited is None:
    #         visited = []
    #     visited.append(start)
    #     for next_el in self.vertices[start]:
    #         if next_el not in visited:
    #             self.graph_rec(next_el, target, visited)
    #     return visited

    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x

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
