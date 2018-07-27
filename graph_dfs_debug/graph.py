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
        self.vertices[start].add(end) # value in vertices are the end of the edge
        if bidirectional:
            self.vertices[end].add(start) # bidirection mean from end to start

    def dfs(self, start, target=None):
        stack = [] 
        stack.append(start) 
        visited = set() #do not put the start vertex in the set of visited

        while stack:
            current = stack.pop(-1)
            if current == target: # use current element instead of the stack!
                break
            visited.add(current) # keep track of visited vertex
            stack.extend(self.vertices[current] - visited) # need to remove the visited element from the stack

        return visited # return visited instead of the stack which is just internal to the function

    def dfs_recursion(self, start, target=None):#use descriptive name for function
        visited = set()
        visited.add(start) # use add for set
        for vertex in self.vertices[start]:
            visited.add(self.dfs_recursion(vertex))# need self to call class function
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited: # do the ones 'not' visited to make progress
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
