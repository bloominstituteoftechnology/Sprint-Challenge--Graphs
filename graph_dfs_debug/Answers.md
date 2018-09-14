Describe the fixes/improvements you made to the Graph implementation here.
1. Edges weren't connecting. You had vertices connecting to themselves rather than to other
vertices. I changed self.vertices[start].add(start) on line 22 to self.vertices[start].add(end)
and you did the same thing for bidirectional connections so I changed self.vertices[end].add(end)
on line 24  to self.vertices[end].add(start)

 
