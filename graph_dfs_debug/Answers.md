Describe the fixes/improvements you made to the Graph implementation here.

- Got lines to draw by flipping start and end in the add section of the add_edge method

- Modified dfs to out put to y instead of x, x is the queue, y is the visited list. This fix combined with adding not to the visited in find_components allowed the color per matching group to work
