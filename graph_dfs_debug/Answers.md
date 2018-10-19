Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seems to connect, my edges aren't showing up.

#Line 5
- Removed        
`, component=-1`
- Not necessary for a graph to work

#Line 7
- Removed 
`self.component = component`
- Not necessary

#Line 8
- Added
`self.edges = set()`
- Needs to initialize edges set

#Line 16
- Removed
`self.components = 0`
- Not necessary

#Line 18/19
- Added
`if vertex in self.vertices:`
	`raise Exception("Vertex already added, please add a different one”)`
- To make sure the newly added node is unique

#Line 21
- Added
`if start not in self.vertices or end not in self.vertices:`
- To make sure the nodes are already added

#Line 22
- Added
`raise Exception("Missing necessary nodes to add edges to”)`
- A reminder in case nodes weren’t added

#Line 23
- Fixed
`self.vertices[start].add(start)`
- To
`self.vertices[start].add(end)`
- Must connect a node to a different node

#Line 25
- Fixed
`self.vertices[end].add(end)`
- To
`self.vertices[end].add(start)`
- Same as Line 23
