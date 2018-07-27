Describe the fixes/improvements you made to the Graph implementation here.

in def add_edge:()
self.vertices[start].add(start)
changed to:
self.vertices[start].add(end) -> i changed it to end because we are adding edges and it has to have a start and end.
self.vertices[end].add(end) 
changed to:
self.vertices[end].add(start) -> i specified a start or else it won't know to add start.

in def dfs():
i changed all x variable names to stack because it makes more sence.  I also changed z to current and y to visited.
