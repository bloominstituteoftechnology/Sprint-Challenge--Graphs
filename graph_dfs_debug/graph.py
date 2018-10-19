"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label) #id
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
        x = [] # this is the stack
        x.append(start)
        y = set(x) #unused variable - questionable 

        while x:
            z = x.pop() # takes off the back that would be for a stack - good 
            if x == target: # should most likely be z --change
                break
            x.extend(self.vertices[z]) #extend just flattens the list - good
        print('x - dfs -> ', x)
        print('y - dfs -> ', y)
        return x # this would return the path? 

    def graph_rec(self, start, target=None):
        x = set()
        x.append(start) # should be add? 
        for v in self.vertices[start]:
            graph_rec(v)
        return x # not returning anything from for loop

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices: #checks all the vertex
            if vertex in visited: #if they are also in visited
                reachable = self.dfs(vertex) #should return a traversal? -- wrong or dfs is wrong
                for other_vertex in reachable: # for all nodes connected to the vertex and in visited (which is empty) 
                    other_vertex.component = current_component # that component is now zero
                current_component += 1
                visited.update(reachable)
        self.components = current_component

                #searches through all vertexs in visited(which is set to 0) and assigns other_ertex to the current component which is 0. then sets self.components to the last component

                #______all components are labeled -1 by default so this assignes labels_____________