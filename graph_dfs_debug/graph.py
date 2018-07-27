"""
adding comment to make pull request
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

    def add_vertex(self, vertex, edges=()): """Add a new vertex, optionally with edges to other vertices."""
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True): """Add a edge (default bidirectional) between two vertices."""
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None): """Search the graph using BFS or DFS."""
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop() # pops the last one 
            if current == target: # check if found target
                return target
            visited.add(current) # add the current to the stack
            stack.extend(self.vertices[current] - visited) # subtract whats visited from the vertices and whats remaining, add it to the stack

        return visited

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x
        def bfs(self, start, target=None):
        """Search the graph using BFS or DFS."""
        queue = []
        queue.append(start)
        visited = set(queue)
        
        while queue:
            current = queue.pop(0)  # pops the first one

            # check if found target
            if current == target:
                return target

            # add the current to the stack
            visited.add(current)

            # subtract whats visited from the vertices and whats remaining, add it to the stack
            queue.extend(self.vertices[current] - visited)

        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            # because you have been here so, you don't want to repeat
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
