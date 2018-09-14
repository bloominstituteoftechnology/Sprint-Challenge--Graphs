# Describe the fixes/improvements you made to the Graph implementation here.

To show the edges, graph add_edge method was written in correctly (each vertex was connected to its self), the solution is, for each connection the start vertex should be connected to the end vertex, and it you are trying to make bidirectional connection, it will also need to create a connection from the end to the start vertex.

For the second issue, on line 60, I have changed the if statement to check the current vertex from each for loop of self.vertices, and check that if it has not been visited. on the first and only time we visited each vertex, we grab all the children of that vertex, and update the visited list

And another issue with that is, since the method is expecting some result from the dfs method, which was running infinite loop, was not checking the right target, was not going through the vertex branch, and is returning empty list at the end.
To fix that,I have implemented stack and a visited list to check, so we don't check then again, then we would take vertex from the bottom, and check each one until the we found the target or the stack of empty
