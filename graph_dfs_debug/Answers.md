Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seems to connect, my edges aren't showing up.

The bug is in the add_edge function of the Graph class. First we must check to see if we have a starting or ending node. If we already have the starting node, we don't need to add the start again, but the ending node instead. Likewise if the edge is Bidirectional, we would already then have the ending node, so we add the starting node to point the edge in the other direction as well.

2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

In the find_components function, you need to check for the components that have not yet been visited, that way it updates all of the components that have been to the same color. 

* You will also need to refactor the dfs, as making this change will cause your hang up in problem 3 (had to restart my frozen computer 4 times before realizing)

3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.

This is because the dfs is running an infinite while loop and must be refactored. We use queues for breadth first searches and stacks for depth first, so we append all of our starting nodes to an empty stack. we then have to pop() a node from the stack and add it to the list of visited nodes. If the current node however has not been visited, we move on to the next node and append to the stack. The unvisited node is given a different color (pointing to find_components function)

* 4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.

in the dfs_rec function, we run dfs until we find the target, then run dfs from the target vertex and add all visited vertices to the empty set.  We then return the visited target vertex and it's children


* 5. My editor sure is complaining a lot about something called "lint."

Linting highlights syntactical and stylistic errors in your python code. Variable naming and spacing has been changed to make sure these errors no longer appear when we run our code.

6. I keep losing track of my variables, I guess I should name them better?

To name them better, instead of x, y, v, and z we can use names like visited, stack, and other_vertex for vertices not visited.

7. I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck. It was running forever so I tried adding a thing to keep
track of vertices, and now I just get an error message. Please try to fix this
too if you can, or at least give me some pointers on what I should be doing.

Instead of using a stack we can just add all visited vertices to an empty set. then running dfs on all of the other vertices not visited.
