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
      self.vertices[start].add(end) #start to end
      if bidirectional:
         self.vertices[end].add(start) #end to start

    def dfs(self, start, target=None):
        x = []
        y = set(x)
        x.append(start)
        while x:
          z = x.pop()
          if z == target:
            break
          y.add(z) # add x to 
          x.extend(self.vertices[z]-y)
        return y

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
            if vertex not in visited: # not in
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
