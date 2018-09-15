Describe the fixes/improvements you made to the Graph implementation here.

Tested and changed the add_edge method to make sure two vertces are connected to each other bi-directionally. Also made sure a vertex can connect one way.

dfs method implements a visited dictionary to quickly search if the vertex has been seen or not in O(1). Changed the variables to appropriate names such as stack and removed non-sense names such as x,y,z for readability. Also dfs method returns an array with the path it took. Just tested once the target is found, then it should not append the next node for path 
