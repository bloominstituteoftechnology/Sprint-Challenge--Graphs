Describe the fixes/improvements you made to the Graph implementation here.


1. pip installed Bokeh

2. add checks to add_vertex and edd_edges functions (graph.py)

3. Fixed dfs, which illuminated a mistake in add_edges:
    self.vertices[start].add(start) -> self.vertices[start].add(end)

4. I tested dfs by adding to the bottom of graph.py and running it:

    graph = Graph()

    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)

    print("\n")
    print("The Graph: ", graph.vertices)
    graph.dfs(3)

5. Honestly, not sure what graph_rec function is for, just going to ignore it for now, since it doesn't seem connected to anything else in graph.py. I've commented it out with a question, oppossed to just deleting it.

6. in find_components:
    if vertex in visited: -> if vertex not in visited