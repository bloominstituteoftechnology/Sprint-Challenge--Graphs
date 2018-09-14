# Fixes

I've made the following changes to `draw.py` and `graph.py`:

1. The connections were not showing up because the edges were pointing to themselves, so I've changed them to point to each other.

<!-- 
2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.
5. My editor sure is complaining a lot about something called "lint."
6. I keep losing track of my variables, I guess I should name them better? -->