Describe the fixes/improvements you made to the Graph implementation here.

## Dept-first search bug fixes
Skimming through the implementation of `dfs`, I noticed variable `x` was being used in multiple instances, so I started out by changing that.
I also noticed that naming of variables was not descriptive, so I named them appropriately.
There was not a statement to check if a vertex exists and/or whether or not it has been visited, so fixed that.
Lastly, `x` which would contain potential vertices to be visited was being returned instead of an actually visited set of vertices. I changed it so that it returns the visited vertices.

