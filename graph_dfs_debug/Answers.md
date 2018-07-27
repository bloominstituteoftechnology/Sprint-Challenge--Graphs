Describe the fixes/improvements you made to the Graph implementation here.

Graphs.py
(1) the .append method is for lists. We want to use .add for a set. Changed Line 41 to x.add(start), 
(2) inside function 'dfs', changed variable 'x' to 'stack', 
(3) changed variable 'y' to 'visited', 
(4) changed variable 'z' inside while statement to 'current', 
(5) amended line 36 previously x.extend to 'stack.extend(self.vertices[current] - visited)', 
(6) changed .append in in graph_rec function to .add; no .append for set, 
(7) in 'add_edge' method, you need to connect 'start' to 'end', 'self.vertices[start].add(start)' should be 'self.vertices[start].add(end)' and do the same in the if statement,  
(8) 
