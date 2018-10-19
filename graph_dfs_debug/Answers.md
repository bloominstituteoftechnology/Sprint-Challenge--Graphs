Describe the fixes/improvements you made to the Graph implementation here.

1. Edges aren't showing up:


2.
3.
4.
5.

6.  
    def dfs(self, start, target=None):
        x = [] <-- change to visited = [] to track nodes                that have been checked

        x.append(start)
        
        y = set(x) <-- it seems that y should be the edges

        while x:
            z = x.pop() <-- call z removed to indicated that                 we have taken an item from                       visited for inspection
            if x == target:
                break
            x.extend(self.vertices[z])

        return x