import warnings

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """Vertex class includes a label (automatically cast to a string) and a component attribute."""
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        """Represents each vertex using its label"""
        return 'Vertex: ' + self.label


class Graph:
    """Graph class that uses a dictionary of the vertices as keys with values are the end vertices of edges associated with the key"""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        """Add a vertex that doesn't exist or overwrite a vertex that does"""
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: one or more edges points to a vertx not in graph.')
            self.vertices[vertex] = set(edges)
        if vertex in self.vertices:
            warnings.warn('Warning: vertex already existed. Previous edges have been overwritten.')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge between existing vertices"""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error: One or more specified vertices are not in the graph.')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        """Depth first search of the graph using looping method"""
        stack = [start]
        visited = set()

        while stack:
            current = stack.pop()
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            stack.extend(self.vertices[current] - visited)

        return visited
  
    def dfs_recursive(self, start, target=None, visited=[]):
        """dfs of graph using recursion"""
        visited.append(start)
        if start.label == target:
            return visited
        for neighbor in self.vertices[start]:
            if neighbor not in visited:
                visited = self.dfs_recursive(neighbor, target=target, visited=visited)

        return visited
    
    def find_components(self):
        """Identify components of graph and update the component value of each vertex"""
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
