"""
Simple graph implementation compatible with BokehGraph class
"""

# Stack
class Stack:
  def __init__(self):
    self.size = 0
    self.storage = []
  
  def last_in(self, value):
    self.storage.append(value)
    self.size += 1

  def first_out(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop()


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

    def dfs(self, starting_node, target_node=None):
        stack = Stack()
        stack.last_in(starting_node)
        visited = []
        while stack.size > 0:
            current_node = stack.first_out()
            visited.append(current_node)
            if current_node == target_node:
                return True
            for edge in self.vertices[current_node]:
                if edge not in visited:
                    stack.last_in(edge)
        return False

    def graph_rec(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for vert in self.vertices[start]:
            if vert not in visited:
                self.graph_rec(vert)
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
