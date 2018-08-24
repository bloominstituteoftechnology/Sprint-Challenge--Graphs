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
        ''' adds vertex '''
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        '''adds edges '''
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        ''' iterative depth first search method '''
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            visiting = stack.pop()
            if visiting == target:
                print("Target {} has been found".format(target))
            stack.extend(self.vertices[visiting])-visited

        return visited

    def dfs_recursion(self, start, visited=None, target=None):
        ''' recursive depth first search method '''
        visited = visited or set()
        visited.add(start)
        for v in self.vertices[start]:
            if v not in visited:
                self.dfs_recursion(v)
                visited.add(v)
        return visited

    def find_components(self):
        ''' find contiguous components '''
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                reachable = self.dfs_recursion(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
