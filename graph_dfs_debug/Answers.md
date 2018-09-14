# Describe the fixes/improvements you made to the Graph implementation here.

To show the edges, graph add_edge method was written in correctly (each vertex was connected to its self), the solution is, for each connection it must connect the start vertex with the end vertex, and it you are trying to make bidirectional connection, it will also need to conenct the end with the start vertex.

For the second issue, the find_components method was not building up any component, to fix that problem, on line 60, I have changed the if statemment to check the current vertex, if it has not been visited. then, it can build up the connected components

And another issue with that is, since the method is expecting some result from the dfs method, which was running infinte loop, was not checking the right target, was not doing through the vertex branch, and is returning empty list at the end.
To fix that,I have emplemnted stack and a visited list to check, so we dont check then again, then we would take vertex from the bottom, and check each one until the we found the target or the stack of empty
