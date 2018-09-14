Describe the fixes/improvements you made to the Graph implementation here.


Hi Friend!
I was able to review your graph_dfs files and I think I can help. Let's go over the Issues list that you provided and find out what's going on.

ISSUES LOG:
1. Nothing seems to connect, my edges aren't showing up.
	If you look at your graph.py / def_add_edges function, it seems that vertices begins at "start", but connects to "start". Also, your bidirectional if statement says "end" to "end".  I changed it to say the following:

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start) //change to self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start) // self.vertices[end].add(start)
********************************************************

2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

 In graph.py /

 def dfs - rewrote the method with easier variable names that are readable.

 def find_components, vertex was not in visited.  Add "not" to the if statement "if vertex in visited" to make it say "if vertex not in visited".



*********************************************************
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.

I'm not sure what's happening.  In terminal, when I run 'python3 graph_demo.py #edges #vertices' and it seems that I'm fine to draw a graph quickly.  Maybe adding too many #vertices(100)/#edges(100) may make it run forever?

*********************************************************
4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.

In graph.py / def dfs, since dfs are like stacks it was easier to change 'x' to be named 'stack' since we're doing a depth-first search, renamed 'y' to be 'visited', which are vertices that been checked during the search, and renamed 'z' to be 'current' which temporarily holds the vertex(nodes) that we pop from the stack for because its searching.  The reason why I was chose to rename it that it helped me understand whats happening in dfs code (since its a stack the renaming could help understand who are the players) and potentially help again in future state if we need to go back and review the code again.

Next, I checked out the while loop. Rewrote def graph_rec recursion method to find target.


 *************************************************************
 5. My editor sure is complaining a lot about something called "lint."

 I'm not sure how to really give a good answer.  I have pylint in my editor and it works fine.  Maybe you can check the linter and see what's having with the linting behavior and then modify its setting?

 *************************************************************

6. I keep losing track of my variables, I guess I should name them better? I also tried to do it with recursion instead of a stack, in `graph_rec`, but I got even more stuck. It was running forever so I tried adding a thing to keep track of vertices, and now I just get an error message.

In graph.py / def graph_rec and def dfs,  fixed the names of the dfs.














