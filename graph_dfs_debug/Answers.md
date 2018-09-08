Describe the fixes/improvements you made to the Graph implementation here.

in add_edge():
    1. add the end to start, and add the start to end to actually connect the components

in dfs():
    1. make variable names more descriptive
    2. change `if stack == target` to `if current == target`
    3. add current to the visited stack
    4. subtract visited when extending the stack to avoid repeats
    5. return the visited set because the stack will be empty at that point

in graph_rec():
    1. use "add" instead of "append" when adding to a set
    2. use "self.method" when calling a method within the same class
    3. make variable names more descriptive

in find_components():
    1. make sure the vertex is **not** in visited