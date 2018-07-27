Describe the fixes/improvements you made to the Graph implementation here.

1) function on line 50 of graph py; Needed [if vertex NOT in visited].

2) Change in bfs method [stack.extend(self.vertices[current] - visited]

3) Also, changed the variables x, z  

4) In add_edge added;
if start not in self.vertices or end not if
    self.vertices:
        raise Exception('Vertices not in graph!')

5) Also, in add_edge switch up:
self.vertices[start].add(end)
    if bidirectional:
        self.vertices[end].add(start)          
