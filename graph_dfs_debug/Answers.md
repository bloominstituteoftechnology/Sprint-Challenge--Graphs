Describe the fixes/improvements you made to the Graph implementation here.

----draw.py------

1) removed 'from math import ceil, floor, sqrt' from the libraries section.

2) Line 34, changed 'list()' into 'set()' to preserve uniqueness.

3) Line 38 replaced the for loop with an appending of keys.

4) Line 57, changed 'num_colors' variable within the function to 'num_color' to cause less confusion.

5) Line 57, changed the 'or' statement into an if conditional statement.

6) Line 70 and 71, removed the '.label'.

7) Line 79, changed it to 'position' instead of (x_pos, y_pos).

8) Line 80,81. changed the inputs to position[0] and position[1] to specify x and y values.

9) Line 82, called a str() in the input to convert it to a string.

10) Line 98, removed .label.

11) Line 96, 'self.graph.vertices' instead of 'self.vertex_list'.


-----graph_demo.py-------

1) added the error message.


----graph.py------

1) added the hash bang.

2) Line 21-25, added Exception messages.

3) Line 28-29, raised Exception to specify if the Vertices are in the graph or nonexistent

4) Line 30 and 32, switched end and begin inputs

5) Changed x variable in dfs to 'stack',
removed append statement of start and inserted it directly inside the list,
changed y variable to 'visited',
changed z to 'current',
added 'visited.add(current)'' to signify the nodes visited,
return visited nodes.

6) graph_rec function edited
