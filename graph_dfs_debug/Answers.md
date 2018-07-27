Describe the fixes/improvements you made to the Graph implementation here.
* add_edge:
    . made sure the start and end point for the edge were viable vertices
    . changed self.vertices[start].add[start] to
    self.vertices[start].add[end] so the edges would connect 
    correctly
    . did the same with self.vertices[end].add[end] changed to
    self.vertices[end].add[start]

* add_vertex:
    . made sure we couldn't add the same vertex twice by adding
    lines 22 + 23
    . made sure that we were adding edges to vertices that exist
    by adding lines 24 25

* dfs:
    . changed variables to more readable / relevent names
    . also added visited.add(current) to keep track of visited
    vertices
    .refactored appending start to stack by initalizing stack with start already in it.

* find_components:
    . changed if vertex in visited to if vertex not in visited
    because otherwise all the nodes would end up being the same color!