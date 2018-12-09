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
        stack = []
        stack.append(start)
        visited = set() 
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                if current == target:
                    return True
                stack.extend(list(self.vertices[current]))
        return visited
# diff implementation
        # touched = []
        # stack = [start]
        # while len(stack) > 0:
        #     current = stack.pop()
        #     if current not in touched:
        #         if current == target:
        #             break
        #         touched.append(current)
        #         for newVert in self.vertices[current]:
        #             stack.append(newVert)
        #     return touched

    def graph_rec(self, start, target=None):
        x = set()
        x.add(start)
        for v in self.vertices[start]:
            self.graph_rec(v)
        return x

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
