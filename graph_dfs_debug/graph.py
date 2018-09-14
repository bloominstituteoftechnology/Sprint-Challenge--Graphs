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
        self.vertices[start].add(end) # directions of each edge has to be opposite. edges should show up now
        if bidirectional:
            self.vertices[end].add(start) # directions of each edge has to be opposite. edges should show up now

    def dfs(self, start, target=None): # changed 'stack == target' to 'current == target'
        stack = [] # renamed to stack to be more desciptive
        stack.append(start) 
        visited = set() # renamed to visited to be more desciptive

        while stack:
            current = stack.pop() # renamed to current to be more desciptive
            visited.add(current) # current added to visited
            if stack == target:
                break
            stack.extend(self.vertices[current] - visited) # remove visited from the stack at the end

        return visited

    def graph_rec(self, start, target=None):
        visited = set() # renamed variable to visited to be more clear
        visited.add(start)
        for vertex in self.vertices[start]: # rename for loop to be more clear
            self.graph_rec(vertex)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited: # change the condition to say if not which will now display random colors when not connected
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
