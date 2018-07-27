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
        print('stack', stack)
        visited = visited if visited is not None else set()
        print('visited', visited)
        component = set()

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.add(current)
                if stack == target:
                    break
                stack.extend(self.vertices[current] - visited)

        return component

    def get_components(self):
        connected_components = []
        visited_nodes = set()

        # print(f'''SELF VERTICES {self.vertices.keys()}''')
        for vertex in self.vertices.keys():
            if vertex not in visited_nodes:  # if fvertex no visited.
                # print('\n\nNO PASSED', vertex, '\n')
                response = self.dfs(vertex, None, visited_nodes)
                print(response)
                connected_components.append(response)
        # print('\nconnected_components', connected_components)
        self.components = connected_components

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
print('DFS', _graph.dfs())
_graph.get_components()
print('\nConnected components', _graph.components)
# print('\nVertex 3 in graph:', _graph.dfs(3))
# print('\nVertex 100 in graph:', _graph.dfs(100))
# _graph.add_edge('0', '4')
