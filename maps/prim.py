
# Python program to print DFS traversal for complete graph 
from collections import defaultdict 
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
  
        # Mark the current node as visited and print it 
        visited[v]= True
        print (v)
  
        # Recur for all the vertices adjacent to 
        # this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self): 
        V = len(self.graph)  #total vertices 
  
        # Mark all the vertices as not visited 
        visited =[False]*(V) 
  
        # Call the recursive helper function to print 
        # DFS traversal starting from all vertices one 
        # by one 
        for i in range(V): 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
# Driver code 
# Create a graph given in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print( "Following is Depth First Traversal")
g.DFS() 
  
# This code is contributed by Neelam Yadav 
testdict={
  0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
  1: [(3, 6), {'s': 0, 'n': 2}],
  2: [(3, 7), {'s': 1}],
  3: [(4, 5), {'w': 0, 'e': 4}],
  4: [(5, 5), {'w': 3}],
  5: [(3, 4), {'n': 0, 's': 6}],
  6: [(3, 3), {'n': 5}],
  7: [(2, 5), {'w': 8, 'e': 0}],
  8: [(1, 5), {'e': 7}]
}
def in_test_dict(check_item):
    if check_item is in testdict:
        return f'{check_item} in testdict'
    else:
        return f'false'

in_test_dict('0')

in_test_dict((1,5))
print(f'for item in testdic')