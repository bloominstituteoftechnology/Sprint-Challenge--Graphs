
# General Fixes

Nothing seems to connect, my edges aren't showing up.
- 

All the vertexes are the same color. They're supposed to be different colors if they're not connected, and right now none of them are.
- although the method _get_random_colors exists and it is a part of the child function, however in the main class (BokehGraph) is False on default and therefore the graphs are being rendered with the vertices of the same colour. 

Sometimes I do something and when I run python graph_demo.py it just takes forever, even though my draw.py and graph_demo.py are totally just the same as from class.
- this may be most commonly caused by running an infinite loop or by using an inefficient algorithm that needs to process large datasets.

I wanted to let it find a target vertex, but even back when it did kinda run this part didn't really work.
- 

My editor sure is complaining a lot about something called "lint."
- lint is a function that checks the python code for programming and style errors and highlights them. 

I keep losing track of my variables, I guess I should name them better?
- the best way is to use descriptive names for each of the variables, which greatly improves the readability of the code. 

## I. graph_demo.py Fixes and Improvements



## I. draw.py Fixes and Improvements

BokehGraph Class:
[line 15] A recommendation I would make here is to increase the graph size from 100px X 100px to improve legibility.



## I. graph.py Fixes and Improvements

