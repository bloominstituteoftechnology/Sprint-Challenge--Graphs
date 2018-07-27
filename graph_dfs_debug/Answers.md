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
line 34 changed stack to current because we are looking for current target
line 35 changed break to return target beause we want to return a target
line 36: changed it to visited.add(current) because we're adding the current to the stack
line 37: stack.extend(self.vertices[current] - visited) -> i want to subtract what's visited from the vertices and what's remaining to the stack
line 39: return visited -> that's the info we want returned

line 47-60: added bfs method to be able to perform bfs method

def find_components:
line 74: changed code because if I've already been there, I don't wnt to repeat it.
