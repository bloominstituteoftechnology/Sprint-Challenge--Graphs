Describe the fixes/improvements you made to the Graph implementation here.

Line Number | Before | After
----------- | ------ | -----
22 | ```self.vertices[start].add(start)``` | ```self.vertices[start].add(end)```
24 | ```self.vertices[end].add(end)``` | ```self.vertices[end].add(start)```
26 - 44 | x, y, z | quack, visited, vertex
43 | ```graph_rec(v)``` | ```self.graph_rec(v)```