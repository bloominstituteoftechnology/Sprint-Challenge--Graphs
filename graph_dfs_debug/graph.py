"""
Simple graph implementation compatible with BokehGraph class.
"""

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Vertex:
    def __init__(self, label, x=None, y=None):
        self.label = label
        self.edges = set()

        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x

        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    def __repr__(self):
        return f"{self.edges}" 

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        self.vertices[label] = Vertex(label)

    def add_edge(self, start, end, bidirectional=True):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].edges.add(end) 
            if bidirectional:
                self.vertices[end].edges.add(start)

    def dfs(self, start, target=None):
        visited = []

        s = Stack()

        s.push(start)

        while s.size() > 0:
            destacked = s.pop()

            if destacked not in visited:
                visited.append(destacked)
                print(destacked)

                if destacked == target:
                    return True

                for edge in self.vertices[destacked].edges:
                    s.push(edge)

        return False

    def graph_rec(self, start, target=None):
        x = set()
        x.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return x

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
