Describe the fixes/improvements you made to the Graph implementation here.
In Vertex class, renamed label to vert_label and removed the str() from self.label
In Graph class changed the add_vertex method so that it calls the Vertex class instead of just set()
Refactored add_edge so that it is accessing the edges of each vertex.
Imported Graph class from graph into draw.py

In Draw.py file, in the setup_graph_renderer method, replaced [vertex.label for vertex in self.vertex_list] with self.vertex_list.

For the recursive search graph_rec, removed =None from target parameter and added and added a visited parameter set to =None.  Made a few more fixes to graph_rec, should now be working correctly

Revised Notes:
1. In add_edge method changed .add(start) to .add(end) and vice versa for if bidirectional is True
2. 
3. 
4. Created a stack class to use for the DFS method.  Refactored and debugged DFS so that it is now working.
5. 
6. I've renamed several variable to make the code more clear.