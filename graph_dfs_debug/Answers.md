Describe the fixes/improvements you made to the Graph implementation here.

--Installed pylint and bokeh

1. Graph.py
    a. Added checks in graph.py functions(add_vertex, and add_edge) to see if changes were valid. 

    In add_vertex, I added an exception that checked to see if the vertex already existed and if the vertex's edges already existed.

    In add_edge I checked to see if the start and edge vertex's passed in as parameters were in the graph. I also had to changed the add method to end when accessing the start vertices.

    b. In the dfs search I changed variables to make code more readable.

    I also made it so any vertex that was visited as properly added into the visited set.

2. Graph_demo.py
    a. Added checks tgo see if edge already existed