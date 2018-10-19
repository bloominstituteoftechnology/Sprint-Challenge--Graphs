Describe the fixes/improvements you made to the Graph implementation here.

1. Edges aren't showing up: 
    access edges using "self.vertices[start].edges"
    
2. I noticed that, in find_components, it says:
     
     for vertex in self.vertices:
            if vertex in visited:
    
    I think that it should say 
    
            if vertex not in visited:

    that might solve the issue where all nodes start out having colors.

3.  

4.  We shouldn't be checking if the whole stack is equal to the target value 

    wrong --> if x == target:

    the method should check if the vertex we are observing (the one most recently removed from the stack) is equal to the target.

5.  in the graph_rec method, the ollowing code is trying to append a set, but we can only   use append with lists.

    wrong:
        x = set()
        x.append(start)

    we could do: 
        
        x.add(start)

    from my google searching, I learned that linting checks code for "programmating as well as stylistic errors".  So perhaps confusing "add()" with "append()" is a common mistake. 

6.  
    def dfs(self, start, target=None):
        x = [] <-- change to stack = [] to track nodes that have been checked

        x.append(start)
        
        y = set(x) <-- it seems that y should be the set of visited items from the stack

        while x:
            z = x.pop() <-- call z removed to indicated that                 we have taken an item from visited for inspection
            if x == target:
                break
            x.extend(self.vertices[z])

        return x