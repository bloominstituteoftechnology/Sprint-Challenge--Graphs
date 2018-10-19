Describe the fixes/improvements you made to the Graph implementation here.

I fixed add_edge method in the Graph class, the edges are attached to 2 different vertices so that they're no bidriectional.

find_components checked if a vertex had been visited and if it was it would be recolored. I changed the if statement so that if it wasn't flagged as visited, the loop would skip over it.

On line 33, I changed the variable from x to z because we need to check if the current element(which is z) is our target index not the whole x list.

On line 35, I included  an elif statement that can check if the current element(z) has not been visited (y), and if it is not, it will add it to the set and then adds to stack

changed variable names for graph_rec for my own clarity