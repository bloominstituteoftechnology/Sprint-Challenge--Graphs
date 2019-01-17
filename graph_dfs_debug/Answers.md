Describe the fixes/improvements you made to the Graph implementation here.


1. Nothing seems to connect, my edges aren't showing up.

Addressing the issues in graph.py fixed this issue. I'm not sure exactly what it 
was. One possibility was that in the add_edge method you were adding the vertice's self to its edges list instead of the other vertices that we want to add to its edges list. I'll leave up a closer investigation of what fixed this issue to you. 

2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

In the find_components method, vertices weren't being added to the visited set.
The set stayed empty, hence the uniform colors regardless if a vertex is connected
or not. 

3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.

I'm not sure about this. It seems to run fine with the code as it is now. 

4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.

Please see the comments I made in the code for the dfs and graph_rec method.

5. My editor sure is complaining a lot about something called "lint."

Hmmm. The linter serves to highlight syntactical and stylistic errors in your code. Are you sure that the python linter is turned on? In VSCode, you have to add the pylint extension and then activate it for the python linter to work. Can you check if a similar extension is available for the code editor that you're using. 

6. I keep losing track of my variables, I guess I should name them better?

Yes. See the comments I made throughout graph.py.