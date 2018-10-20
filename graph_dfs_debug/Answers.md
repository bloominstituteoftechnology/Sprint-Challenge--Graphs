Describe the fixes/improvements you made to the Graph implementation here.

in add_edge the edges were beging added to the nodes themselves, not other nodes. added start to end and end to start (if bidirectional)

put self.edges on vertex class because that makes more sense to me

actually used vertex class in add_vertex

changed the random edge method in the interest of time, not sure what the original plan entailed

refactored things in draw.py to fit with vertex class

started to refactor recursive dfs but moving on to second part of sprint