Describe the fixes/improvements you made to the Graph implementation here.

Errors in:

def dfs(self, start, target=None):

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

# should return the visited vertices
# return x

  return y

#error - vertex is reachable if is not visited yet, this will help to track if is a different component and select a color for this component
# if vertex in visited:
            
  if vertex not in visited:


