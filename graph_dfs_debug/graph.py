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
        if vertex not in self.vertices:
            self.vertices[vertex] = set(edges)
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Vertices not connecting in graph")
        else:
            #connect edges from start to end
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)

    def dfs(self, start, target=None):
        queue = [start]
        found = set()

        while queue:
            current = queue.pop(0)
            print('current', current)
            if current == target:
                return current
            found.add(current)
            # Add possible (univisited) vertices to queue
            print('found', found)
            queue.extend(self.vertices[current] - found)
        return found

    def graph_rec(self, start, target=None):
        # x = set()
        # x.append(start)
        # for v in self.vertices[start]:
        #     graph_rec(v)
        # return x

        stack = []
        stack.append(start)
        found = set(stack)

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                found.add(vertex)
                if vertex == target:
                    break
                stack.extend(self.vertices[vertex])
        return found


    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                print("found")
                if vertex not in visited:
                    reachable = self.dfs(vertex)
                    print('reachable', reachable)
                    for other_vertex in reachable:
                        other_vertex.component = current_component
                    current_component += 1
                    visited.update(reachable)
        self.components = current_component

graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
print("\n")
print("The Graph: ", graph.vertices)
#graph.dfs(3)
graph.find_components()