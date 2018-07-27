Describe the fixes/improvements you made to the Graph implementation here.
1.The Edges aren't displayed because in the add_edge method, edge are connected with the same edge instead of other edges.
it is fixed as shown below:

def add_edge(self, start, end, bidirectional=True):
    self.vertices[start].add(end)
    if bidirectional:
       self.vertices[end].add(start)
       
2. Find_components method is not correct. In the code, we are considering visited vertices but it should be opposite.
corrected code:
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
     
3. Names of variables must be descriptive. For Example, in the dfs method, instead of using x,y we can use stack,visited. We can also initialize a list with the start element instead of doing it in another line.
fix: stack = [start]

4.Change in bfs method [stack.extend(self.vertices[current] - visited]
5.Code should be added in graph.add_vertex method in order to raise an exception where an edge points to non-existent edge.
       
