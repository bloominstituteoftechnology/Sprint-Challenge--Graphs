Describe the fixes/improvements you made to the Graph implementation here.




























graph.py file

    Line 22 where you add the edge, you were adding the starting vertex as the end, So the line representing the edge was never drawn.

    Line 24 you had to add the start not the end.

    Line 41 is a set, in order to add an item to a set you have to use .add()
     x.add(start) should be used.
    
    Line 43 since you were calling a function from within a function, there was no way for your varible
    to know where to look.  graph_rec is a funtion part of the Graph class, then you must specify self.graph_rec() when calling that function.  Otherwise it assumes you are calling a variable.

    Line 49 You have to check that the vertex is not visited.  so change the condition to "not in" in stead of "in".