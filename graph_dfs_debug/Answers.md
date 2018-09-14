Describe the fixes/improvements you made to the Graph implementation here.

It's always a good idea to have a `.gitignore` file that excludes things like `__pycache__` from being included in the repo.

Lint is a program that checks your code for potential errors. Python is a bit tricky to set up, so if you need help, message me and we'll get a zoom going.

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

graph_rec

- this looks like you're attempting a dfs via recursion
- meaningful variable names really help you (and me!) keep things straight when coding
- when doing recursion, have to keep track of our lists by calling them with each recursive iteration
- because we are passing in visited, we don't need `visted = set()`, rather let's append
- we also have to keep track of `path`
- check to see if we've hit the target
- let's change `v` to `child_vert`
- when calling `graph_rec` need to include `self`, that is, `self.graph_rec`

find_components

- we should be checking for vertices NOT in visited
