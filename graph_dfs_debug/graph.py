"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label_id):
        self.label = str(label_id)
        self.edges = set()
        self.component = 0

    def __repr__(self):
        # return 'Vertex: ' + self.label 
        return f"Component: {self.component}" 
    
    def __hash__(self):
        return hash((self.label, ))
        

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

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


    def dfs(self, start):
        x = []
        x.append(start)
        visited = set(x)

        while x:
            current_vertex = x.pop()
            print(f"current vertex: {current_vertex}")
            for edge in current_vertex.edges:
                if self.vertices[edge] not in visited:
                    x.append(self.vertices[edge])
                    visited.add(self.vertices[edge])    
        return visited


    # def dfs(self, vertexObj, target=None) {
    #     vertex_list = []
    #     vertex_list.append(vertexObj)

    # }



    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x

    def find_components(self):
        print("find_components is being called")
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            print(f"vertex {vertex}")
            if vertex not in visited:
                reachable = self.dfs(self.vertices[vertex])
                for other_vertex in reachable:
                    print(f"other_vertex {other_vertex}")
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    for i in range(6):
        graph.add_vertex(str(i))

    graph.add_edge('0', '1')
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