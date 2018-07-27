"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """
    Represent a vertex with a label and component.
    This component attribute is a number attributed to a given connected component
    The possession of a number indicates inclusion in the connection
    """

    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return "Vertex: " + self.label


class Graph:
    """Represent a graph as a dictionary of vertices"""

    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception("Error: Duplicate vertex.")
        if not isinstance(vertex, Vertex):
            raise Exception("Error: Not an instance of the Vertex class")
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error: Cannot connect to a nonexistent vertex.")
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
                return target
            visited.add(current)
            stack.extend(self.vertices[current] - visited)

        return visited

    def graph_rec(self, start, visited=None, target=None):
        if visited is None:
            visited = set()
        visited.add(start)
        if start == target:
            return target
        for edge in self.vertices[start] - visited:
            self.graph_rec(edge, visited)
        return visited

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
