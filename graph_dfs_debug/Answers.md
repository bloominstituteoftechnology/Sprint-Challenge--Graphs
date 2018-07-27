Describe the fixes/improvements you made to the Graph implementation here.
1. add check in add_edge for attempts to add edge to nonexistent vertices.
2. fix code in add_edge to connect egde to desired vertex.
3. fix dfs - chnage line 35 to 'if Z == target'
4. fix graph_rec - change 'append' to 'add' for approriate set operation, add 'self.' to class methond call in line 45.
5. dfs should return 'y' - the visited vertices, not x which will be empty. also use y to keep track of already visited vertices by set subtracting when extending in line 37 and adding current item to visited set.
6. line 53 - should be 'not in visited'
7. make variables in dfs descriptive of what they are refrencing.