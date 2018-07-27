# /usr/bin/env python

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
        """
        Looks through all the vertices in the graph instance and returns
        the first vertex it finds that matches the `value` parameter.
        """
        # !!!! IMPLEMENT ME
        # for item in self.vertices:
        #     if item.value == value:
        #         return item
        #     return None
        vert = [v for v in self.vertices if v.value == value]
        if len(vert) == 0:
            return None
        return vert[0]

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.
        """

        # I think the init already does this though
        # It's also not necessary for the output
        for item in self.vertices:
            item.color = 'white'
            item.parent = None

        start.color = 'gray'
        queue = []
        queue.append(start)

        while queue:
            current = queue.pop(0)

            for edge in current.edges:
                vertex = edge.destination
                if vertex.color == 'white':
                    vertex.color = 'gray'
                    vertex.parent = current
                    queue.append(vertex)
            current.color = 'black'

    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # !!!! IMPLEMENT ME
        vertex = start
        output = ''
        while vertex:
            output += vertex.value
            if vertex.parent:
                output += ' --> '
            vertex = vertex.parent
        print(output)

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
