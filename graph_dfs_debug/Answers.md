Describe the fixes/improvements you made to the Graph implementation here.

### def depth_first_search

1. If you wanted to you could add conditionals to inside the add_vertex and add_edge to filter out when they input variables that shouldn't be entered.
2. In your add edge, you added end to end.  I changed to end to start
3. Your variables aren't clearly labeled:
    1. dfs => depth_first_search
    2. x => stack
    3. y => visted
    4. z => current
4. I made the starter code in dfs => stack = [start] so you don't have to append
5. You don't have to initialize the x/stack in visted, bc it is added below, but it doesn't hurt bc it's a set
6. In while loop:
    1. I replaced variables with newer variable names
        1. if *current* == target
        2. *stack*.extend(self.vertices[*current*])
7. visted.add(current) => add the current vertex to visted so you don't check them again and go into loop
8. When extending stack with (self.vertices[current]), you need to subtract the visted set so that you don't revisit the vertexes that you already went to and go on a infinite loop
9. you should return visted and not the stack so that you know which vertex's were touched and the target was really not there.



### find_components

1. in => not in - you want to check vertexes you haven't checked