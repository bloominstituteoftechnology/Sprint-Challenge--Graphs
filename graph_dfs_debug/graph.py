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
        visited = []
        stack = [start]
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                if current == target:
                    break
                visited.append(current)
                for next_vert in self.vertices[current]:
                    stack.append(next_vert)
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

    def graph_rec(self, start, target=None, visited=[]):
        x = set()
        x.add(start)
        for v in self.vertices[start]:
           se;f.graph_rec(v)
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
