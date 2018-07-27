# Help!

Hi Friend,

After learning about breadth-first-search, I decided to give depth-first-search
a try.  I'm pretty sure I've almost got it working, but I can't figure out the
last few bugs.  Can you help?  I've got the following issues.  I'm not sure if
the order here matters, you might have to fix them in a different order than
they are listed. I think these are all problems with `graph.py`.

1. Nothing seems to connect, my edges aren't showing up.
R// fixed with as shown on the comments on the file Answers.md
2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.
R// on graph_demo.py there you have this line:
def main(num_vertices=8, num_edges=8, draw_components=True):
but the variable draw_components should have a value of 0 or 1 so you can change it like this and that will show your colors correctly:
def main(num_vertices=8, num_edges=8, draw_components=0):
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
R// the file graph.py has some differences to the one made in class, some of those differences make some proceses slower, for instance adding new edges or adding a vertex. I corrected and documented them on your code:

also the graph_rec function does not seem to be used on your code, though it is not the cause for your code to be running slow (taking forever).

4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.
R// your dfs function had an error, I documented it on the graph.py file, what happened is it lacked this line visited.add(current) so even if ir was running, it was never returning the target vertex when it found it.
5. My editor sure is complaining a lot about something called "lint."
editor usually have a linter it helps you a lot about possible mistakes you make while writing code
6. I keep losing track of my variables, I guess I should name them better?
R// yes, you are correct, I changed the name of some variables on your dfs code on the graph.py file
I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck. It was running forever so I tried adding a thing to keep
track of vertices, and now I just get an error message. Please try to fix this
too if you can, or at least give me some pointers on what I should be doing.
R// oh, so that is what you where using graph_rec for... I made some changes on graph.py I think that will work.
I'm still trying to learn this stuff, so please don't just fix the code for me.
Let me know in the `Answers.md` file where my bugs are and what you did to fix
them, so I can have an easier time watching out for them next time. Oh and don't
forget to `pipenv install` and `pipenv shell`!

If you get all this figured out, it'd be great if you could also help try to
improve the `randomize()` in `BokehGraph` so I can draw vertices that don't
overlap (*i.e. stretch goal*).
R// I improved the ramdomize so instead of assigning random locations it locates each vertex on some kind of zig zag so their edges dont overlap too much, check it out on your code.
Thanks!
