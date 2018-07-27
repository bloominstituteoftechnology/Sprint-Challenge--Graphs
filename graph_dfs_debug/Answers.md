Describe the fixes/improvements you made to the Graph implementation here.

#Changes to Graph.py

Line 22 + 24 -- The edges would go start -> start and end -> end. this won't work. Changed it to start to end and end to start. 
Lines 27-29 -- changes var names
Line 43 - directed recursion function to self 

#Changes to graph_demo.py 

Needed to change draw_componets to false for the graph to show and connect the vertices

#Changes to routing.py

In the find_vertex(line 31), bfs(Line 49), and the output_route(Line 57) functions I implemented them to fit the sprint challenge