Describe the fixes/improvements you made to the Graph implementation here.

- In 'graph.py' file within the add_edge method, I added end to the start and start to the end if bidirectional so the edges would display corrently in the graph demo.

- In 'graph.py' file within the depth first search(dfs) method, I made the variable names more intuitive and easy to read for the next developer. I also changed 'if stack == target' to 'if current == target' so we are targeting the current vertex. I also added '-visited' to line 36 so we can make sure to avoid re-visiting the same vertex.

- In 'graph.py' file within the graph_rec method, I changed it up quit a bit by adjusting the variable names to make them more intuitive and also changed the logic. Changed ".append()" method to ".add()" since we are working with a set and not a list. There was also a call to 'graph_rec(v)' but it needed a 'self' keywork since you are trying to call it inside of the Graph class. I also added the 'visited=None' argument to the method so it could start out as None and be changed upon coming across a vertex it had already visited. 

- In 'graph.py' file within the find_components method, I changed the 'if vertex in visited:'
to 'if vertex not in visited:' so it will now color the vertexes correctly if they aren't connected to any other vertices.