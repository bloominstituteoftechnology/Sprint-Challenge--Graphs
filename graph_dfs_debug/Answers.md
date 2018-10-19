Describe the fixes/improvements you made to the Graph implementation here.
graph.py:

dfs()

1.  Clearer variablenames in dfs. Changed to something more readable.
2.  Potential infinity loop in dfs,  check if a vertex was already visited. Changed.
3.  Allow DFS to run with out passing any argument. By default the 'start_vertex' will be '0'.

add_edges()

1.  If a vertex is not in the Graph, the implementation allowed for the inclusion of a new vertex without using the proper method for that (add-vertex()).
Checks for return Exceptions if the vertex is not part of the Graph.
2.  Refactored variable names.

general:

1.  Mixing data types, e.g. str with int.

find_components() -> get_components()

1.  Make name more readable: changed to get_components()
2.  Re-define the logic to track components. Added a new attribute to Graph so it holds and tracks the Sets of posible components.

BUGS isn draw.py:

1.  Several Bugs fixed: due to the new implementation done, fix references to new properties,as well to change the calls to methods with new names
2. get_connected_component_colors(), redone overall
    