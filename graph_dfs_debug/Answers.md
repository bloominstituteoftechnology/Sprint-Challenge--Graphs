Describe the fixes/improvements you made to the Graph implementation here.

- if vertex not in self.vertices: ------- if there are vertex is not in verticies

-  if start in self.vertices and end in self.vertices:------ if start of a vertex is in vertices and the end is as well then connect them

-   self.vertices[start].add(end) #change the start to end
        if bidirectional:
    self.vertices[end].add(start) #change the end to start
    this is needed to connect the vertices to one another.

-   ended up changing most of the DFS function from its original form
    I have kept the start and the target = none. 

     def dfs(self, start, target=None):
        visited = []    # create a empty visited dictionary
        stack = [start] # create a stack dictionary where start is placed
        while len(stack) > 0: # while stack is still holding start loop through it
            # pop off each off the elements
            destacked = stack.pop()
            #check to see if any of the destacked elements have been visited
            #and if any of the destacked elements are the target.

            if destacked not in visited:
                if destacked == target:
                    break
                    # place all of the destacked elements into the visited dictionary
                visited.append(destacked)
