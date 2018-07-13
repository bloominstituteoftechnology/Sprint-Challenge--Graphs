Describe the fixes you made to the Graph implementation here.

1.  changed canvas size to view all nodes
2.  gave canvas and buttons simple styling
3.  changed vertexes to have fill color that matches their color property
4.  randomize button had an incorrect onClick handler
5.  dfs() function was removing 2 nodes from the stack in one while loop iteration, causing the graph to draw "crazily". Removed the erroneous shift()statement.
