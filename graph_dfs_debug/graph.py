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
        #lines 22 & 25 changed the start vertices to point to the end and the end to point to the start
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        #Changed variable names to convey to another dev what you were intending to do here. X and Y were vague and easy to misconstrue
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack: #
            stacked = stacked.pop()
            if stacked == target:
                print("Target {} has been found".format(target)) #it didn't make sense to break here so I put a print statement
            stack.extend(self.vertices[stacked])-visited

        return visited #This ensures that the stack will actually work properly as you search

    def dfs_recursive(self, start, target=None): #changed to method name to better inform the next dev what is trying to be accomplished in this line
        visited = set()
        visited.add(start) #because visited is a set you want to add not append
        for v in self.vertices[start]:
            self.dfs_recursive(v) #In order to call the recursive method we have to use self otherwise lint will yell at you
        return visited

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
