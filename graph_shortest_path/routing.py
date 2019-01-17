#/usr/bin/env python

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
        # Vertex color used to mark vertices as visited or not in the traversal algorithm (BFS or DFS).
        self.color = color
        # Parent reference to keep track of the previously visited node in the graph when traversing through the graph. 
        self.parent = parent

# Graph class
class Graph:
    def __init__(self):
        self.vertices = []

    def find_vertex(self, value):
        """
        Looks through all the vertices in the graph instance and returns
        the first vertex it finds that matches the `value` parameter.

        Used in the `main` function to look up the vertices passed in
        from the command line.

        @param {*} value: The value of the Vertex to find

        @return None if no such Vertex exists in the Graph.
        @return {Vertex} the found Vertex
        """

        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        else:
            return None

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        for vertex in self.vertices:
            vertex.color = 'white'
            vertex.parent = None
        
        start.color= 'gray'
        queue = [start]
        # print(start.parent)
        while len(queue)>0:
            # print([vertex.value for vertex in queue])
            currentVert = queue[0]
            # print(currentVert.value)
            for edge in currentVert.edges:
                if edge.destination.color == 'white':
                    edge.destination.color = 'gray'
                    # print("edge.destination.parent = ", edge.destination.parent)
                    # print("edge.destination = ", edge.destination)
                    edge.destination.parent = currentVert
                    # print(edge.destination.parent.value)
                    queue.append(edge.destination)
            queue.pop(0)
            # print("queue length: ",len(queue))
            currentVert.color = 'black'
        
        # ## Not sure why this method isn't working. Will do more analysis at a later time. 
        # queue = [start]
        # while len(queue)>0:
        #     # print([vertex.value for vertex in queue])
        #     # print(len(queue))
        #     currentVert = queue.pop(0)
        #     if currentVert.color == 'white':
        #         currentVert.color = 'gray'
        #         for edge in currentVert.edges:
        #             currentVert.parent = edge.destination
        #             # edge.destination.parent = currentVert
        #             # print(edge.destination.parent)
        #             queue.append(edge.destination)
        #             # print(edge.destination.value)
        #     queue.pop(0)
        #     # print("queue length: ",len(queue))
        #     currentVert.color = 'black'

    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        route = [start.value]
        route_string = start.value
        while start.parent:
            start = start.parent
            route.append(start.value)     
        
        for i in range (1, len(route)):
            route_string = route_string + '-->' + route[i]
        print(route_string)

    def route(self, start, end):
        # BFS to build the parent reference tree
        self.bfs(end)
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
