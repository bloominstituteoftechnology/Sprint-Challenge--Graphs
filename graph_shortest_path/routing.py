#/usr/bin/env python

import sys

# Queue class
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        return self.queue.append(element)
    def dequeue(self):
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        if len(self.queue) <= 0:
            return True

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
        # !!!! IMPLEMENT ME
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        return None

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue(start)
        # Check starting points neighboring nodes
        # Go into self.vertices and match string to target
        # Then loop through the edges
        # While queue is not empty
        while not q.isEmpty():
            dq = q.dequeue()
            # Already visited
            if dq.color == "white":
                dq.color = "black"
                for edge in dq.edges:
                    vertex = edge.destination
                    # If it wasn't visited
                    if vertex.color == "white":
                        vertex.parent = dq
                        q.enqueue(vertex)
            """
            Original code
            else:
                dq.color = "black"
                for vertex in self.vertices:
                    if vertex.value != dq:
                        return None
                    else:
                        for edge in vertex.edges:
                            dest = edge.destintion
                            
                            print(neighbor)
                            # Should have gone one more deep to grab destination
                            # At this point we're just attributing .parent onto an edge, not the Vertex node held by destintion
                            neighbor.parent = dq
                            q.enqueue(neighbor)
            """
            # """
            # Solution code
            # queue = Qeueu()
            # queue.enquque(start)

            # while queue.size() > 0:
            #     vertex = queue.dequeue()
            #     if vertex.color == "white":
            #         vertex.color = "black"
            #         # Loop through edges for this vertex
            #         for edge in vertex.edges:
            #             dest = edge.destination:
            #             if dest.color == "white":
            #                 dest.parents = vertex 
            #                 queue.enqueue(dest)
            # """
    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # Initialize starting vertex
        # !!! When we input the text 'HostA' the sys.argv regonizes the text as the Variable HostA = Vertex('HostA')
        starting_node = start
        print(start)
        print(starting_node)
        # Store collected string into a variable so we can contain it and present it all at once
        output_string = ""
        print(output_string)

        # While there is a node to start
        while starting_node is not None:
            # Append to node
            # starting_node.value because it is an Instance 
            output_string += starting_node.value
            if starting_node.parent is not None:
                # We need this hedge to separate Vertex's and when there is a parent node to add to output_string
                output_string += " --> "
            # Since we're traversing bottom up/child to parent, we're checking if parent exists
            # We want to keep the loop going therefore we reset the conditional variable to the parent
            starting_node = starting_node.parent
        print(output_string)
        
        # while not :
        #     dq = q.dequeue()
        #     for vertex in self.vertices:
        #             if vertex.value != dq:
        #                 return None
        #             else:
        #                 for neighbor in vertex.edges:
        #                     print(neighbor)
        #                     neighbor.parent = dq
        #                     q.enqueue(neighbor)

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
