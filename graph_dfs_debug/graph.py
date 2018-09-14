"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vertex_id, component=-1, value=None):
        self.id = int(vertex_id)
        self.label = str(vertex_id)
        self.component = component
        self.value = value
        self.edges = set() 
        if self.value is None:
            self.value = self.id

    def __repr__(self):
        return self.label

    """Trying to make this Graph class work..."""
    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].edges.add(end)
        if bidirectional:
            self.vertices[end].edges.add(start)

    def dfs(self, initial_vert, target_value, visited=[], path=[]):
        visited.append(initial_vert)
        path = path + [initial_vert]
        if self.vertices[initial_vert].value == target_value:
            return path
        for child_vert in self.vertices[initial_vert].edges:
            if child_vert not in visited:
                new_path = self.dfs(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

    # def dfs(self, node_id, search_node, visited=[]):
    #     if node_id == search_node:
    #         return True
    #     visited.append(node_id)

    #     for child_node in self.vertices[node_id].edges:
    #         if child_node not in visited:
    #             new_path = self.dfs_path(child_vert, target)
    #             self.dfs(self, child_node, search_node, visited)
    #     return False

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
            if vertex in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
