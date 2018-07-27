Describe the fixes/improvements you made to the Graph implementation here.

1. I added a conditional on line 20 to check if the vertex provided already exists in self.vertices. If it does, I added an exception to be raised on line 21. 

2. I added a conditional on line 22 to check if the edges provided exists as a subset of self.vertices. If it does, I added an exception to be raised on line 23. 

3. I added conditionals and exception statements from line 28 to line 31 to check if the start and end edges provided are in self.vertices. 

4. Fixed line 37 to be self.vertices[start].add(end) instead of self.vertices[start].add(start). Fixed line 40 to be self.vertices[end].add(start) instead of self.vertices[end].add(end).  

5. I renamed the dfs method to search and changed its properties to accept either bfs or dfs. I also renamed variables for better readability (e.g. queue_stack and visited instead of x and y). I recoded the loop in the search method to pop an item from the queue_stack using the pop_index and to check if the current_vertice that was popped out is equal to the target. If it does, break from the loop. If it does not, add the current vertice to the visited set and extend the queue_stack using the value of self.vertices[current_vertice] - visited. 