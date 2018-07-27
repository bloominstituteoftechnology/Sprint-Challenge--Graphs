Describe the fixes/improvements you made to the Graph implementation here.

Dear Sugar-Bear,

Here're some changes:

### Line 21: add_edge method;
1. Edges need to connect between two vertices - start has to connect to end and vice versa for bidirectional.

### Line 26: dfs method;
1. Rename the variables to be more descriptive and consistency (I used )  As we work on DFS, using word stack makes more sense.  And I use 'visited' for the vertex that is already checked or 'current' for the vertex that pop out and is being checked.

2. I also add `visited.add(current)` in dfs. Once the vertex is checked, it needs to be added in visited stack.

### Line 44: graph_rec method;
1. Rename the variable
2. I change the method from `.append()` to be `.add()` because it's initialized as a set.  Both work the same but `.append` is for a list and `.add()` is for a set. 
3. When invoke method in the same class, need to call `self.method` (line 48).

### Line 53: find_components;
1. Add `not` for checking condition. We want to check the vertex that have NOT been vistied. 

I also add comments in the file where I changed the code so it'd be eaiser to understand later :)

Cheers,
xxx
