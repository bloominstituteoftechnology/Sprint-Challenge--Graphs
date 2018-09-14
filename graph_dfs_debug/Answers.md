Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seemed to connect: I changed up the add_edge function to add some constraints.
2. All the vertexes are the same color: A few things wrong here, first, on graph_demo, I added constraints so that it forces the user to put in numbers for the vertexes and edges, and yes or no to draw_components. Second, I changed your find_components function to say `if vertex NOT in visited.
3. ???
4. Changed it to check target value.
5. A variable in graph_rec was trying to add to a set, so had to change that.
6. The DFS and graph_rec had variables like x and y, I changed it to be more clear.
