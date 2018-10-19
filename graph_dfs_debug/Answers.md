Describe the fixes/improvements you made to the Graph implementation here.

In the graph class:
    In the add_edge method, connected start to end and vice versa instead of
  start to itself and end to itself.

    In the dfs method, switched it to compare using the popped off vertex
  instead of the list of vertices. Also had it add the current vertex to the
  vertex set and return said vertex set which contains a list of unique vertices visited.
  Also removed x from `y=set()`, vertices will be added
  to the set as they're looped over. Renamed variables for better understanding.
  Added a check to make sure that the current vertex isn't
  already in the seen list, this keeps from getting trapped in loops.

    In the find_components method, added check to make sure vertex is NOT in
  list of visited vertices, only want to search through ones we have seen.
