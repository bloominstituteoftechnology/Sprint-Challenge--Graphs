Describe the fixes/improvements you made to the Graph implementation here.

## Dept-first search bug fixes
Skimming through the implementation of `dfs`, I noticed variable `x` was being used in multiple instances, so I started out by changing that.
I also noticed that naming of variables was not descriptive, so I named them appropriately.
There was not a statement to check if a vertex exists and/or whether or not it has been visited, so fixed that.
Lastly, `x` which would contain potential vertices to be visited was being returned instead of an actually visited set of vertices. I changed it so that it returns the visited vertices.

## Recursive Implementation
I started by changing variable names for appropriate logic usage. Names are similar to that of`dfs`.

I changed `x` to `visited` and I noticed that it was initialized as a set, so changed `append` to `.add()` which is the appropriate method for set.

I noticed `graph_rec` was being called recursively as a non-class method, so I changed it to include `self` to it in order to use it apppropriately.

Lastly, I updated `visited` which contains result of the recursive call. I added some tests to the main function to make sure `bfs` and `graph_rec` were working correctly.