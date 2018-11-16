
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
        self.label = str(label)
        self.edges = set()
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception("Vertex already added, please add a different one")
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Missing necessary nodes to add edges to")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        visited = []
        stack = Stack()
        stack.push(start)
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                if current == target:
                    break
                visited.append(current)
                for next_vert in self.vertices[current]:
                    stack.push(next_vert)
        return visited
        
        # stack = []
        # stack.append(start)
        # visited = set(stack)

        # while stack:
        #     current = stack.pop()
        #     if stack == target:
        #         break
        #     stack.extend(self.vertices[current])

        # return visited

    def graph_rec(self, start, target=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for other_vertex in self.vertices[start]:
            if other_vertex not in visited:
                self.graph_rec(other_vertex, target, visited)
        return visited


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


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')

# bg=BokehGraph
# bg.show()
print(graph.vertices)
