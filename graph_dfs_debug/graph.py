"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    """Trying to make this Graph class work..."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        #error - edge has to be connected with a different Vertex no the same one
        # start connects with end
        # self.vertices[start].add(start)
        self.vertices[start].add(end)
        #error - edge has to be connected with a different Vertex no the same one
        # end connects with start if is bidirectional
        # if bidirectional:
        #     self.vertices[end].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        #error - unused variable y, and set with initial value of x, should be empty
        # y = set(x)
        visited_vertices = set()
        while stack:
            current_vertex = stack.pop()
            #error - x is a list of vertices, should be the current vertex to compare with the target
            # if x == target:
            # instead of break should return the vertex 
            # if z == target:
            #     break
            if current_vertex == target:
                return current_vertex
            #error - we have to add to y the visited Vertex(z)
            visited_vertices.add(current_vertex)
            #error - we add to the x stack all the vertices connected with this current vertex z excludind the ones already visited
            # x.extend(self.vertices[z])            
            stack.extend(self.vertices[current_vertex] - visited_vertices)

        # should return the visited vertices
        # return x
        return visited_vertices

    def graph_rec(self, start, target=None):
        x = set()
        #error - x is a set and has not have a append() method, only add() method should be used
        # x.append(start)
        x.add(start)

        #error - graph_rec() is a recursive call to a method inside the same class needs to be called with self
        # for v in self.vertices[start]:
        #     graph_rec(v)
        for v in self.vertices[start]:
            self.graph_rec(v)
        return x

    def dfs_recursive(self, start, target=None):
        visited = set()
        visited.add(start)

        def dfs_helper(curr):
            visited.add(curr)
            for vertex in self.vertices[curr]:
                if vertex not in visited:
                    dfs_helper(vertex)
        dfs_helper(start)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            #error - vertex is reachable if is not visited yet, this will help to track if is a different component and select a color for this component
            # if vertex in visited:
            if vertex not in visited:
                reachable = self.dfs_recursive(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
