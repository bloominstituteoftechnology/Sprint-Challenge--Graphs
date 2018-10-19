Describe the fixes/improvements you made to the Graph implementation here.
Lines  22 and  24 
from the Graph class add_edge method...
def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)
No edges will be connected because the start is connected to the start. And the end is connected to the end. Thus the vertex is connected to itself. Which is why no lines are shown on the graph.  

def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
now we are connecting to another vertex since start and end are two different vertex's

Lines show up.. 

Colors aren't showing up because of the find_componets method in the Graph class.  
def find_components(self):
    visited = set()
    current_component = 0
    for vertex in self.vertices:
                if vertex in visited:
                    reachable = self.dfs(vertex)
                    for other_vertex in reachable:
                        other_vertex.component = current_component
                    current_component += 1
                    visited.update(reachable)
            self.components = current_component

Line 23, the conditional is never met. Visited is set to be empty so the vertex in self. vertices aren't going to be in the set. Therefore, the other statements will never run. It is just a loop that runs through self.vertices and will never do anything else. Instead, we need to check for if vertex not in visited. If it is not in visited, we have not "visited" the vertex, so we need to. 

def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

Once we make the change, the graph takes forever to load.  This has something to do with the dfs method in the Graph class. Not sure exactly what's wrong but it is causing some loop I believe.  I don't like it at all so I am scratching it.  One thing nothing is being done with the y variable. We pop off z after adding it. Then we add it back to x.  This is no good. I'm scratching this off completely. 

def dfs(self, start, target=None):
        adj = self.vertices
        parent = {start: None}
        def visited(adj, start):
            for vertex in adj[start]:
                if target is not None and vertex == target:
                    return "Target Found"
                if vertex not in parent:
                    parent[vertex] = start
                    visited(adj, vertex)
        visited(adj, start)
        return parent 
What I am doing here is  I plan to run through self.vertices, but I don't want to keep typing self. vertices so I set it to a variable adj.  I create a parent dictionary setting start as a key and value None. This reads in plain English start has no parent as we are treating it as the root. Next, I create a function the sole purpose of this I don't want to carry the "visited"/ "parent" part around recursively. I do, however, want to perform some recursion. I use the adj variable and start as arguments. If the target is None and vertex matches the target we will return "target found." This line will not hit if the target is None.  Next, I want to know if the vertex is in the parent. If it is not let's go ahead and place it in the parent dictionary and allow the start to be its parent. We then make a recursive statement on that vertex. 

Now once this function is complete, we have to call it for the first time.  We then return the parent dictionary.  Some coders like to use a list. However, the in keyword works for dictionaries and list. I used the dictionary here because the result maintains the adjacency list feel. In a more complex program I may need to pass this around instead of the orginal self.vertices. (probably overthinking that though) 

Long story short  colors now change for non connected vertex or if there is mutliple connections.  Example of this is where there is three different types.  One connects 5 vertexs. Another connects between two vertex's and one solo vertex not connected. Three different colors. 

I am not sure about the losing of the variables.  What I would say is the naming convention of x y z  is not following the PEP  snake_case naming conventions. 

I also added a way to find the target. 

Graph_rec  has the issue of its returning a empty set. There is no case for if the target is not none.  Pretty much just runs through the vertices without a care in the world. I would add a check if  v == target  return True. Also you will get an error message on x.append(start)  x is a set() there is no append method on set. You have to use add().  Also the way the method is set up you may have to carry around your visited data. So x would have to be passed in and some way to add where you have been to your method. 