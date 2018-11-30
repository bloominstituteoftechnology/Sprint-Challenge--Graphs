#/usr/bin/env python

import sys

print('\n --- NEW FILE RUN ---')
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
        self.parent = parent # *** this is what gets changed during BFT ***

# class Queue:
#   def __init__(self):
#     self.size = 0         # not sure if I need this
#     self.storage = []

#   def enqueue(self, item):
#     self.storage.append(item)
#     print(f'{item} added to q')
  
#   def dequeue(self):
#     if len(self.storage) == 0:
#       return None
#     else:
#       return self.storage.pop(0)

#   def len(self):
#     if len(self.storage) == 0:
#       return 0
#     else:
#       return len(self.storage)

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
        vertex_found = False

        for vertex in self.vertices:
            if vertex.value == value:
                vertex_found = True
                return vertex

        if vertex_found is False:
            return None

    def bfs(self, start): # start could be end
        """
        this is basically changing self.parent of each vertex

        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        print('\n--- New BFS ---\n')
        q = []
        visited = set()
        q.append(start)
        print(f'starting q = ', q[0].value)

        while len(q) > 0:
            vertex = q.pop()
            
            print(f'Visiting {vertex.value}')
            if vertex not in visited:
                visited.add(vertex)
                print(f'Vertex {vertex.value} has been visited')
                
                if vertex.edges is None:
                    print('no edges')
                    return None

                else: # if it has edges
                    for child in vertex.edges:
                        if child.destination not in visited:
                            q.append(child.destination)
                            if child.destination != vertex:
                                child.destination.parent = vertex
                            print('child added to q')
                            print('parent is ', vertex.value)
                    # for edge in range(0, len(vertex.edges - 1)):
                    #     print(vertex.edges[edge])
                    # if vertex.parent is None: # and if it doesn't have a parent
                    #     vertex.parent = vertex.edges[0]
                    
        start.parent = None

    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bft` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        route = []
        vertex = start
        
        print(vertex.parent.value)
        while vertex.parent is not None:

            route.append(vertex.parent.value)
            vertex = vertex.parent

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
    else:
        print('hostAVert is: ', hostAVert.value)

    hostBVert = graph.find_vertex(sys.argv[2])

    if hostBVert is None:
        print('routing.py: could not find host: ', sys.argv[2])
        sys.exit()
    else:
        print('hostBVert is: ', hostBVert.value)  

    # Show the route from one Vertex to the other
    # ************ I SWITCHED start and end here *****************
    graph.route(hostAVert, hostBVert) 
