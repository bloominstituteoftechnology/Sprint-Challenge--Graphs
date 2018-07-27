Describe the fixes/improvements you made to the Graph implementation here.

1.  In `add_edge`, `self.vertices[start].add(start)` must be `self.vertices[start].add(end)` and visa versa since you want the edge to go from one vertex to another, not from itself back to itself.

2.  In `dfs` use more descriptive variable names such as "queue", "visited", etc.
    You can also initialize a list with the first element already in it, so you don't have to write another line to append it.
    Don't forget to add nodes to the `visited` list so you don't look at them again.

3.  In `graph_rec` you want your visited list outside of the function, otherwise, every time you call the it, you'll get an empty list.
    Again, don't forget to add nodes to the `visited` list and pass the list to the next function call.
    Also, `graph_rec` should be `self.graph_rec`.
    
