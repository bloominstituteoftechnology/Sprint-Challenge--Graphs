# Describe the fixes/improvements you made to the Graph implementation here.

## Errors in:

### def dfs(self, start, target=None):

#error - unused vaiable y, and set with initial value of x, should be empty
# y = set(x)

  y = set()

#error - x is a list of vertices, should be the current vertex to compare with the target
# if x == target:

  if z == target:

#error - we have to add to y the visited Vertex(z)
            
  y.add(z)

#error - we add to the x queue all the vertices connected with this current vertex z excludind the ones already visited
# x.extend(self.vertices[z])            
            
  x.extend(self.vertices[z]- y)

# should return the visited vertices
# return x

  return y

# instead of break should return the vertex 
#if z == target:
#    break

if z == target:
    return z

Errors in:

def add_edge(self, start, end, bidirectional=True):

#error - edge has to be connected with a different Vertex no the same one
# start connects with end
# self.vertices[start].add(start)

  self.vertices[start].add(end)

#error - edge has to be connected with a different Vertex no the same one
# end connects with start if is bidirectional
# if bidirectional:
#     self.vertices[end].add(end)
  
  if bidirectional:
      self.vertices[end].add(start)

Errors in:

def find_components(self):

#error - vertex is reachable if is not visited yet, this will help to track if is a different component and select a color for this component
# if vertex in visited:
            
  if vertex not in visited:


# TODO check if edge already exists
  if vertices[1] not in graph.vertices[vertices[1]]:
      graph.add_edge(vertices[0], vertices[1])


Lint errors in:

def graph_rec(self, start, target=None):

#error - x is a set and has not have a append() method, only add() method should be used
# x.append(start)
        
  x.add(start)

  #error - graph_rec() is a recursive call to a method inside the same class needs to be called with self
  # for v in self.vertices[start]:
  #     graph_rec(v)

    for v in self.vertices[start]:
        self.graph_rec(v)


Variables names changes:

    def add_edge(self, start, end, bidirectional=True):
        #error - edge has to be connected with a different Vertex no the same one
        # start connects with end
        # self.vertices[start].add(start)
        self.vertices[start].add(end)
        #error - edge has to be connected with a different Vertex no the same one
        # end connects with start if is bidirectional
        # if bidirectional:
        #     self.vertices[end].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        #error - unused vaiable y, and set with initial value of x, should be empty
        # y = set(x)
        visited_vertices = set()
        while stack:
            current_vertex = stack.pop()
            #error - x is a list of vertices, should be the current vertex to compare with the target
            # if x == target:
            # instead of break should return the vertex 
            # if z == target:
            #     break
            if current_vertex == target:
                return current_vertex
            #error - we have to add to y the visited Vertex(z)
            visited_vertices.add(current_vertex)
            #error - we add to the x stack all the vertices connected with this current vertex z excludind the ones already visited
            # x.extend(self.vertices[z])            
            stack.extend(self.vertices[current_vertex] - visited_vertices)

        # should return the visited vertices
        # return x
        return visited_vertices
