Describe the fixes/improvements you made to the Graph implementation here.

- [x] Nothing seems to connect, my edges aren't showing up.

To connect the edges, I used `add()` to add the opposite vertex. For example, `self.vertices[start].add(end)` rather than the same vertex: ``self.vertices[start].add(start)`

```
def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
```

- [x] All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

The key here was changing the if statement to look for vertices `not` in visited

```
if vertex in visited:
# became
if vertex not in visited:
```

- [ ] Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
- [ ] I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.
- [ ] My editor sure is complaining a lot about something called "lint."
- [x] I keep losing track of my variables, I guess I should name them better?

For dfs, I created a stack and visited list and changed `x` to `stack` and `y` to `visited`. I changed `z` to `current_node` and used `pop()`. Rather than comparing x (now stack) to `target`, I compared current_node. I extended stack adding unvisited nodes. Finally I returend `visited`. This one really showed the importance of variable naming conventions.

```
def dfs(self, start, target=None):
    stack = [start]
    visited = set()

    while stack:
        current_node = stack.pop()
        if current_node == target:
            break
        stack.extend(self.vertices[current_node] - visited)

    return visited
```

- [x] I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck.

I made the recursive dfs more descriptive by changing `graph_rec` to `dfs_rec`, `x` to `visited`, and `v` to `vertex`. I changed `append` to `add` because add works better with `set()` and add doesn't add items already present. To make the recursion work, I called `dfs_rec` with `self.dfs_rec`.

```
def dfs_rec(self, start, target=None):
    visited = set()
    visited.add(start)
    for vertex in self.vertices[start]:
        self.dfs_rec(vertex)
    return visited
```