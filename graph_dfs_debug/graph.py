"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1): #idk what component =-1 is doing but seems fishy
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
        #changed start to end for add to make connection
        self.vertices[start].add(end)
        if bidirectional:
            #changed end to start for add to make connection
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        x = []
        x.append(start)
        y = set(x)

        while x:
            z = x.pop()
            # was checking for x(whole array) instead of z (current).
            if z == target:
                break
            #added z which is the current vertex to the y which is used to check current
            y.add(z)
            #added a minus y to your vertices so it doesn't return everything
            x.extend(self.vertices[z] - y)

        return x

    def graph_rec(self, start, target=None):
        x = set()
        #add instead of append here as it's a set
        x.add(start)
        for v in self.vertices[start]:
            #Seems like a recurisve method but it wasn't recognizing graph_rec. 
            #I made it self.graph_rec. idk if that fixes because idk what this does
            self.graph_rec(v)
        return x

    def find_components(self): # Bet there are problems here
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            #added the vertex's into visited. idk if that's 
            # what I need to do. if not I don't believe the loop
            # runs. Most likely not the right idea but something is up 
            # in this loop not making the right connections
            visited.add(vertex)
            if vertex in visited:
                reachable = self.dfs(vertex)   
                for other_vertex in reachable:
                    other_vertex.component = visited
                current_component += 1
                visited.update(reachable)
        print(current_component)
        # print(reachable)
        self.components = current_component
