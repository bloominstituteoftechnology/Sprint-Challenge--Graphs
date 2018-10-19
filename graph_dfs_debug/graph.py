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
        self.vertices[str(vertex)] = set(edges)

    # def add_edge(self, start, end, bidirectional=True):
    #     self.vertices[start].add(start)
    #     if bidirectional:
    #         self.vertices[end].add(end)
"""
Added validations and better varaible names
"""
    def add_edge(self, start_vertex, end_vertex, bidirectional=True):
        keys = self.vertices.keys()
        if (str(start_vertex) not in keys) and (str(end_vertex) not in keys):
            raise Exception('The vertex are not in the Graph')
        elif str(start_vertex) not in keys:
            raise Exception(
                f'''The vertex {start_vertex} is not in the Graph.''')
        elif str(end_vertex) not in keys:
            raise Exception(
                f'''The vertex {end_vertex} is not in the Graph.''')
        else:
            self.vertices[str(start_vertex)].add(str(end_vertex))
            if bidirectional:
                self.vertices[str(end_vertex)].add(str(start_vertex))

    # def dfs(self, start, target=None):
    #     x = []
    #     x.append(start)
    #     y = set(x)

    #     while x:
    #         z = x.pop()
    #         if x == target:
    #             break
    #         x.extend(self.vertices[z])

        # return x
"""
Looks like a simple stack being tried(non-class), changed names to ake more readable
"""
    def dfs(self, start=None, target=None, visited=None):
        stack = []
        stack.append(start if start is not None else '0')
        visited = visited if visited is not None else set()
        component = set()

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.add(current)
                if current == str(target):
                    break
                stack.extend(self.vertices[current] - visited)
        return component
"""
Just re-write the recursion to con fusing to follow at all
"""
    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x

    def get_components(self, method='dfs'):
        connected_components = []
        visited_nodes = set()

        for vertex in self.vertices.keys():
            if vertex not in visited_nodes:  # if fvertex no visited.
                response = self.dfs(vertex, None, visited_nodes) if method is 'dfs' else self.dfs_recursive(
                    vertex, None, visited_nodes)
                connected_components.append(response)
        self.components = connected_components

    # def find_components(self):
    #     visited = set()
    #     current_component = 0

    def dfs_recursive(
        self, start=None, target=None, visited=None, component=None
    ):
        start = start if start is not None else '0'
        visited = visited if visited is not None else set()
        visited.add(str(start))
        component = component if component is not None else set()
        component.add(start)
        # print(start)


        # for vertex in self.vertices:
        #     if vertex in visited:
        #         reachable = self.dfs(vertex)
        #         for other_vertex in reachable:
        #             other_vertex.component = current_component
        #         current_component += 1
        #         visited.update(reachable)
        # self.components = current_component

        for vertex in self.vertices[str(start)]:
            if vertex not in visited:
                self.dfs_recursive(vertex, None, visited, component)

        return component
