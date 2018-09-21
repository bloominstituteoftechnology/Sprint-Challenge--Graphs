Describe the fixes/improvements you made to the Graph implementation here.
A. the following code: 
'def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(start)'
has two lines to be fixed: 
1. self.vertices[start].add(start) - goal here is to connect next element(end)
=> self.vertices[start].add(end)
2. self.vertices[end].add(end) - same thing. End point needs to be connected with the start point
=> self.vertices[end].add(start)

B. changed naming of DFS and DFS_rec variables to be more descriptive
x -> stack
y -> visited
z -> popped
C. changed:  if vertex not in visited 
