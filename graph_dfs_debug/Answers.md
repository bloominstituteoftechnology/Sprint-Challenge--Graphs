Describe the fixes/improvements you made to the Graph implementation here.

1. <code>add_edge()</code> was creating an edge <code>self.vertices[start].add(start</code> and </code>self.vertices[end].add(end)<code> that were connecting start to start and end to end, instead of start to end and end to start.

<code>
    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
            </code>


2. <code>find_components()</code> should be vertex not in visited instead of vertex in visited.

<code>
   for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
        </code>


