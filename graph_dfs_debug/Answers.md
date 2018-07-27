Describe the fixes/improvements you made to the Graph implementation here.
1. add check in add_edge for attempts to add edge to nonexistent vertices.
2. fix code in add_edge to connect egde to desired vertex.
3. fix dfs - chnage line 35 to 'if Z == target'
4. fix graph_rec - change 'append' to 'add' for approriate set operation, add 'self.' to class methond call in line 45.