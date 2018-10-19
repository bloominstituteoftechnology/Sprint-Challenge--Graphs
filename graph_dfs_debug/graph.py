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
    def __init__(self, label, component=-1):
        # self.vert_label = vert_label
        self.label = str(label)
        self.component = component
        # self.edges = set()

    def __repr__(self):
        # return ' {}'.format(self.edges)
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, label, edges=()):
        # self.vertices[vertex_label] = Vertex(vertex_label)
        self.vertices[label] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)
        #     self.vertices[vert1].edges.add(vert2)
        # if bidirectional:
        #     self.vertices[vert2].edges.add(vert1)

    def dfs(self, start, target=None):
        s = Stack()
        visited = []
        s.push(start)
        # x.append(start)
        # y = set(x)

        while s.size() > 0:
            curr_vert = s.pop()
            if curr_vert == target:
                return True
            visited.append(curr_vert)
            # x.extend(self.vertices[z])
            for vert in self.vertices[curr_vert].edges:
                if vert not in visited:
                    s.push(vert)

        return False

    def graph_rec(self, start, target=None, visited=None):
        if visited is None:
            visited = []
        # x = set()
        visited.append(start)
        if start == target:
            return True

        for vert in self.vertices[start].edges:
            if vert not in visited:
                if self.graph_rec(vert, target, visited):
                    return True
        return False

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

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1', True)
# graph.add_edge('0', '3', True)
# print(graph.vertices)