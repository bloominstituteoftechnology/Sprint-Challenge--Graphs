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
#         self.vertices[start].add(start)
        self.vertices[start].add(end)
        if bidirectional:
#             self.vertices[end].add(end)
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        queue = [start]
        visited = set()
        
        while queue:
            node = queue.pop()
            visited.add(node)
            if node == target:
                break
            for n in self.vertices(node):
                if (n not in queue) and (n not in visited):
                    queue.extend(self.vertices(node))
            
        return visited
    
#     def dfs(self, start, target=None):
#         x = []
#         x.append(start)
#         y = set(x)

#         while x:
#             z = x.pop()
#             if x == target:
#                 break
#             x.extend(self.vertices[z])

#         return x

    visited = set([])
    
    def graph_rec(self, start, visited = visited, target=None):
        visited.add(start)
        for n in self.vertices[start]:
            if n not in visited:
                visited.add(n)
                self.graph_rec(n, visited = visited)
        return visited
    
    
#     def graph_rec(self, start, target=None):     
#         x = set()
#         x.append(start)
#         for v in self.vertices[start]:
#             graph_rec(v)
#         return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            visited.add(vertex)
            if vertex in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
