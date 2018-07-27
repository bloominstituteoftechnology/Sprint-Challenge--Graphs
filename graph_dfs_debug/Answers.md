Describe the fixes/improvements you made to the Graph implementation here.

1. updated variable names to be more descriptive of their purpose
2. added comments to describe what the code was doing
3. updated the add_vertex method to handle cases where:
	A. the vertex to be added already existed (vertex was already a key in self.vertices dictionary)
	B. the edge connected to a nonexistent vertex (edge vertices were not keys in self.vertices dictionary)

4. updated the add_edge method so that it connected edges properly
	A. Edges were connecting vertices to themselves (start to start, end to end) instead of another vertex (start to end, end to      start)
	B. This was also true for the bidirectional default.
	C. The method also could not handle the case where a nonexistent vertex was passed in as an argument

5.  updated the dfs method so that it now works
	A. visited should start empty, not with the start node
	B. stack should pop from the end for dfs, not from the zero index
	C. the conditional should check whether the popped node is equal to the target (None by default), not the whole stack
	D. visited now adds the current node
	E. stack now only updates with new nodes
	F. returns the visitied nodes, not an empty stack
