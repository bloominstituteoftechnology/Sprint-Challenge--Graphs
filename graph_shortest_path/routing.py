#/usr/bin/env python

import sys

# Queue Class

class Queue: #FIFO
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
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
        self.edges = [] # note edges are a list not a set
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
        # !!!! IMPLEMENT ME
        if value in self.vertices:
            return self.vertices[value]
        else:
            return None

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
    def bfs(self, start, target):
        for vertex in self.vertices:
            vertex.color = 'white'
            vertex.parent = None

        visited = []
        # create a queue for BFS
        queue = Queue()
        start.color = 'green' # give the starting vertext a color
        queue.enqueue(start) # place the starting node in the queue
        while queue.size() > 0: # when the queue is not empty
            # Dequeue a vertex from the queue and print it
            current = queue.dequeue() # remove the first element from the queue
            visited.append(current) # mark the removed node as visited
            print(current)
            if current == target:
                return True
            # Get all adjacent vertices of the dequeued vertex.  If adjacent has not been visited, then mark it visited and enqueue it
            for vertex in self.vertices[current].edges: # for each child node
                if vertex not in visited: # if the node has not been visited
                    queue.enqueue(vertex) # place the node in the back of the queue
                    vertex.destination.color = 'red'
                    vertex.destination.parent = current
                    queue.push(vertex.destination)
            queue.dequeue()
            current.color = 'grey'

        return False

    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # !!!! IMPLEMENT ME
        current = start
        output = f"{current.value}"
        while current.parent is not None:
            current = current.parent
            output = f"{current.value} --> {output}"
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
    graph.route(hostAVert, hostDVert)

main()



