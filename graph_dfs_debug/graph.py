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
        # Add a new vertex, optionally with edges to other vertices.
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exist.')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        # Add a edge (default bidirectional) between two vertices
        if start not in self.vertices:
            raise Exception('Error: The start vertice is not in the graph.')
        elif end not in self.vertices:
            raise Exception('Error: The end vertice is not in the graph.')

        self.vertices[start].add(end)

        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method='dfs'):
        queue_stack = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while queue_stack:
            current_vertex = queue_stack.pop(pop_index)
            if current_vertex == target:
                break
            visited.add(current_vertex)
            # Add possible (unvisited) vertices to queue
            queue_stack.extend(self.vertices[current_vertex] - visited)

        return visited

    def graph_rec(self, start, target=None):
        x = set()
        x.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
