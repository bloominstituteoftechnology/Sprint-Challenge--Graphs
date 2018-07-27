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
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(start)

    def depth_first_search(self, start, target=None):
        stack = [start]
        visted = set()

        while stack:
            current = stack.pop()
            if current == target:
                break
            visted.add(current)
            stack.extend(self.vertices[current] - visted)

        return visted

    def graph_rec(self, start, target=None):
        visted = set()
        visted.add(start)
        for v in self.vertices[start]:
            if v not in visted:
                visted.update(self.graph_rec(v, target=target))
        return visted

    # def graph_rec(self, start, target=None):
    #     visted = set()
    #     visted.add(start)
    #     vertices = self.vertices
    #     def search(start, target=None):
    #         for v in vertices[start]:
    #             if v not in visted:
    #                 visted.add(v)
    #                 if v == target:
    #                     break
    #                 search(v, target)
    #         print(visted)
    #     search(start, target)
    #     return visted


    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.graph_rec(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
