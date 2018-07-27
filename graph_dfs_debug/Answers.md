Describe the fixes/improvements you made to the Graph implementation here.

Hola Friend,

I think so far your doing a great job with learning BFS. I go into futher details on the changes I made in the ansers.md file and you can now see a graph when it runs! How cool is that?

The one thing I want to mention is about variable naming. I try to label variable as close to what there doing. So instead of just using "x" think about what "x" is. Is "x" a stack or quece? Then you should name "x", stack just so its more clear what "x" is. This also helps when your working with a bunch of people and a new devloper clearity and simplisty are key.

Otherwise everything looks good my friend and the graph_demo runs like a well oiled machine! Good work!

Always here if you need me,

Max Washington

# Graph.py

* Changed line 22 - 24. add_edge had the edgeings going from start to start and the end to end. Changed that to start to end and end to start.

* Line 27 changed x to stack so its a bit more clear what is it.

* Line 29 changed y to visited also for clearity.

* line 32 changed 'z' to visiting

* Line 34 changed block statement into a print statement just so I have a better idea whats going on.  

* line 40 - 44 changed all the x vars into visited for better description. If we are to call recursion, we need to use 'self' on the func name otherwise the linter will read it as a var

#Draw.py

* Line 39 Added labels to display the index of each node.
