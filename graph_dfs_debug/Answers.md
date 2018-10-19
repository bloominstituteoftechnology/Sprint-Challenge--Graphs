Describe the fixes/improvements you made to the Graph implementation here.
--------------------------------------------------------------------------------------------
graph.py
---------
def graph_rec:

1) changed x to [] (was set())
2) change recursion call to SELF.graph_rec(v) (was missing self.)

def add_edge:

1) should add end to start, not start to start
2) if it's bidirectional, should point end back to start, not end to end

def dfs:

1) rewrote dfs using a stack. 

def find_components:

1) you would want to find vertex that is NOT in visited, then call dfs recursively.

---------
graph_demo.py
---------

def main:

1) check if both vertices are not in each other's edges(graph.vertices[vertex]) before adding the edge.

---------
draw.py
---------

def randomize:

1) restructured function to create a random coordinate and store it in a set. only add coordinate to the vertex if the coordinate is not in occupied.