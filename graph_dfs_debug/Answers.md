Describe the fixes/improvements you made to the Graph implementation here.
graph.py

changed from start to start and end to end to start to end and end to start on lines 22 & 24

changed x to stack
changed y to visited
changed z to current

on line 34, changed to print statement for clarity

to graph_rec, I added visited.add(start) and added self.graph_rec(v) so it would recurse within the function. 