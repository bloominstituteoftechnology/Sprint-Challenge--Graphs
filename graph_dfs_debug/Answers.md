Describe the fixes/improvements you made to the Graph implementation here.
Lines  22 and  24 
from the Graph class add_edge method...
def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)
No edges will be connected because the start is connected to the start. and the end is connected to the end. Thus the vertex is connected to itself. Which is why no lines are show on the graph.  

def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
now we are connecting to another vertex since start and end are two different vertex's

Lines show up.. 

