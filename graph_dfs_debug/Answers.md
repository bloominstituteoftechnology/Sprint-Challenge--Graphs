# Fixes

I've made the following changes to your files:

1. The connections were not showing up because the edges were pointing to themselves, so I've changed them to point to each other.

5. The "lint" messages are coming up due to your code not conforming to style and structure conventions that make your code easier to read and less prone to errors.

6. I have changed values like `x` and `y` into more descriptive names so you do not lose track of variables.

<!-- 
2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.-->