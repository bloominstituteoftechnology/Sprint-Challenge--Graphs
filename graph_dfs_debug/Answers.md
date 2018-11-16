Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seems to connect, my edges aren't showing up.

#Line 5
- Removed        
`, component=-1`
Not necessary for a graph to work

#Line 7
- Removed 
`self.component = component`
Not necessary

#Line 8
- Added
`self.edges = set()`
Needs to initialize edges set

#Line 16
- Removed
`self.components = 0`
Not necessary

#Line 18/19
- Added
`if vertex in self.vertices:`
	`raise Exception("Vertex already added, please add a different one”)`
To make sure the newly added node is unique

#Line 21
- Added
`if start not in self.vertices or end not in self.vertices:`
To make sure the nodes are already added

#Line 22
- Added
`raise Exception("Missing necessary nodes to add edges to”)`
A reminder in case nodes weren’t added

#Line 23
- Fixed
`self.vertices[start].add(start)`
- To
`self.vertices[start].add(end)`
Must connect a node to a different node

#Line 25
- Fixed
`self.vertices[end].add(end)`
- To
`self.vertices[end].add(start)`
Same as Line 23


2. All the vertexes are the same color.  They're supposed to be different colors

# Line 11
- Added
`from graph import Graph`
Need to import the graph you want to draw

Dear friend, your graph isn't showing at all, there are errors from outside of this file, so currently unable to check the current output to either confirm or correct issues.


3. Sometimes I do something and when I run python graph_demo.py it just takes forever, even though my draw.py and graph_demo.py are totally just the same as from class.

Friend, they aren't the same at all, if you could clarify what you're saying and what you're needing, this is a bit vague.

4. I wanted to let it find a target vertex, but even back when it did kinda run this part didn't really work.

Placed `components` back in graph but didn't add any unfinished code that isn't fully working properly, to not make your situation worse, friend.




