Describe the fixes/improvements you made to the Graph implementation here.

# Add Labels in draw.py:
graph_renderer.node_renderer.data_source.add(self.vertex_list, 'index')


# fixed add_edge and dfs:
start vertex is adding end and vice versa
added unvisited vertices to x i.e. queue
added 'not' to conditional in find_components
added y.add(z) to dfs
return return y i.e. set containing connected vertices instead of return x i.e. stack