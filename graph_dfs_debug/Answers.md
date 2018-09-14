Describe the fixes/improvements you made to the Graph implementation here.

6. I keep losing track of my variables, I guess I should name them better?
**Changed variables in dfs

1. Nothing seems to connect, my edges aren't showing up.
**Fixed add_edge method. The way the method was set up it was creating an edge with the same vertex on both sides of the connection. I fixed it to now have a starting vert and a separate ending vert for both unidirectional and bidirectional edges.