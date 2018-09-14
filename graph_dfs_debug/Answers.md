Describe the fixes/improvements you made to the Graph implementation here.


In method add_edge fixed  self.vertices[start].add(end) and self.vertices[end].add(start)

In method dfs variables named with x changed to stack and y to visited and z to current_vertex. return needs to return visited instead of stack. visited.add(current_vertex) added to method.  visited = set() changed. changed if current_vertex == target: from stack. 