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
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop()
            visited.add(current)
            if current == target:
                return current
            stack.extend(self.vertices[current] - visited)
        return visited
        # x = []
        # x.append(start)
        # y = set(x)

        # while x:
        #     z = x.pop()
        #     if x == target:
        #         break
        #     x.extend(self.vertices[z])

        # return x

    def graph_rec(self, start, target=None, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        if start == target:
            return True
        for node in self.vertices[start]:
            if node not in visited:
                if self.graph_rec(node, target, visited):
                    return True
        return False
        # x = set()
        # x.append(start)
        # for v in self.vertices[start]:
        #     graph_rec(v)
        # return x

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
