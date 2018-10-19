Describe the fixes/improvements you made to the Graph implementation here.
1) in add_edge function, changed `self.vertices[start].add(start)` to `self.vertices[start].add(end)` and `self.vertices[end].add(end)` to `self.vertices[end].add(start)`
2) in find_components function, changed `if vertex in visited:` to `if vertex not in visited:`
3) changed dfs function to 
        `stack = []`
        `stack.append(start)`
        `visited = set()`
        `while stack:`
            `z = stack.pop()`
            `if z not in visited:`
                `visited.add(z)`
                `stack.extend(self.vertices[z] - visited)`
            `if z == target:`
                `return True`
        `return visited`
4) dfs returns True if there is a target passed in and it is reachable via the start node. for instance, for an instantiation like this:
`graph = Graph()`
`graph.add_vertex(0)`
`graph.add_vertex(1)`
`graph.add_vertex(2)`
`graph.add_edge(0, 1)`
`print(graph.dfs(0, 1))`
running `python graph.py` will return true, but with `print(graph.dfs(0, 2))`, running the same file will result in the visited set, `{0, 1}`