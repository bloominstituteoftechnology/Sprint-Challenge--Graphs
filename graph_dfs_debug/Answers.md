Describe the fixes/improvements you made to the Graph implementation here.

1.  add_edge: fixed it so edges added are start -> end (and end -> start) instead of start -> start_indices
2.  Changes to dfs: changed variable names to clarify what's going on. Visited is initialized to an empty set rather than starting with start. Added if statement to check if the current node hasn't been visited and add children nodes if true. Changed return statements to vary depending on whether there is a target
3.  In find_components changed if to check for vertex not in visited
4.  Reformatted to comply with pep8 standards
5.  In graph_rec rewrote the function to work with recursion
