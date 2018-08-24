Describe the fixes/improvements you made to the Graph implementation here.


### Hi Friend!!!

You've done a great job thus far on getting this far! Good work! I've implemented some changes so that you're able to see a graph on the screen when you execute the file in your python virtual environment. 

I've added some comments below to detail what changes I made, but the biggest thing I wanted to point out -- are variable names. Yes - it might not make a difference what variable names are called as long as you are consistent...BUT! future you or another developer like you who reads your code in the future will think it's more readable if you use variable names that are associated with what that variable is actually doing. 

You've done a really great job otherwise - your other files look great and I was able to run the demo file no problem after I corrected the graph.py file. 

Great job!

Sincerely,

Christina K. 
------------





# Draw.py
* adjusted name of _get_edge_indexes because my Latin is too strong to just let that one slide. :P 

* added doc strings to lines 57, 66, 81 to indicate what function was for

# Graph.py
* line 22 and line 24 - edges went from start to start and end to end. Wouldn't actually show any edges! Flipped the second set so each goes from start to end and end to start. 

* line 26 block: changed vars to be more in line with what you're doing here. Better to name vars with the intent that some one -- future, forgetful you -- a new developer, etc -- will be able to tell just from looking at the code at what's going on. 
* added a print statement in lieu of break statement on line 34. 

* line 33 - changed 'x' to visiting...if I went with convention on how I changed vars, it would have been stack...and that just didn't make sense for what I was doing here. 

* added '- visited' to line 35 to make the code work so that the stack extends properly

* line 39 looks like it is supposed to be a recursive but it's a guess if I'm going just off var name. Changed var name. 

* Line 40 changed x to visited.
Because visited is a set changed append to add in line 40 (along with var)

* if we are to call recursion, we need to use 'self' on the func name otherwise the linter will read it as a var

* line 44 changed x to visited

* added docstrings to funcs in graph.py