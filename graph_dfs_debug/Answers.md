Describe the fixes/improvements you made to the Graph implementation here.

Updated the add_edge method to ensure two vertces are connected to each other bidirectionally. Also made sure a vertex can connect one way.

I impleted a visited dict in my dfs method that allows for quick search to see if the vertex has been seen or not. Updated the variable names to make more sense (descriptive) and allow for better readability. The dfs method returns an array with the exact path it took and when the target is found, the next node is not appended. 


