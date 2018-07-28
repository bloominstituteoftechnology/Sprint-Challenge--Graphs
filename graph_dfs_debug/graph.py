"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return self.label

class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('ERROR: This Vertex Already Exisits')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        q = [start]
        index = -1
        visited = set()

        while q:
            current = q.pop(index)
            print("Current Vertex: ", current)
            if current == target:
                break
            visited.add(current)
            print("Visited Vertices: ", visited)
            q.extend(self.vertices[current] - visited)
            print("Connected Vertices in Queue: ", q)
        
        return visited

    def dfs_recursive(self, vertex):
        visited = [False] * (len(self.vertices))
        print("Initially, None Have Been Checked: ", visited)
        self._dfs_helper(vertex, visited)

    def _dfs_helper(self, root, visited):
        visited[root] = True
        print("Updated When Checked: ", visited)
        for adjacents in self.vertices[root]:
            print("Has It Checked This Node?", adjacents)
            if visited[adjacents] == False:
                self._dfs_helper(adjacents, visited)

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

    def shortest_route(self, start, end, path=[]):
        path = path + [start]
        print("Path: ", path)
        if start == end:
            return path
        if not self.vertices[start]:
            return None
        shortest_path = None
        for vertex in self.vertices[start]:
            print("Current Position: ", vertex)
            if vertex not in path:
                new_path = self.shortest_route(vertex, end, path)
                if new_path:
                    if not shortest_path or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        print("Shortest Path: ", shortest_path)
        return shortest_path

    def bfs(self, start):
        visited = [False] * (len(self.vertices))
        print("Initially, all Nodes are set to False: ", visited)
        q = []
        q.append(start)
        visited[start] = True
        print("Updated when Visited: ", visited)

        while q:
            print("Queue to be Visited: ", q)
            current = q.pop(0)
            print("Current Position: ", current)
            print("Updated when visited: ", visited)
            for next_up in self.vertices[start]:
                if visited[next_up] == False:
                    q.append(next_up)
                    visited[next_up]=True

"""
TESTS
"""
graph = Graph()

graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

print("\n")
print("Test Graph Data: ", graph.vertices)
print("\n")
print("Shortest Route Test: ")
print("(Between 0 and 5)")
graph.shortest_route(0, 5)
print("\n")
print("Depth-First Search Test: ")
print("(Starting at 3)")
graph.dfs(3)
print("\n")
print("Recursive DFS Test: ")
print("(Starting at 3)")
graph.dfs_recursive(3)
print("\n")
print("Breadth-First Search Test: ")
print("(Starting at 0)")
graph.bfs(0)
print("\n")
print("Depth-First Search on Randomly Generated Bokeh Graph: ")
