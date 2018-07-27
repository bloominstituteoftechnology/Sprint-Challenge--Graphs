Describe the fixes/improvements you made to the Graph implementation here.

Graph_DFS_DEBUG

1.  Edges did not show up because line 22 and 24 in graph.py were adding an edge from start to start and not start to end (and vice-versa).

2.  In the dfs method variable names were made more descriptive; line 36 of graph.py was corrected to from 'if x == target:' to 'if current == target'.

3.  In the graph_rec method made the variable names more descriptive; line 48 of graph.py added self to the beginning of graph_rec(vertex)

4.  In the find_components method, line 56 of graph.py was corrected to read "if vertex 'not' in visited".
