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
        self.color = color
        # Parent reference to keep track of the previous node in the
        # graph when traversing through the graph
        self.parent = parent


# Graph class
class Graph:
	def __init__(self):
		self.vertices = []

	def find_vertex(self, value):
		for i in self.vertices:
			if i.value == value:
				return i
		return None
		pass
	
	def bfs(self, start, end):
		found = [start]
		index = 0
		current = start
		while current != end:
			for i in current.edges:
				next_node = self.find_vertex(i.destination.value)
				if next_node not in found:
					next_node.parent = current
					found.append(next_node)
			index = index + 1
			current = found[index]
		print ("all nodes checked:\n")
		for i in found:
			if i.parent:
				print("Node: {}, parent: {}".format(i.value,i.parent.value))
			else:
				print("Node: {}, parent: {}".format(i.value,i.parent))
		self.output_route(end, found)
		pass

	def output_route(self, end, data):
		path = ""
		current = end
		while current.parent:
			path = path + "{} => ".format(current.value)
			current = current.parent
		path = path + "{}".format(current.value)
		print ("\n{}\n".format(path))
		for i in data:
			i.parent = None
		pass

	def route(self, start, end):
		self.bfs(start, end)


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
