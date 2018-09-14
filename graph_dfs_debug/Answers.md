Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seems to connect, my edges aren't showing up.

Changed add_edge() to connect "start" to "end".

2. All the vertexes are the same color. They're supposed to be different colors
   if they're not connected, and right now none of them are.

Changed "if vertex in visited:" to "if vertex not in visited:" in find_components() so that it is same-colors for vertices in connected components.

3. Sometimes I do something and when I run `python graph_demo.py` it just takes
   forever, even though my `draw.py` and `graph_demo.py` are totally just the same
   as from class.

Commented out graph_rec()?

4. I wanted to let it find a target vertex, but even back when it did kinda run
   this part didn't really work.

Improved dfs() to actually traverse entire graph.

5. My editor sure is complaining a lot about something called "lint."

It sure is...

6. I keep losing track of my variables, I guess I should name them better?

In dfs(): x -> search, y -> searched, z -> selected
