# Help!

Hi Friend,

After learning about breadth-first-search, I decided to give depth-first-search
a try.  I'm pretty sure I've almost got it working, but I can't figure out the
last few bugs.  Can you help?  I've got the following issues.  I'm not sure if
the order here matters, you might have to fix them in a different order than
they are listed. I think these are all problems with `graph.py`.

1. Nothing seems to connect, my edges aren't showing up.

The reason nothing is connecting, because your vertices have cycles or connecting to themselves. Lines 22 and 24 had to be changed. self.vertices[start] is a key in Graph's dictionary. Its value is a set that contains all other naighbors it has edges with. 
In line 22 - self.vertices[start].add(start)
In line 24 - self.vertices[end].add(end)
That is just connecting to themselves. You can't just say for vertices start add vertice start and the same goes for the end in line 24. For the future reference, don't coonect edges to themselves or you will get the same problem 'nothing seems to connect' :D :D :D 


2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

It looks like there were some none functioning methods in graph.py.

In dfs starting line 26:
    a) Variable names are totally messed up, returning totally wrong values that not connecting to anything. So now returning visited that returns all vertices traversed starting from start vertex.
    b) Added '- visited' in stack.extend on line 36. It avoids duplicate adds, means not adding visited vertices to the stack.
    c) Also added visited to the visited stack to avoid duplicate checking if vertices are already checked.
In find_components, starting line 47:
    a) Changed 'if vertex in visited' to 'if vertex not in visited'. The original line never visited any vertices, even for the firast time. The updated code of this line ensures we never visit vertices that are already visited.




3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.

I didn't get this issue while testing. I guess this issue was fixed with all other issues. Have a feeling there was an infinite loop somewhere not letting the program to execute.


4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.

The reason was on line 34. It was breaking the while loop. Changed if condition in dfs to return found match instead of 'break'. 



5. My editor sure is complaining a lot about something called "lint."

'Lint' is checking for the typing mistakes. Also makes sure that your code is up to the standards and conventions that helps other developers read your code easier.

Not quiet sure what was that graph_rec for. ouldn't even find it on google. So deleted it. 


6. I keep losing track of my variables, I guess I should name them better?

Starting from line 26 in dfs:
    Changed the variable names to be more understadable and easier to read. Using stack, keeping track of current_vertex and keeping track of visited vertices. Make sure it is named so others can understand what the function or a method does or intend to do.

I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck. It was running forever so I tried adding a thing to keep
track of vertices, and now I just get an error message. Please try to fix this
too if you can, or at least give me some pointers on what I should be doing.

I'm still trying to learn this stuff, so please don't just fix the code for me.
Let me know in the `Answers.md` file where my bugs are and what you did to fix
them, so I can have an easier time watching out for them next time. Oh and don't
forget to `pipenv install` and `pipenv shell`!

If you get all this figured out, it'd be great if you could also help try to
improve the `randomize()` in `BokehGraph` so I can draw vertices that don't
overlap (*i.e. stretch goal*).

Thanks!
