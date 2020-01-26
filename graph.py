from stack import Stack
from queue import Queue

class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex_id):
    if vertex_id in self.vertices:
      pass
    else:
      self.vertices[vertex_id] = set()

  def add_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
      # add to the dict of the first vertex
    else:
      raise IndexError("Missing Vertex, One or more vertices don't exist")

  def get_neighbors(self, vertex_id):
    return self.vertices[vertex_id]
    # gives a dictionary of all items associated with the vertex given it is a valid one

  def bft(self, starting_vertex):
    # Create a queue/stack as appropriate
    queue = Queue()
    # Put the starting point in that
    queue.enqueue(starting_vertex)

    # Make a set to keep track of where we've been
    visited = set() 
    # a set is better than a list ins this scenario because there is no duplication being done with a set
    # sets are a variant of hashtables so the time complexity for look ups is O(1)

    # While there is stuff in the queue/stack
    while queue.size() > 0:
      # Pop the first item
      vertex = queue.dequeue()
      # If not visited
      if vertex not in visited:
        # DO THE THING!
        print(vertex)
        visited.add(vertex)
        # For each edge in the item
        for next_vert in self.get_neighbors(vertex):
        # Add that edge to the queue/stack
          queue.enqueue(next_vert)

  def dft(self, starting_vertex):
    # Create a queue/stack as appropriate
    stack = Stack()
    # Put the starting point in that
    stack.push(starting_vertex)
    # Make a set to keep track of where we've been
    visited = set()
    # While there is stuff in the queue/stack
    while stack.size() > 0:
    # Pop the first item
      vertex = stack.pop()
    # If not visited
      if vertex not in visited:
    # DO THE THING!
        print(vertex)
        visited.add(vertex)
    # For each edge in the item
        for next_vert in self.get_neighbors(vertex):
    # Add that edge to the queue/stack
          stack.push(next_vert)

  def dft_recursive(self, starting_vertex, visited = None):
    if visited is None:
      visited = set()
    visited.add(starting_vertex)
    print(starting_vertex)
    for child_vert in self.vertices[starting_vertex]:
      if child_vert not in visited:
        self.dft_recursive(child_vert, visited)

  def bfs(self, starting_vertex, destination_vertex):
    # Create a queue/stack as appropriate
    queue = Queue()
    # Put the starting point in that
    # Enstack a list to use as our path
    queue.enqueue([starting_vertex])
    # Make a set to keep track of where we've been
    visited = set()
    # While there is stuff in the queue/stack
    while queue.size() > 0:
      # Pop the first item
      path = queue.dequeue()
      vertex = path[-1]
      # If not visited
      if vertex not in visited:
        if vertex == destination_vertex:
          # Do the thing!
          return path
        visited.add(vertex)
        # For each edge in the item
        for next_vert in self.get_neighbors(vertex):
          # Copy path to avoid pass by reference bug
          new_path = list(path) # Make a copy of path rather than reference
          new_path.append(next_vert)
          queue.enqueue(new_path)


  def dfs(self, starting_vertex, destination_vertex):
    # Create a queue/stack as appropriate
    stack = Stack()
    # Put the starting point in that
    # Enstack a list to use as our path
    stack.push([starting_vertex])
    # Make a set to keep track of where we've been
    visited = set()
    # While there is stuff in the queue/stack
    while stack.size() > 0:
      # Pop the first item
      path = stack.pop()
      vertex = path[-1]
      # If not visited
      if vertex not in visited:
        if vertex == destination_vertex:
          # Do the thing!
          return path
        visited.add(vertex)
        # For each edge in the item
        for next_vert in self.get_neighbors(vertex):
        # Copy path to avoid pass by reference bug
          new_path = list(path) # Make a copy of path rather than reference
          new_path.append(next_vert)
          stack.push(new_path)
  
  def dfs_recursive(self, starting_vertex,  target_value, visited=None, path=None):
    if visited is None:
      visited = set()
    if path is None:
      path = []
    visited.add(starting_vertex)
    path = path + [starting_vertex]
    if starting_vertex == target_value:
      return path
    for child_vert in self.vertices[starting_vertex]:
      if child_vert not in visited:
        new_path = self.dfs_recursive(child_vert, target_value, visited, path)
        if new_path:
          return new_path
    return None