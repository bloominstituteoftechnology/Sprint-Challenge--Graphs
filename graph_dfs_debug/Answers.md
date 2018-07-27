Describe the fixes/improvements you made to the Graph implementation here.

To display the nodes on the graph we needed to create each vertice using the Vertex
class and pass that vertice to the Graph class. From there we need to pass the entire
graph class to the BokehGraph class, this is where the magic happens.

Originally when adding edges with the `add_edge` method on the `Graph` class we were
adding the vertice to itself. To fix this we need to instead add the `end` variable
to the `start`, which are the vertices we supply to the `add_edge` method, and if
`bidirectional` is `True` we also flip this process, add `start` to `end`.

Originally we were NOT correctly tracking whether or not components actually existed.
To do this, when we add edges to our vertices we need to increase their count so that
our `_get_connected_component_colors` method on the `BokehGraph` class can add the
correct colors to our connected components, `vertices` that are connected with `edges`.