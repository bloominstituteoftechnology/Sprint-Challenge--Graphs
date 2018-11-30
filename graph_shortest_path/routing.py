#/usr/bin/env python

import sys

# Queue for BFS
class Queue:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop(0) if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)

    # for indexing
    def __getitem__(self, index):
        return self.storage[index]

    def __setitem__(self, index):
        return self.storage[index]

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
        # looping over all vertices and if the value matches return the vert otherwise return none
        for vert in self.vertices:
            if vert.value == value:
                return vert
        return None

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        # bfs needs a rework
        # rework idea using my new Queue() class updates

        # create an empty queue
        queue = Queue()

        # # loop over the vertices setting them to while like in bokeh grids
        ## and clear the parents
        for vert in self.vertices:
            vert.color = "white"
            vert.parent = None
        
        ## set the starting vert color to gray
        ## and add it to the queue
        start.color = "gray"
        queue.enqueue(start)

        ## while the queue has some items grab the first item off it and set it to the current one
        while queue.size() > 0:
            current = queue[0] # this made me have to make some new methods in my queue class

            ## loop over thr edges and if the edge destination is white then 
            ## set the edge destination to gray and set the edge destination pareent to the current
            ## and add the edge.destination to the queue
            for edge in current.edges:
                if edge.destination.color == "white":
                    edge.destination.color = "gray"
                    edge.destination.parent = current
                    queue.enqueue(edge.destination)

            ## set the current color to black and and deque the front off
            current.color = "black"
            queue.dequeue()




    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # going back to basics to get a simplified version with a list comprehension
        route_list = []
        vert = start

        while vert:
            route_list.append(vert)
            vert = vert.parent

        print(" --> ".join([F"{v.value}" for v in route_list]))
        return " --> ".join([F"{v.value}" for v in route_list]) # this breaks bfs

    def route(self, start, end):
        # BFS to build the parent reference tree
        self.bfs(end)
        # print the route from the start Vertex
        self.output_route(start)


# Helper function to add bidirectional edges
def add_edge(start, end):
    start.edges.append(Edge(end))
    end.edges.append(Edge(start))


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
