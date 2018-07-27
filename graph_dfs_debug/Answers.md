Describe the fixes/improvements you made to the Graph implementation here.

BUGS in graph.py:

dfs()

1.  Bad vairable names in dfs. Changed to something more rediable.
2.  Potential infinity loop in dfs, it worth to check if a vertex was already visited. Changed.
3.  Allow run DFS with out passin gany argument. By default the 'start_vertex' will be '0'.

add_edges()

1.  If a vertex is not in the Graph, the implementation allow an inclusion of a new vertex without
    ussing the proper method for that (add-vertex()). I added some checks that return Exceptions is
    the vertex is not part of the Graph.
2.  Refactored variable names, now are a bit more rediable.

general:

1.  Messing types, str with int. Fixing all that in a defesing programming manner.

find_components() -> get_components()

1.  Make name more rediable: changed to get_components()
2.  Re-define the logic to track components. Added a new attribute to Graph so it holds and track the Sets of posible components.
