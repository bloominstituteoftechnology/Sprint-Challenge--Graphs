"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return self.label


"""Trying to make this Graph class work..."""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = []

    def add_vertex(self, vertex, edges=()):
        self.vertices[str(vertex)] = set(edges)

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

    def get_components(self):
        connected_components = []
        visited_nodes = set()

        for vertex in self.vertices.keys():
            if vertex not in visited_nodes:  # if fvertex no visited.
                response = self.dfs(vertex, None, visited_nodes)
                connected_components.append(response)
        self.components = connected_components

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x
