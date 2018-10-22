"""
Simple graph implementation compatible with BokehGraph class.
"""
from draw import BokehGraph

"""Trying to make this Graph class work..."""

class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            raise Exception("Error: Cannot have edge to nonexistent vertices")
        if vertex in self.vertices:
            raise Exception("Error: Vertex already exists.")
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        # check to see if we have a starting or ending node
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error: No vertices found")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        # Queue for breadth first, Stack for Depth first
        stack = []
        # append starting node
        stack.append(start)
        visited = set()

        # iterate through stack to find visited nodes
        while stack:
            current_node = stack.pop()
            visited.add(current_node)
            # check if next node is visited
            for next_node in self.vertices[current_node]:
                # if not, leave in stack and check next node
                if next_node not in visited:
                    stack.append(next_node)
        # return all visted nodes
        return visited

    def dfs_rec(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for other_vertex in self.vertices[start]:
            if other_vertex not in visited:
                self.dfs_rec(other_vertex, visited)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            # call dfs on node if NOT visted to add it to stack
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                # updates visited nodes with a new color, leaves nodes still in stack with original color
                visited.update(reachable)
        self.components = current_component

        
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label
