Describe the fixes/improvements you made to the Graph implementation here.
Edges were being made from the start node to the start node and vice versa. Fixed so edges would be made from start node to the end node.
changed vertex in visited on line 65 to vertex not in visited, fixes color issue
rewrote dfs to use a stack method, made the variables more explicit