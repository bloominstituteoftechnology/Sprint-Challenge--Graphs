"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1, color ='gray'):
        self.label = str(label)
        self.component = component
        self.color = color

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex not in self.vertices: #if there are vertex is not in verticies
            self.vertices[vertex] = set(edges) #put the vertex in the vertices and set the edges
        else:
            IndexError("error")

    def add_edge(self, start, end, bidirectional=True):
        if start in self.vertices and end in self.vertices: #if start of a vertex is in vertices and the end is as well then connect them
            #do both end of the vertice, this is where bidirectional will come in.
            #add the ends to each other start-end end-start
            self.vertices[start].add(end) #change the start to end
        if bidirectional:
            self.vertices[end].add(start) #change the end to start
        else:
            IndexError("error")

    def dfs(self, start, target=None):
        visited = []    # create a empty visited dictionary
        stack = [start] # create a stack dictionary where start is placed
        while len(stack) > 0: # while stack is still holding start loop through it
            # pop off each off the elements
            destacked = stack.pop()
            #check to see if any of the destacked elements have been visited
            #and if any of the destacked elements are the target.

            if destacked not in visited:
                if destacked == target:
                    break
                    # place all of the destacked elements into the visited dictionary
                visited.append(destacked)
       

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
