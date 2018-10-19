Describe the fixes/improvements you made to the Graph implementation here.

- disable pylint
- change `self.vertices[start].add(start)` to `self.vertices[start].add(end)` in `add_edge()`
- change variable names in `dfs()` to be more descriptive
- change `if vertex in visited:` to `if vertex not in visited:` in `find_components()`
- change `x.append()` to `x.add()` in `graph_rec()`