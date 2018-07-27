"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    """Vertex needs a label and optionally a connected component"""
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    """This Graph will use a dict to store verts, edges"""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        """Add a vertex, edges optional"""
        if vertex in self.vertices:
            raise Exception('Error: vertex exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: no edge possible if both vertices don\'t exist')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge, needs 2 verts, defaults to bidirectional"""
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    # def dfs(self, start, target=None):
    #     x = [] 
    #     x.append(start)
    #     y = set(x)

    #     while x:
    #         z = x.pop()
    #         if x == target:
    #             break
    #         x.extend(self.vertices[z])

    #     return y

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.add(start)
    #     for v in self.vertices[start]:
    #         x.add(graph_rec(v, target))
    #     return x

    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS."""
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)

        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
