"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0
    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)
    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        x_stack = [] # to act as our stack
        x_stack.append(start) # we append the start node to the stack
        # visited = set() # y will serve to hold all the visited vertices. we add visited nodes to visited in the while loop as they're popped from the stack
        visited = [] #changed from set to array because a set is unordered. This is necessary if we want to see the path taken by the algorithm to reach the target. 
        while x_stack: # while x (the stack) is not empty
            currentVert = x_stack.pop() #we pop out the element at the end of x. z is set equal to x
            if currentVert not in visited:
                visited.append(currentVert)
                x_stack.extend(self.vertices[currentVert])
            if currentVert == target:
                # return currentVert #serves to break the loop and return the target vertex. As set up before with the break, the return at the bottom would just return the last popped element in the stack.
                return visited #serves to break the loop and return all the vertices that were visited before finding the target vertex.
            else:
                pass
        if target is None: #For cases when you want the full depth first traversal (i.e. when you don't input a target vertex)
            return visited
        else:
            return None   #if the function loops through all the vertices and their edges without finding the target vertex, return None. 

    def graph_rec(self, start, target=None, visited = []): #changed data type of visited from set to array to preserve order # we set the value of visited here. otherwise, it will continuously be reset to empty for each recursive call and the recursive call will infinitely loop.
        # x.append(start) # changed x to visited for readability
        visited.append(start) #set object doesn't have an append method
        # print(start.label) 
        for vert in self.vertices[start]:
            if vert not in visited:
                self.graph_rec(vert)
        if target in visited or target is None:
            return visited #can also make it so that this returns only the path leading to the target node.
        else:
            return None 

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            visited.add(vertex) #vertices weren't added to the visited set here. 
            if vertex in visited:
                reachable = self.dfs(vertex)  #dfs method should return all the vertices touched during the traversal
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

# # TEST code
# graph = Graph()
# v0 = Vertex(0)
# v1 = Vertex(1)
# v2 = Vertex(2)
# v3 = Vertex(3)
# v4 = Vertex(4)
# v5 = Vertex(5)
# v6 = Vertex(6)
# v7 = Vertex(7)
# v8 = Vertex(8)
# v9 = Vertex(9)

# graph.add_vertex(v0)
# graph.add_vertex(v1)
# graph.add_vertex(v2)
# graph.add_vertex(v3)
# graph.add_vertex(v4)
# graph.add_vertex(v5)
# graph.add_vertex(v6)
# graph.add_vertex(v7)
# graph.add_vertex(v8)
# graph.add_vertex(v9)

# graph.add_edge(v0,v1)
# graph.add_edge(v0,v3)
# graph.add_edge(v1,v2)
# graph.add_edge(v2,v5)
# graph.add_edge(v2,v4)
# graph.add_edge(v4,v9)
# graph.add_edge(v3,v7)
# graph.add_edge(v3,v6)
# graph.add_edge(v7,v9)

# print(graph.dfs(v0,v9))
# print(graph.graph_rec(v0,v9))

# graph.find_components()
# print(graph.components)