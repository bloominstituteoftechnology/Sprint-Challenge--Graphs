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

    def remove_item(self, index):
        return self.stack.pop(index)

    def size(self):
        return len(self.stack)


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        If both exist add a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue or stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #   Pop the first item
            vertex = stack.pop()
            #   if not visited
            if vertex not in visited:
                # DO NOTHING!
                print(vertex)
                visited.add(vertex)
                #  for each edge in th item:
                for next_vert in self.get_neighbors(vertex):
                    # Add that edge to the queue/stack
                    stack.push(next_vert)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue or stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enqueue as a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            # Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
            # if not visited
            if vertex not in visited:
                # DO NOTHING!
                if vertex == destination_vertex:
                    # Do the thing!
                    return path  # possibly return the thing
                visited.add(vertex)
                # for each edge in th item:
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)  # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    queue.enqueue(new_path)