Describe the fixes/improvements you made to the Graph implementation here.

1. `add_edge`: <br>
`add_edge` was adding from `start` to `start` rather than `start` to `end` and vice versa
<br> <br>
2. `dfs`: <br>
Variable names were really confusing so I rewrote it with clearer names, left old code for reference. Implemented a stack. <br> <br>
3. `graph_rec`: <br>
Was not keeping track of visited vertices and was not passing in necessary data to recursive function call. Variables badly named. Commented out old code and left for reference
4. `find_components`: <br>
Coloration not working because was checking for vertices in visited rather that not in visited