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
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)

    def dfs(self, start, target=None):
        #x = [] changet to stack=[]
        stack=[start]
        #x.append(start)
        #y = set(x) changed to visited=set()
        visited=set()

        #while x: changed to while stack:
        while stack:
            #z = x.pop() changed to current = stack.pop()
            current = stack.pop()
            #if x == target: changet to if current == target:
            if current == target:
                break
            # added visited.add(current)
            visited.add(current)
            #x.extend(self.vertices[z]) changed to visited.add(current) changed to the following line
            stack.extend(self.vertices[current] - visited)
            

        #return x changed to return visited
        return visited

    def graph_rec(self, start, target=None):
        x = set()
        #x.append(start) append does not work on a set so I changed it to x.add(start)
        x.add(start)
        for v in self.vertices[start]:
            #graph_rec(v) changed to self.graph_rec(v)
            self.graph_rec(v)
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
