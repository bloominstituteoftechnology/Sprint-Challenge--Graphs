
import sys

# Edge class
class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight
#Vertex class
class Vertex:
    def __init__(self,value='vertex', color="white", parent=None):
        self.value = value
        self.edges = []
        self.color = color
        self.parent = parent 
 #Graph class

class Graph:
    def __init__(self):
        self.vertices = []
    

    '''
    * function looks through all the vertices in the graph and returns the
    * first one it finds that matches the value parameter.
    *
    * Used from the main code to look up the verts passed in on the command
    * line.
    *
    * @param: {*} value: The value of the Vertex to find
    *
    * @return None if not found.
    * return {Vertex} the found vertex
    * 
    '''
    def find_vertex(self, value):
        #!!! IMPLEMENT ME
        vert = [v for v in self.vertices if v.value == value]
        
        return vert[0]
        

    '''
    * Breadth-First search from a starting vertex. self should keep parent
    * pointers back from neighbors to their parent.
    *
    * @param:Vertex start The starting vertex for the BFS
    '''
    def bfs(self, start):
        """Search the graph using BFS or DFS."""
        start.color = 'gray'
        queue = [start]

        #init func already doing this
        """
        for vertex in self.vertices:
            vertex.color = 'white'
            vertex.parent = None
        """
        # refactor
        """
        start.color = 'gray'
        queue.append(start)
        """
        while queue:
            current = queue.pop(0)

            for edge in current.edges:
                vertex = edge.destination
                if vertex.color ==  'white':
                    vertex.color = 'gray'
                    vertex.parent = current
                    queue.append(vertex)

            current.color = 'black'

    '''
    * Print out the route from the start vert back along the parent
    * pointers(self,set in the previous BFS)
    *
    * @param:Vertex start The starting vertex to follow parent
    * pointers from
    '''
    def output_route(self, start):
    #!!! IMPLEMENT ME
        vertex = start
        output = ''

        while (vertex):
            output += vertex.value
            if (vertex.parent):
                output += ' --> '
            
            vertex = vertex.parent
        
        print(output)
    
    # Show the route from a starting vert to an ending vert.
    
    def route(self, start, end):
        #Do BFS and build parent pointer tree
        self.bfs(end)

        #Show the route from the start
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
