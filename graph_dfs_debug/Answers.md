Describe the fixes/improvements you made to the Graph implementation here.

1. Fixed add_edge method so that edges will be rendered on the graph. In line 36, changed the value of .add(start) to .add(end). In line 38, changed the value of .add(end) to .add(start)

2. When running "python graph_demo.py", all of the vertices share the same color. So I entered values for vertices and edges.

3. Running "python graph_demo.py" did not "take forever" as the friend described. Its runtime was normal (it rendered the graph immediately after running the command). 

4. In the while loop under the dfs method, changed "break" to "return target".

5. Changed x, y, and z variables into more descriptive and proper names, namely "stack", "visited", and "current" respectively. Refactored existing code and added new code.

