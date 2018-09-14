Describe the fixes/improvements you made to the Graph implementation here.

Nothing seems to connect, my edges aren't showing up.
    To get the edges to show up in graph.py you need `self.vertices[start].add(end)` instead of `self.vertices[start].add(start)`

All the vertexes are the same color. They're supposed to be different colors if they're not connected, and right now none of them are.
    On the find_components it was checking if it was in visited and you needed it so its if not in visited. That way it runs the functions and lets them all be same color except non connected nodes.

I keep losing track of my variables, I guess I should name them better?
    Changed:
    x to stack
    y to visited
    z to neighbor