Describe the fixes/improvements you made to the Graph implementation here.

- I decided to change the _get_random_colors to contain brighter colors for the vertices.
- I changed Graph.add_edge() to add the start to the end and the end to the start (as it was, previously, start was adding to start and end was adding to end, making all of the nodes connected to themselves instead of to other nodes, which visually appears as there being no edges on the graph).
- I attempted to work on fixing DFS for roughly an hour and a half and kept getting KeyError thrown back to me when trying to index into self.vertices. I'm really frustrated with this sprint as a result.
- changed add_vertex and Vertex class for indexing purposes; created a separate attribute for edges as well
