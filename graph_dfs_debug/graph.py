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

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        # x = [] no, x named stack not x
        stack = []
        print('vertiecs', self.vertices['0'])
        stack.append(start)
        print('start', start)
        visited = []
        # y = set(x) I have no idea what y = set(x) is but we will declare visited as an empty list
        #notFound = True
        while len(stack) > 0:
            value = stack.pop()
            print('pop', value)

            if value not in visited:
                visited.append(value)
                if value == target:
                    return True
                    break


                for next_vert in self.vertices[value]:
                    stack.append(next_vert)
        return False

        # while x:
        #     z = x.pop()
        #     if x == target:
        #         break
        #     x.extend(self.vertices[z])
        #
        # return x

    def rec_dfs(self, start, target=None, visited=[]):
        visited.append(start)

        if start == target:
            return True

        for v in self.vertices[start]:
            if v not in visited:
                if self.rec_dfs(v, target, visited):
                    return True
            # graph_rec(v)
        return False

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

graph = Graph()

print(graph.vertices)
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')
print(graph.vertices)
graph.add_edge('0', '1')
graph.add_edge('0', '2')
graph.add_edge('1', '3')
graph.add_edge('2', '6')
graph.add_edge('3', '7')
graph.add_edge('1', '4')
graph.add_edge('1', '5')
graph.add_edge('4', '8')
graph.add_edge('4', '9')
print(graph.vertices)

print(graph.dfs('0', '9'))
print(graph.rec_dfs('0', '10'))
