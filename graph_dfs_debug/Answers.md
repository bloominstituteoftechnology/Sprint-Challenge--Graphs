Describe the fixes/improvements you made to the Graph implementation here.

1.) Line 21 to 27 I added an if statement that makes sure that edges are actually existing edges. I also changed some parameters within the statement that
connexts the edges ```self.vertices[end].add(end)``` instead of add [end] to [end], for bi-directional you would add end to start. The same goes for before. It is not start to start, it would be start to end

 2.) From line 29 to 43 I changed vairbale names so it made more sense for me to understand. x is still our stack, y is changed to visited, and z is changed to current. And just had it append a node that wasnt the target to visited so we keep track of nodes we have already visited. And then when we find the target we return visited instead of the stack.

 3.) On your recursive method I just had it return the nodes that we have visited, and called ```self``` on the method   ``` graph_rec``` becuase you will need to use self to access itself.
