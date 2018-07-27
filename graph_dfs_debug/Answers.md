Describe the fixes/improvements you made to the Graph implementation here.
1. change the graph.py method defined:
    instead of using two separate definition. I put these two together
    def search(self, start, target=None, method='dfs'):
    ...
    along with changing the name on line#57 reachable = self.search(vertex)

2: change the draw.py def _setup_graph_renderer:
    self.vertex_list to self.vertex_keys
    and follow by:
    graph_renderer.node_renderer.data_source.add(
            self.vertex_keys, 'index')
    this is much easier, but yours not wrong
    also need to change everything else if it has vertex_list to vertex_keys
    
3. change the graph_demo.py last line with this code instead of main()

print('Expected arguments: num_vertices num_edges draw_components')
print('Both numbers should be integers, draw_components should be 0/1')