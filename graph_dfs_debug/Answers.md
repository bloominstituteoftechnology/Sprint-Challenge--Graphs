Describe the fixes/improvements you made to the Graph implementation here.
* Switch `start` and `end` argument for `add_edge` method in `graph.py`
* Changed variable names in `dfs` method for better readability. Also the logic was messed up so it needed to be fixed/
* In `find_component` method, change to `if vertex not in visited`
* `dfs` method should now find the target vertex.
* Install pylint to fix the linting probles
* In `graph_demo.py`, add `if vertices[1] not in graph.vertices[vertices[0]] and vertices[0] not in graph.vertices[vertices[1]]:` to check if edge already exists