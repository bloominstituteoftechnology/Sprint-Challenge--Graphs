Describe the fixes/improvements you made to the Graph implementation here.

I have added code to `graph.add_vertex` so the method will throw an error if one or more of the edges points to a nonexistent vertex. I have also chosen to give a warning if the vertex already exists, a `UserWarning` will explain that the vertex has been overwritten - meaning all previous edges were deleted before adding the edges specified in the current method call.

I have added code to `graph.add_edge` to raise an error if one or more of the specified vertices does not exist. In addition, I have debugged the method to make sure edges go from `start` to `end` (and vice versa if `bidirectional=True`).

I have debugged `dfs` by ensuring we don't revisit vertices by adding the current vertex to the set of visited vertices and deleting those vertices before we add children to the queue. I have also renamed the variables to be more descriptive.

I have debugged `find_components` by changing line `if vertex in visited` to `if vertex not in visited`. Also changed `self.component` to `self.components` as specified in `__init__`.

Finally, I added doc strings to describe each method in `graph`.



!!!Forgot to write recursive version before first submission. It has been done now. Included base case by adding argument to keep track of visited vertices!!!
