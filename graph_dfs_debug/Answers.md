Describe the fixes/improvements you made to the Graph implementation here.

6. I keep losing track of my variables, I guess I should name them better?
**Changed variables in dfs

1. Nothing seems to connect, my edges aren't showing up.
**Fixed add_edge method. The way the method was set up it was creating an edge with the same vertex on both sides of the connection. I fixed it to now have a starting vert and a separate ending vert for both unidirectional and bidirectional edges.

2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
**To fix the dfs method I first removed "stack" from the set() module because it should be empty upon intialization (because no nodes have been visited yet). I added a line `visited.add(current)` in order to add the popped vertex into the visited list, and modified the next line to `stack.extend(self.vertices[current] - visited)` in order to update the stack. Also, rather than returning the stack we need to return a list of the verts and the order in which they were visited.
**I also modified the find_components method to visit vertices that have NOT yet been visited.