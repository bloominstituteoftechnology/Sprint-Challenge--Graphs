Describe the fixes/improvements you made to the Graph implementation here.


1. Nothing seems to connect, my edges aren't showing up.

Addressing the issues in graph.py fixed this issue. I'm not sure exactly what it 
was. I'll leave that up to you to figure out. 

2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

In the find_components method, vertices weren't being added to the visited set.
The set stayed empty, hence the uniform colors regardless if a vertex is connected
or not. 

3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.

4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.


5. My editor sure is complaining a lot about something called "lint."

6. I keep losing track of my variables, I guess I should name them better?

Yes. 



1) In add_edge method, you were adding the vertice's self to its edges list, instead
of the other vertex we want to add to its edges list. 
