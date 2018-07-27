Describe the fixes/improvements you made to the Graph implementation here.
The problem with the implemtation of dfs is using variables that are not meaningful and it is easy to make mistakes

1. def dfs(self, start, target=None):
        x = []
        # x is the stack, can be named as such so that we know it LIFO
        x.append(start)
        # stack.append(start)
        y = set(x)
        # y should be named visited, naming it y makes it is hard to track what is in y, it would make sense that if it in visited we don't have to search for it again

        while x:
            z = x.pop()
             #z should be named current node, since it is that.
            if x == target:
            # logical error, if current == target
                break
            # should be added to visited or y
            y.add(z)
            #have to keep track of the visited node to the one not
            #logical error should be
            x.extend(self.vertices[z] - y)
            #the way the code was setup we will not have clear pic of what is visited and what is in stack.


        return y
        #should return visited

2. in add edge, the mapping should be from start to end and if bidirectional from end to start
def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)
3. randomize:
Needs actual vertices from the graph class not the Vertex_list 
def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices: # graph.vertices not Vertex_list
            # TODO make bounds and random draws less hacky
            self.pos[vertex.label] = (1 + random() * (self.width - 2),
                                      1 + random() * (self.height - 2))