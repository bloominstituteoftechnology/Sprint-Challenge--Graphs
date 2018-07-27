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

    # Fixed this
    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    # Fixed this
    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop() # Pops the last one

            # Fixed this
            # Check of target is found
            if current == target:
                return target

            # Add the current to the stack
            visited.add(current)

            # Added this code: subtract what's visited from the vertices and what's remaining, add it to the stack
            stack.extend(self.vertices[current] - visited)

        return visited

    # Added this method
    def dfs_recursive(self, start, target=None):
        def dfs_helper(vertex, visited):
            # TODO recursion
            visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor, visited)
            return visited

        return dfs_helper(start, set())

    def find_components(self):
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
