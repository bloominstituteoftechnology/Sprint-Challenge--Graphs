Describe the fixes/improvements you made to the Graph implementation here.

It's always a good idea to have a `.gitignore` file that excludes things like `__pycache__` from being included in the repo.

The first pass of going through your class, going from top to bottom, here are some thoughts.

add_vertex

- When adding a vertex, make sure the vertex being added doesn't already exist.
- make sure the edges connect to vertices that do exist

add_edge

- make sure the edges connect to vertices that do exist
- start was connecting to start and end was connecting to end - not much of an edge:), so connect start to end and end to start

dfs

- `x` is a confusing variable name for the stack, so I changed it to stack
- `y = set(stack)` should be set([start]), and y is a confusing name, let's call it visited
- `z` is a confusing variable name, so I changed it to current_vert
- instead of checking if `stack == target`, we should check the current vert
- you have to remove the visited verts from this set `stack.extend(self.vertices[current_vert])`
- instead of returning `stack` at the end, should return `visited`
