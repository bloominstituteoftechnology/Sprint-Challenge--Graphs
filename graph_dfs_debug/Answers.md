### Describe the fixes/improvements you made to the Graph implementation here.

##### Graph
- Added changes to dfs method
    - changed variable names, so it doesn't get mixed up.
    - added changes to the dfs method to make it work, like while loop.
    ```
    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop()
            if current == target:
                break
            stack.extend(self.vertices[current] - visited)
    ```

- Added changes to graph_rec
    - added visited.add(start)
    - added self.graph_rec(v) recursion
    - use add instead of append for set
    ```
    def graph_rec(self, start, target=None):
        visited = set()
        visited.add(start)
        for v in self.vertices[start]:
            self.graph_rec(v)
        return visited
    ```

