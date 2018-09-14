"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = label
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
        print(start)
        visited = []
        stack = []
        stack.append(start)
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                for next_vert in self.vertices[current]:
                    stack.append(next_vert)
        return visited

    def graph_rec(self, start, target=None):
        current_vert = set()
        current_vert.append(start)
        for vertex in self.vertices[start]:
            graph_rec(vertex)
        return current_vert

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

    '''def dft(self, node, visited=[]):
        print(node)
        visited.append(node)
        for child_node in self.vertices[node]:
            if child_node not in visited:
                self.dft(child_node, visited)
        return visited'''

    def dfs_rec(self, start, target=None, visited=[]):
        visited.append(start)
        if start.label == target:
            print(True)
            return True
        for child in self.vertices[start]: 
            if child not in visited:
                self.dfs_rec(child, target, visited)
        print(False)
        return False