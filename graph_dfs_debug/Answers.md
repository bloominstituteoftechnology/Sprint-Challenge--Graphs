Describe the fixes/improvements you made to the Graph implementation here.

### Graph Class
- `add_edge` method altered to add edge from start to end, end to start
- `graph_rec` method needed `self.graph_rec`, append to add
- `dfs` method changed to have clearer names, modify code a little, should compare
the pop element with target, need to take out visited elements on extend
- `find_components` method needed to have `not in visited`, wouldn't run the function
with just `in visited` because nothing is in visited initially