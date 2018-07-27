Describe the fixes/improvements you made to the Graph implementation here.

This: https://help.github.com/articles/comparing-commits-across-time/

1. In the Graph.add_vertex fuction you are adding self connecting edges. You need to switch the add calls.
2. You needed to return the set of nodes you visited. Not the empty list of nodes the algorithm needed to visit.
3. If the graph is a cyclic graph, has a loop in it, you just follow that loop forever. You need to remove vertices you already visited with set differencing.
4. Here you are checking for equality against all the vertices you are planning to visit, not the current vertex. I changed to check against current_vertex (formerly z)
5. Its a style thing, you're editor should tell you what to do about each one.