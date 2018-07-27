Describe the fixes/improvements you made to the Graph implementation here.

1. `add_edge()` was making an edge `self.vertices[start].add(start)` and `self.vertices[end].add(end)` (should be start->end and end->start)
2. `find_components()` was using `visited` as `if vertex in visited:` – should be `if vertex not in visited:`
3. `dfs()` had variable names as `x`, `y`, `z` – change those to `stack`, `marked`, `current` respectively
4. `dfs()` was not even using the `marked` variable – which was supposed to prevent `dfs()` to not repeat vertices and only add non_marked vertices to the stack
5. `dfs()` was using the wrong condition to break out of the loop - `stack == target` – should be `if current == target:`
6. `dfs()` was returning the `stack` variable to `find_components()`, it needs to return the `marked` as we are interested in what vertices were visited in the search
7. If we want to use `graph_rec()`, then we need to pass around a set `visited` in the recursion, update it and return it – and use it to only make further recursive calls `if v not in visited:`
