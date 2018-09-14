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

    def add_vertex(self, vertex): #removed edges from method parameters
        self.vertices[vertex] = set() #initialized set without edges

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end) #start and end variables updated
        if bidirectional:
            self.vertices[end].add(start) #start and end variables updated

    def dfs(self, start, target=None, visited = []): #added visited list parameter to replace x
        visited.append(start)
        current = visited.pop()
        if target == None:
          raise Exception('You must provide a start and target value') #added exception handling if values not supplied
        if current == target:
            return True  # return true if target found
        for child_node in self.vertices[start]: #added loop to check for child nodes from start node
          if child_node not in visited: # check each child node to see if we have looked at it yet. if not, run recursion
            if self.dfs(child_node, target, visited): #run recursion on child
              return True #if found return true
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


#testing, testing, can you hear me?
test = Graph()
test.add_vertex(4)
test.add_vertex(6)
test.add_vertex(8)
test.add_vertex(10)
test.add_edge(4,6, bidirectional=False) #unidirectional edge
test.add_edge(4,8, bidirectional=False)  # bidirectional edge
test.add_edge(8,10, bidirectional=False)  # bidirectional edge
print(test.dfs(4, 8))
