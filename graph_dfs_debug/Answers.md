Describe the fixes/improvements you made to the Graph implementation here.
1. Edges weren't connecting. You had vertices connecting to themselves rather than to other
vertices. I changed self.vertices[start].add(start) on line 22 to self.vertices[start].add(end)
and you did the same thing for bidirectional connections so I changed self.vertices[end].add(end)
on line 24  to self.vertices[end].add(start)

2. All the vertices are the same color, they're supposed to be different colors
if they're not connected. The issue is with the draw_components boolean in your
graph_demo.py file. It comes from your BokehGraph in draw.py and you have it set
up so that when it's true the edges will be the same color and when it's false they
will be differnt colors. When the components are not connected i.e. there are no
edges they should be different colors so you'll need draw_components set to false if there
are no edges and true if edges do exist. I have made this change in your logic
by adding an if statement to lines 26 and 27 of graph_demo.py but a further
update may be needed to make sure only connected components change color.

3. "Wanted to find a target vertex." Both the stack version and the recursive
versions are working now. In the recursive version you were missing a base case
that would cause your recursion to stop and you were implementing the visited list
in an ineffective way, I you tried to use append with set() which is not allowed
and you did not pass in your visited list into your recursive function (or the
default function for that matter). As another point, yes you should consider naming
your variables more descriptively, x,y and z are not telling me anything about
what each variable means I have added more descriptive names and have also renamed
your recursive dfs function to rec_dfs to make it's purpose more clear.

4. graph_demo.py takes forever to run. I did not have that issue but I may have
fixed a typo before running it initially, I will check in a few. 
