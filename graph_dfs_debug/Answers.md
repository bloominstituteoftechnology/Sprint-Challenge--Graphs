Describe the fixes/improvements you made to the Graph implementation here.

Fixed a few syntax errors with the graph

The vertices need opposite directions to connect with other vertex

Completely redid dfs instead of refactoring, Used a stack class to implement

Refactored rec to use better variables and self was missing for the recursion call

find_components was missing 'not', to be able to run dfs if vertex not in visited

