Describe the fixes/improvements you made to the Graph implementation here.

Nothing seems to connect, my edges aren't showing up.

    In graph.py in def add_edge, 'self.vertices[start].add(start)' should be changed to 'self.vertices[start].add(end)' because we want to connect one node to another, not itself. If we want a node to be bidirectional, we want 
    'self.vertices[end].add(end)' to be 'self.vertices[end].add(start)'.


All the vertexes are the same color. They're supposed to be different colors if they're not connected, and right now none of them are.

    In graph_demo.py in def main, we want to switch draw_components to False because there is a check in draw.py on line 41 to call a function to randomize the colors if draw_components is False.


Sometimes I do something and when I run python graph_demo.py it just takes forever, even though my draw.py and graph_demo.py are totally just the same as from class.

    Debugging graph fixed it.


I wanted to let it find a target vertex, but even back when it did kinda run this part didn't really work.

    Added check in graph_rec

My editor sure is complaining a lot about something called "lint."

    Go to File > Preferences > Settings > Python > Linting: Enabled
    Then uncheck the box.

I keep losing track of my variables, I guess I should name them better?

    Make the variables more descriptive. For dfs, changed x to stack, y to visited, and z to current. For graph_rec, changed x to visited and v to child_vert.