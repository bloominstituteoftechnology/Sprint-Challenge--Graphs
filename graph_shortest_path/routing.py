#/usr/bin/env python

import sys

# Queue Class
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


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
        # Loop through self.vertices list and look for vertex
        for vertex in self.vertices:
            # if vertex.value is value, whose default value is 'vertex'
            if vertex.value == value:
                # return vertex
                return vertex
        # return None if no such Vertex exists in the Graph
        return None

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        # Create an empty queue
        q = Queue()

        # Add initial vertex to the queue
        q.enqueue(start)

        # while the queue is not empty...
        while q.size() > 0:
            # remove the first vertex from the queue
            vertex = q.dequeue()

            # check to see if it is visited
            # if the vertex is color white, which is the default color
            # and means that it is unvisited
            if vertex.color == 'white':
                # change the color to not_white, which means it has been visited
                vertex.color = 'not_white'
                # Loop through each edge in vertex.edges
                for edge in vertex.edges:
                    # edge.destination is a child in the graph
                    # rename it destination
                    destination = edge.destination
                    # if the color of the child vertex is white, child has not been visited...
                    if destination.color == 'white':
                        # set previous node as parent to vertex
                        destination.parent = vertex
                        # put the vertex at the end of the queue
                        q.enqueue(vertex)

    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # start from the tail
        # this is the vertex we are looking at
        last_vertex = start
        # build a string so that output will print a '-->' in between vertices
        flowArrow_str = ''

        # if there is a tail...
        while last_vertex is not None:
            # Add the tail to the string to print out
            flowArrow_str = flowArrow_str + last_vertex.value

            # if the tail has a parent
            # there is an arrow before it
            if last_vertex.parent is not None:
                # add '-->' before the tail
                flowArrow_str = flowArrow_str + '-->'
                
            # make the parent the new starting point
            last_vertex = last_vertex.parent
        print(flowArrow_str)


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
