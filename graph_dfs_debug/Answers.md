Describe the fixes/improvements you made to the Graph implementation here.


1. It seems like you were adding the vertices to themselves in add_edge
    So I added your end vertices to your start vertices instead of your start
    vertices to your start vertices. I also reversed this for your bidirectional edges.

2. The vertex should be explored if it is `not` in visited 



3. I think that you need to keep track of the vertices that you've visited in your dfs
    method. I would deprecate your graph_rec method in favor of dfs or possibly a more
    general version of a search method.


4. also make sure you're looking at whatever the current target is during each step


5. Your linter is there to help you when you stray from the proper path. 
     You needed a self.graph_rec as opposed to the graph_rec in the recursive
     part of your graph_rec method.


6. in dfs I changed some variables for clarity:
        x = stack
        y = visited 
        z = current
    
    in graph_rec changed:
        x = stack
        v = visited