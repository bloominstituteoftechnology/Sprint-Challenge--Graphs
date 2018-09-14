Describe the fixes/improvements you made to the Graph implementation here.

# graph.py
1.In `add_edge()`, we needed add vertices correctly
```
    self.vertices[start].add(end)
    if bidirectional:
        self.vertices[start].add(end)
        self.vertices[end].add(start)
```
2.In `dfs`, we needed add vertices correctly
```
    stack = []
    stack.append(start)
    visited = set(stack)

    while stack:
        curr_vert = stack.pop(0)
        if curr_vert == target:
            break
        visited.add(curr_vert)
        stack.extend(self.vertices[curr_vert] - visited)
        visited.update(self.vertices[curr_vert])
```
3. In `find_components`, needed to change to `if vertex not in visited:`

# draw.py

1. when setting colors, `self._get_random_colors(len(self.vertex_list))` needs the number of vertices sent in


#routing.py

```
    def find_vertex(self, value):
        for v in self.vertices:
            if v.value == value:
                return v
        return None
```

```
    def bfs(self, start_vert):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """
        # !!!! IMPLEMENT ME
        for v in graph.vertices:
            v.color = 'white'
            v.parent = None   #<-- Add parent initialization

        q = []
        start_vert.color = 'gray'
        q.append(start_vert)
        while len(q) > 0:

            u = q[0]

            for e in u.edges:
                if e.destination.color == 'white':
                    e.destination.color = 'gray'
                    e.destination.parent = u     # <-- Keep a parent link
                    q.append(e.destination)
                
            q.pop(0)
            u.color = 'black'
```

```
    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # !!!! IMPLEMENT ME
        curr_vert = start
        str = f"{curr_vert.value}"
        while curr_vert.parent != None:
             curr_vert=curr_vert.parent
             str = f"{curr_vert.value} --> {str}"

        print(str)

```

