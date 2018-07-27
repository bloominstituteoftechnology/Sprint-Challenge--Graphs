Describe the fixes/improvements you made to the Graph implementation here.

1) made this change on graph_rec even though it is not used on other classes on the example:
def graph_rec(self, start, target=None):
        x = set()
        #x.append(start) append does not work on a set so I changed it to x.add(start)
        x.add(start)

2) also on graph_rec method I did this change:

#graph_rec(v) changed to self.graph_rec(v)
 self.graph_rec(v)

 3) changed some names and added some logic to dfs function as follows:

 def dfs(self, start, target=None):
        #x = [] changet to stack=[]
        stack=[start]
        #x.append(start)
        #y = set(x) changed to visited=set()
        visited=set()

        #while x: changed to while stack:
        while stack:
            #z = x.pop() changed to current = stack.pop()
            current = stack.pop()
            #if x == target: changet to if current == target:
            if current == target:
                break
            # added visited.add(current)
            visited.add(current)
            #x.extend(self.vertices[z]) changed to visited.add(current) changed to the following line
            stack.extend(self.vertices[current] - visited)

4) 