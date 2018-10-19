"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label_id):
        self.label = str(label_id)
        self.edges = set()

    def __repr__(self):
        # return 'Vertex: ' + self.label 
        return f"{self.edges}" 
        

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        # self.components = 0

    def add_vertex(self, label_id):
        self.vertices[label_id] = Vertex(label_id)

    def add_edge(self, start, end, bidirectional=True):
        if end in self.vertices and start in self.vertices and bidirectional:
            self.vertices[start].edges.add(end)
            self.vertices[end].edges.add(start)
        elif end in self.vertices and start in self.vertices and bidirectional == False:
              self.vertices[start].edges.add(end)
        
        else:
            raise IndexError("That vertex does not exist currently!")


    def dfs(self, start, target=None):
        x = []
        x.append(start)
        y = set(x)

        while x:
            z = x.pop()
            if x == target:
                break
            x.extend(self.vertices[z])

        return x

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x

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



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    for i in range(6):
        graph.add_vertex(str(i))

    graph.add_edge('0', '1', True)
    graph.add_edge('0', '3')
    graph.add_edge('1', '2')
    graph.add_edge('2', '4')
    graph.add_edge('2', '5')
    # graph.add_edge('0', '4')
    # graph.add_edge('3', '0')
    # print('===graph.bfs_path:', graph.bfs_path('0', '4'))
    # print(graph.dft('0'))

print(graph.vertices)
    # print(graph.vertices)