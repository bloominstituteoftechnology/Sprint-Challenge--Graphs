Describe the fixes/improvements you made to the Graph implementation here.

In add_vertex:
    deleted edges() argument

    created an if statement to give an error message if added vertex already exists in the graph

    changed self.vertices[vertex]=set() to self.vertices[vertex]= set() 

In add_edge: changed it to
    if start not in self.vertices or end not in self.vertices:
        raise Exception('Error: start and/or end point do not exist')
    self.vertices[start].add(end)
    if bidirectional:
        self.vertices[end].add(start)

