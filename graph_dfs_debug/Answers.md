Describe the fixes/improvements you made to the Graph implementation here.


1. pip installed Bokeh

2. add checks to add_vertex and edd_edges functions (graph.py)

3. Gutted and rewrote dfs with more verbose variable names, 
 and added print statements to see what was happening internally

4. while testing dfs, it illuminated a mistake in add_edges:
   (which was causing an infinite loop)
    self.vertices[start].add(start) -> self.vertices[start].add(end)

5. I tested dfs by adding to the bottom of graph.py and running it:

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

6. Honestly, not sure what graph_rec function is for, just going to ignore it for now, since it doesn't seem connected to anything else in graph.py. I've commented it out with a question, oppossed to just deleting it.

7. in find_components:
    if vertex in visited: -> if vertex not in visited

8. After doing all of the above, I ran graph_demo.py, and all seems to be working correctly. I am choosing to leave the print statements in my dfs function because I find the printout of each step of a traversal very useful info.

9. After realizing graph_rec was an alternative recursive search method, I cleaned up the variable names, and added a helper function to execute the recursive part.
