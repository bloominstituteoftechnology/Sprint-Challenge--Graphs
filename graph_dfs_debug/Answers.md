Describe the fixes/improvements you made to the Graph implementation here.

1. graph.py - Graph class - add_edge: Changed add_edge class. Displaying random edges. Adding edges to components.

2. graph.py - Graph class - dfs: Edited the current code. Changed variable names to cur_node, stack, and visited.

3. graph.py - Graph class - graph_rec: graph_rec(v) to self.graph_rec(v). Changed append to add.

4. draw.py - Changed default parameters to true (show_grid, show, axis, draw_components). Now, axis, grid and other components are displaying.

5. graph.py - Graph class - find_components: 'if vertex in visited' to 'if vertex not in visited'. The if statement would not run because the visited set won't have any elements in the beginning.

