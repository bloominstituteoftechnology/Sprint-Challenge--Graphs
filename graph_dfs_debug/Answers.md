Describe the fixes/improvements you made to the Graph implementation here.

### `Graph.add_edge`
- Fix set from adding start to itself. Now connects to end
- Vice versa for bidrectional as well
Graph should now properly display edges

### `Graph.dfs`
- Refactor variables to meaningful names
- Line 32 was comparing if stack was equal to target, when we want to compare current node
- Insert new line at 35 and make sure we are adding current node to visited set
- line 36 tweak stack extend to remove visited nodes from stack
- line 38 must return visted nodes instead of empty stack

### `Graph.graph_rec`
- Erase line 42 `x.append` Cannot append to set, just initialize with `set(start)`
- Recursive function has no base cases, them
- Give variables meaningful names
- Recursive call must be called with `self`

### `Graph.find_components1`
- We want to check if the vertex has not been visited otherwise components will not be colored