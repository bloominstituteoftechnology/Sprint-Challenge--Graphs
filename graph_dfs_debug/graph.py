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
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

# our vertices were not connecting (see answers.md) we connect start to end , end to start to see edges
    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Connecting Vertices not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

# make this more readable for the team.  changed x = stack, y = visited (vertex), z = current (vertex)
    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop()
            if current == target:
                break
            stack.extend(self.vertices[current] - visited)

        return visited
# we make our recursive graph function more readable as well. we will change x to be our visited (vertices) to be able to connect your visited vertices.

    def graph_rec(self, start, target=None):
        visited = set()
        #changed append to add as append doesnt work in this instance.
        visited.add(start)
        for vertex in self.vertices[start]:
            if vertex not in visited:
                visited.update(self.graph_rec(vertex, target=target))

        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            # we needed to add "not" in if statement below to make sure that our find components function works
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
