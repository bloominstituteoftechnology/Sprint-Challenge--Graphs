#/usr/bin/env python

import sys

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.q.pop(0)
        else:
            return None

    def size(self):
        return len(self.q)


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
    # this is finding not adding 
    def find_vertex(self, value):

        # !!!! IMPLEMENT ME
        # pass

        for v in self.vertices:
            if v.value == value:
                return v
            return  None

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        change the color from white to black
        """
        #  all we are doing is recoloring a node (white which is default to black when 'visited')
        # !!!! IMPLEMENT ME
        # pass
        q = Queue()
        start.color = "w"
        q.enqueue(start)
        while q.size() > 0:
            v = q.dequeue()
            for edge in v.edges:
                destination = edge.destination
                if destination.color == "B":
                    destination.color = "B"
                    destination.parent = v
                    q.enqueue(destination)  
        # print(queue)     


    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # !!!! IMPLEMENT ME
        # pass

        s = start
        output = "Testing if this is firing?"

        while s is not None:
            output += s.value
            if s.parent is not None:
                output += "==>"
            s = s.parent
        # print(output)
        

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
        print('routing.py: could not find host1: ', sys.argv[1])
        sys.exit()

    hostBVert = graph.find_vertex(sys.argv[2])

    if hostBVert is None:
        print('routing.py: could not find host2: ', sys.argv[2])
        sys.exit()

    # Show the route from one Vertex to the other
    graph.route(hostAVert, hostBVert)

# going to add this 

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None

#     def size(self):
#         return len(self.queue)

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.stack)



# class Graph:

#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = Vertex(vertex_id)

#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].edges.add(v2)
#             self.vertices[v2].edges.add(v1)
#         else:
#             raise IndexError("That vertex does not exist")

#     def add_directed_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].edges.add(v2)
#         else:
#             raise IndexError("That vertex does not exist")

#     def bft(self, starting_node):
#         # Create an empty Queue
#         q = Queue()
#         # Create an empty visited list
#         visited = set()
#         # Add the start node to the queue
#         q.enqueue(starting_node)
#         # While the Queue is not empty...
#         while q.size() > 0:
#             # remove the first node from the Queue
#             node = q.dequeue()
#             # If it hasnt been visited
#             if node not in visited:
#                 # Mark it as visited
#                 print(node)
#                 visited.add(node)
#                 # then put all its children in the queue
#                 for child in self.vertices[node].edges:
#                     q.enqueue(child)

#     def dft(self, starting_node):
#         # Create an empty Stack
#         s = Stack()
#         # Create an empty visited list
#         visited = set()
#         # Add the start node to the stack
#         s.push(starting_node)
#         # While the Stack is not empty...
#         while s.size() > 0:
#             # remove the first node from the Stack
#             node = s.pop()
#             # If it hasnt been visited
#             if node not in visited:
#                 # Mark it as visited
#                 print(node)
#                 visited.add(node)
#                 # then put all its children in the stack
#                 for child in self.vertices[node].edges:
#                     s.push(child)

#     def dft_r(self, starting_node):
#         # Mark starting_node as visited
#         # Then call dft_r on each child
#         pass


#     visited = [1, 2, 3, 4]
#     queue = [[1, 2, 3, 5], [1, 2, 4, 6], [1, 2, 4, 7]]

#     def bfs(self, starting_node, destination_node):
#         # Create an empty Queue
#         q = Queue()
#         # Create an empty visited list
#         visited = set()
#         # Add the start node to the queue
#         q.enqueue(starting_node)
#         # While the Queue is not empty...
#         while q.size() > 0:
#             # remove the first node from the Queue
#             node = q.dequeue()
#             # If it hasnt been visited
#             if node not in visited:
#                 # Mark it as visited
#                 if destination_node == node:
#                     return True
#                 visited.add(node)
#                 # then put all its children in the queue
#                 for child in self.vertices[node].edges:
#                     q.enqueue(child)
#         return False

# class Vertex:
#     def __init__(self, vertex_id):
#         self.id = vertex_id
#         self.edges = set()