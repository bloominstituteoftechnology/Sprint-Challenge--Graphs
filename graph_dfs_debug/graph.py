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

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set()

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                if stack == target:
                    break
                stack.extend(self.vertices[current] - visited)

        return visited

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x

    # def find_components(self):
    #     visited = set()
    #     current_component = 0

    #     for vertex in self.vertices:
    #         if vertex in visited:
    #             reachable = self.dfs(vertex)
    #             for other_vertex in reachable:
    #                 other_vertex.component = current_component
    #             current_component += 1
    #             visited.update(reachable)
    #     self.components = current_component


_graph = Graph()  # Instantiate your graph
_graph.add_vertex('0')
_graph.add_vertex('1')
_graph.add_vertex('2')
# _graph.add_vertex('3')
_graph.add_vertex(3)
_graph.add_vertex('4')
_graph.add_vertex('5')
_graph.add_vertex('6')
_graph.add_vertex('7')
_graph.add_edge('0', '1')
_graph.add_edge('0', '3')
# _graph.add_edge('0', 9)
print('\nGraph vertices: ', _graph.vertices)
# _graph.dfs()
# print('\nConnected components', _graph.connected_components)
# print('\nVertex 3 in graph:', _graph.dfs(3))
# print('\nVertex 100 in graph:', _graph.dfs(100))
# _graph.add_edge('0', '4')
