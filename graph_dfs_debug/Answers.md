Describe the fixes/improvements you made to the Graph implementation here.
In Vertex class, renamed label to vert_label and removed the str() from self.label
In Graph class changed the add_vertex method so that it calls the Vertex class instead of just set()
Refactored add_edge so that it is accessing the edges of each vertex.