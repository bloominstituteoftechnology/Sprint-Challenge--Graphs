Here are the fixes/improvements that I made to the Graph implementation:

---
## Depth-first Search
I began by changing the variable names in `dfs` to names that were more descriptive. (`stack` for the stack, `explored` for the set of explored vertices, `vertex` for the current vertex). 

As soon as I did that, it became obvious that all three of those variables were being "mixed up". `x` was used to represent the stack, and then later used to represent the vertex. `x` (the stack) was being returned at the end, when it should have returned the explored set. So I changed those around so that each variable was representing the right thing.

Next, I noticed that there was no check in place to make sure a vertex had not already been explored. I added line 33 `if vertex not in explored:` and indented the lines after it so that a vertex would be skipped over if it had already been explored.

After that condition, I also added the vertex to the explored set, so that it would not be explored again in the future (line 34). 

