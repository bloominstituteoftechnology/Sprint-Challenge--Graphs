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
        # Color of this vertex
        # Used to mark vertices for the traversal algorithm (BFS or DFS)
        # - grey: visited
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

        # reset color of all vertices to white (i.e. not visited)
        for vertex in self.vertices:
            vertex.color = 'white'
        queue = [[start]]
        while len(queue) > 0:
            current_path = queue.pop(0)
            current_vertex = current_path[-1]
            # if vertex has not been visit (i.e. colore = white):
            if current_vertex.color == 'white':
                for edge in current_vertex.edges:
                    child = edge.destination
                    child.parent = current_vertex
                    new_path = list(current_path)
                    new_path.append(child)
                    queue.append(new_path)
                    current_vertex.color = 'grey'
            output = []
            for vertex in current_path:
                output.append(vertex.value)
            print(output)
                
    def output_route(self, start, end):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # !!!! IMPLEMENT ME

        # reset all vertices colors
        for vertex in self.vertices:
            vertex.color = 'white'
        current_vertex = start
        # path = [current_vertex]
        # initiate the output variable
        output = current_vertex.value

        while current_vertex.parent.color != 'grey':
            # path.inse(current_vertex.parent)
            output += ' --> ' + current_vertex.parent.value
            current_vertex.color = 'grey'
            current_vertex = current_vertex.parent   
        print(output)

        # vertexE = self.find_vertex('HostE')
        # print("parent of HostE: ", vertexE.parent.value)

    def route(self, start, end):
        # BFS to build the parent reference tree
        self.bfs(start)
        # print the route from the start Vertex
        self.output_route(start, end)


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
