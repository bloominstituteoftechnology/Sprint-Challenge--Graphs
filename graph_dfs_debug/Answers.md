Describe the fixes/improvements you made to the Graph implementation here.

- modified add_vertex method
    -gave the method an if statemnt conditional to add a new vertex to edges that does not exist and is new 4

- modified add_edge
    -this method will add a new edged to vertices. if it is not bidirectional the method will implement the method at the end of the list. if it is bidirectional it will start at the begininng

-dfs search method
    -this method will search is using depth first search. I renamed the elements for naming convention to keep better track of stack
    -implemented while loop to track current in stack is equal to target. Once we have visited target we can remove it from the stack continue with search

-modified find_components method
    added if conditional statment for vertex is not visited, reach and assign it a set to make it unique. It then becomes a key value pair once it is assigned and then it moves to the next node