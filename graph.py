class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if hasattr(self.vertices, f'vertex_id') is not True:
            print("vertex is new")
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            # will throw error if v2 key not in vertices
            check = self.vertices[v2]
            self.vertices[v1].add(v2)  # this add method comes with sets
        except KeyError:
            print(f'There is no "{v2}" vertex')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        scheduled = Queue()
        # add the starting node to said queue
        scheduled.enqueue(starting_vertex)
        # use a set for breadcrumbs
        visited = set()
        # while there are still vertices scheduled to be visited
        while scheduled.size():  # same as while scheduled.size()
            # remove the first item, since you're visiting it right now
            current_vertex = scheduled.dequeue()
            # if we have not visited this one yet
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                # go through the neighbors
                for next_vertex in self.get_neighbors(current_vertex):
                    # schedule the node to visit it later
                    scheduled.enqueue(next_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        scheduled = Queue()
        # add the starting node to said queue
        # for the search, put it inside a list in order to keep track of the path
        scheduled.enqueue([starting_vertex])
        # use a set for breadcrumbs
        visited = set()
        # while there are still vertices scheduled to be visited
        while scheduled.size() > 0:
            # get the current vertex by getting its path and referencing it from the end of the path
            path = scheduled.dequeue()
            current_vertex = path[-1]
            # if we have not visited this one yet
            if current_vertex not in visited:
                # check if the current one is the destination
                if current_vertex == destination_vertex:
                    # if it is, return the path to how you got there
                    return path
                # keep going otherwise
                visited.add(current_vertex)
                # go through the neighbors
                for next_vertex in self.get_neighbors(current_vertex):
                    # schedule the node to visit it later and include it in the path
                    # just doing path.append(next_vertex) will cause bug by changing the original path variable
                    # scheduled will end up with copies full of the same thing
                    # lists get passed by reference, so we need to make an explicit copy
                    path_copy = list(path)
                    path_copy.append(next_vertex)
                    # add the new path to the list of possibilities in the scheduled stack
                    scheduled.enqueue(path_copy)
