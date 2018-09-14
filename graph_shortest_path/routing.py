#/usr/bin/env python

import sys

class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight

class Vertex:
    def __init__(self, value='vertex', color='white', parent=None):
        self.value = value
        self.edges = []
        self.color = color
        self.parent = parent

class Graph:
    def __init__(self):
        self.vertices = []

    def find_vertex(self, value):
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        return None

    def bfs(self, start):
        queue = []
        queue.append(start)
        visited = []
        while len(queue) > 0:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                for edge in vertex.edges:
                    next_vert = edge.destination
                    if not next_vert.parent:
                        next_vert.parent = vertex
                    queue.append(next_vert)

    # print("Start: ", start)
    # print("Start parent: ", start.parent)
    # print("Current vert value: ", current_vert.value)
    # print("Path: ", path)

    def output_route(self, start):
        path = []
        current_vert = start
        while current_vert.parent:
            path.append(current_vert.value)
            current_vert = current_vert.parent
        return " --> ".join(path)

    def route(self, start, end):
        # BFS to build the parent reference tree
        self.bfs(end)
        # print the route from the start Vertex
        self.output_route(start)


# Helper function to add bidirectional edges
def add_edge(start, end):
    start.edges.append(Edge(end))
    end.edges.append(Edge(start))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: routing.py hostA hostB')
        sys.exit()

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

    # Look up the hosts passed in from the command line by
    # name to see if we can find them.
    hostAVert = graph.find_vertex(sys.argv[1])

    if hostAVert is None:
        print('routing.py: could not find host: ', sys.argv[1])
        sys.exit()

    hostBVert = graph.find_vertex(sys.argv[2])

    if hostBVert is None:
        print('routing.py: could not find host: ', sys.argv[2])
        sys.exit()

    # Show the route from one Vertex to the other
    graph.route(hostAVert, hostBVert)
