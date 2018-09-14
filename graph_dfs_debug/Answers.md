Describe the fixes/improvements you made to the Graph implementation here.

add edges to the Vertex object to let it keep track of it's associated nodes. Removed the str() cast from Vertex since input is always taken in as strings. 

in add_edge, swapped end assignment of edges so start attaches to end and end to start, not start to start and end to end. 

in add_vertex, removed ability to pass in edge list when creating vertex, these edges wouldn't be properly connected to their corresponding endpoints, edges can be added only through add_edge in keeping with the principle that each function does one thing well. 

In DFS, changed "y" to "visited". Changed "x" to "stack". change "z" to "current". and x.pop() to stack.pop(). Changed Break to return True if current == value, added visited to dfs. Changed stack.extend(self.vertices[z]) to a for loop which checks each child node of current, and only adds them if they're no in visited already. Changed return x to return False, if we haven't found the node. Added .edges to self.vertices[current] to access the Vertice objects edges. 

Changed graph_rec to dfs_recursive(). Added visited to the arguments of dfs_recursive.  changed, x = set() and x.append(start) to simply visited.append(start). Made a base case to check if our current value is the target value and return True if so. Changed v to child. Add conditional to check if child nodes of current not already in visited. 



In Draw.py

Changed line 36 from .keys() to .values() to get the Vertex objects themselves, not just their indexes. 

in line 69-74, changed edges to vertexObject (since that's what it's grabbing, graph is a dictonary of keys (indexes) and values (Vertex Objects))