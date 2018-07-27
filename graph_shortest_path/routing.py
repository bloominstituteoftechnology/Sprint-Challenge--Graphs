import sys


# Edge class
class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight


# Vertex class
class Vertex:
    def __init__(self, value='vertex', color='white', parent=None):
        self.value = value
        self.edges = []
        # Color of this vertex
        # Used to mark vertices for the traversal algorithm (BFS or DFS)
        self.color = color
        # Parent reference to keep track of the previous node in the
        # graph when traversing through the graph
        self.parent = parent
        self.neighbors = set([])


# Graph class
class Graph:
    def __init__(self):
        self.vertices = []


    def append(self, vertex):
        self.vertices.append(vertex)


    def find_vertex(self, value):
        if len(self.vertices) > 0:
            for v in self.vertices:
                if v.value == value:
                    return v
        return None


    def bfs(self, startVert):
        for v in graph.vertices:
            v.color = 'white'
            v.parent = None

        startVert.color = 'gray'
        queue = [startVert]

        while queue:
            u = queue.pop(0)
            for v in u.neighbors:
                if v.color == 'white':
                    v.color = 'gray'
                    v.parent = u
                    queue.append(v)

            u.color = 'black'

    def output_route(self, start):
        route = []
        node = start
        while node.parent:
            route.append(node.parent.value)
            node = node.parent
        print(route)

    def route(self, start, end):
        # BFS to build the parent reference tree
        self.bfs(end)
        # print the route from the start Vertex
        self.output_route(start)


# Helper function to add bidirectional edges
def add_edge(start, end):
    # start.edges.append(Edge(end))
    # end.edges.append(Edge(start))
    start.neighbors.add(end)
    end.neighbors.add(start)


# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print('Usage: routing.py hostA hostB')
#         sys.exit()

graph = Graph()
vertA = Vertex('HostA')
vertB = Vertex('HostB')
vertC = Vertex('HostC')
vertD = Vertex('HostD')
vertE = Vertex('HostE')
vertF = Vertex('HostF')
vertG = Vertex('HostG')
vertH = Vertex('HostH')

add_edge(vertA, vertB)
add_edge(vertB, vertD)
add_edge(vertA, vertC)
add_edge(vertC, vertD)
add_edge(vertC, vertF)
add_edge(vertG, vertF)
add_edge(vertE, vertF)
add_edge(vertH, vertF)
add_edge(vertH, vertE)

graph.vertices.append(vertA)
graph.vertices.append(vertB)
graph.vertices.append(vertC)
graph.vertices.append(vertD)
graph.vertices.append(vertE)
graph.vertices.append(vertF)
graph.vertices.append(vertG)
graph.vertices.append(vertH)

for v in graph.vertices:
    print(v.value, [i.value for i in v.neighbors])

graph.route(vertA, vertD)
# Look up the hosts passed in from the command line by
# name to see if we can find them.
# hostAVert = graph.find_vertex(sys.argv[1])
#
# if hostAVert is None:
#     print('routing.py: could not find host: ', sys.argv[1])
#     sys.exit()
#
# hostBVert = graph.find_vertex(sys.argv[2])
#
# if hostBVert is None:
#     print('routing.py: could not find host: ', sys.argv[2])
#     sys.exit()
#
# # Show the route from one Vertex to the other
# graph.route(hostAVert, hostBVert)]

        while queue:
            u = queue.pop(0)
            for v in u.neighbors:
                if v.color == 'white':
                    v.color = 'gray'
                    v.parent = u
                    queue.append(v)

            u.color = 'black'

    def output_route(self, start):
        route = []
        node = start
        while node.parent:
            route.append(node.parent.value)
            node = node.parent
        print(route)

    def route(self, start, end):
        # BFS to build the parent reference tree
        self.bfs(end)
        # print the route from the start Vertex
        self.output_route(start)


# Helper function to add bidirectional edges
def add_edge(start, end):
    start.edges.append(Edge(end))
    end.edges.append(Edge(start))
    start.neighbors.add(end)
    end.neighbors.add(start)


# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print('Usage: routing.py hostA hostB')
#         sys.exit()

graph = Graph()
vertA = Vertex('HostA')
vertB = Vertex('HostB')
vertC = Vertex('HostC')
vertD = Vertex('HostD')
vertE = Vertex('HostE')
vertF = Vertex('HostF')
vertG = Vertex('HostG')
vertH = Vertex('HostH')

add_edge(vertA, vertB)
add_edge(vertB, vertD)
add_edge(vertA, vertC)
add_edge(vertC, vertD)
add_edge(vertC, vertF)
add_edge(vertG, vertF)
add_edge(vertE, vertF)
add_edge(vertH, vertF)
add_edge(vertH, vertE)

graph.vertices.append(vertA)
graph.vertices.append(vertB)
graph.vertices.append(vertC)
graph.vertices.append(vertD)
graph.vertices.append(vertE)
graph.vertices.append(vertF)
graph.vertices.append(vertG)
graph.vertices.append(vertH)


graph.route(vertA, vertD)
# Look up the hosts passed in from the command line by
# name to see if we can find them.
# hostAVert = graph.find_vertex(sys.argv[1])
#
# if hostAVert is None:
#     print('routing.py: could not find host: ', sys.argv[1])
#     sys.exit()
#
# hostBVert = graph.find_vertex(sys.argv[2])
#
# if hostBVert is None:
#     print('routing.py: could not find host: ', sys.argv[2])
#     sys.exit()
#
# # Show the route from one Vertex to the other
# graph.route(hostAVert, hostBVert)
