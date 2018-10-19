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
        queue = []
        queue.append(start)
        visited = set(queue)
        while queue:
            currentEvalVar = queue.pop()
            visited.add(currentEvalVar)
            if currentEvalVar == target:
                return True
            for vertix in self.vertices[currentEvalVar]:
                if vertix not in visited:
                    queue.append(vertix)
        if target is None:
            return visited
        else:
            return False

    def graph_rec(self, start, target=None,queue=None):
        if queue is None:
            queue=set()
        queue.add(start)
        for connected in self.vertices[start]:
            if connected not in queue:
                queue.update(self.graph_rec(connected,target, queue))
        return queue

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.graph_rec(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                    visited.add(other_vertex)
                current_component += 1
        self.components = current_component
