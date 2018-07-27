Here are the fixes/improvements that I made to the Graph implementation:

---
## Depth-first Search
I began by changing the variable names in `dfs` to names that were more descriptive. (`stack` for the stack, `explored` for the set of explored vertices, `vertex` for the current vertex). 

As soon as I did that, it became obvious that all three of those variables were being "mixed up". `x` was used to represent the stack, and then later used to represent the vertex. `x` (the stack) was being returned at the end, when it should have returned the explored set. So I changed those around so that each variable was representing the right thing.

Next, I noticed that there was no check in place to make sure a vertex had not already been explored. I added line 33 `if vertex not in explored:` and indented the lines after it so that a vertex would be skipped over if it had already been explored.

After that condition, I also added the vertex to the explored set, so that it would not be explored again in the future (line 34). 

## Recursive Implementation
Again, I started by changing variable names so that it would be easier to keep track of the logic. I used the same names as I used in `dfs`.

I changed `x` to `explored` and I noticed that it was initialized as a set, but then `.append()` is called on it (line 42). The `.append` method is for lists; the equivalent for a set is `.add()`.

Then I noticed that the linter was "complaining" about the recursive call on line 44. It said "undefined variable 'graph_rec'." This is because `graph_rec` is a method of the Graph object. When it is called inside of the Graph, it needs to be called on `self`; i.e: `self.graph_rec()`

Next, I added a condition on line 44 to again check the explored set before doing anything with a vertex. Without this condition, the function will run forever if given a component that has a cycle.

The last step was to update the explored set with the result of the recursive call (line 45). I added some tests to the main function to make sure `bfs` and `graph_rec` were working correctly.