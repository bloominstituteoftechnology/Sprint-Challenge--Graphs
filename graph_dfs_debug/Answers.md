Describe the fixes/improvements you made to the Graph implementation here.

add_edge

Edges are not showing because start and end verticies are pointing themselves. I switched them so start is pointing end and vice-versa.

DFS

-Variables were poorly named. After naming them properly, I also notices that they were all mixed up. It wasnt returning the collections which was supposed to be called 'stack' so I return the 'visited' set which was originally called some letter.

Also while loop didnt check if the curretn vertex had been visited or not so I added an if statement to check that (if vertex not in visited).

find_components

On line 45, it should be 'if vertex <<<not>>> in visited' so we can implement dfs on the vertex if it wasnt visited.

