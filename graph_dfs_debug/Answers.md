1. In graph.py in the add_edge method changed the start and end agrguments as they were incorerct and creating self directed edges

	def add_edge(self, start, end, bidirectional=True):
        	self.vertices[start].add(end)       #changed add(start) to add(end) 
        	if bidirectional:
            		self.vertices[end].add(start)    #changed add(end) to add(start)

2. In graph.py changed the dfs method to check if edge already in visited, updated find components method to check if vertex not in visited

3. In graph_demo.py while adding random edges between the vertices, added a check condition to see if the edge already exits.
(if vertices[1] not in graph.vertices[vertices[0]] and vertices[0] not in graph.vertices[vertices[1]]:)

4. Installed pylint
