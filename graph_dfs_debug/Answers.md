Describe the fixes/improvements you made to the Graph implementation here.

add_edge

Edges are not showing because start and end verticies are pointing themselves. I switched them so start is pointing end and vice-versa.

DFS

-Variables were poorly named. After naming them properly, I also notices that they were all mixed up. It wasnt returning the collections which was supposed to be called 'stack' so I return the 'visited' set which was originally called some letter.

Also,while loop didnt check if the current vertex had been visited or not so I added an if statement to check that (if vertex not in visited). When we extend stack, we need to remove the items we already visited on line 37.

Line 29, 'visited' set should be empty, otherwise it will interfere with the condition in line 33.

find_components

On line 45, it should be 'if vertex <<<not>>> in visited' so we can implement dfs on the vertex if it wasnt visited.

graph_rec

-x was named poorly, I changed it to 'visited'.

-append is for lists, however, 'visited' is a set so, chenged it to add().

-line 44, I added a condition that if target is our start point, it should stop and return the visited set.

-line 46, I renamed 'v' to 'vertex' to clarify what we are iterating. Inside that for loop, I added a condition(vertex not in visited). Otherwise, it would be infinite loop and break.
Also, since graph_rec is method that belongst the Graph class, it should be called as 'self.graph_rec'