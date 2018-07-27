Describe the fixes/improvements you made to the Graph implementation here.

### Main Issues

<hr>

> Nothing seems to connect, my edges aren't showing up.

It is because all your vertices have cycles with themselves. `self.vertices[start]` is a key in the `Graph`'s dictionary, and its *value* is a set that contains all the *other* vertices it has edges with.

Look at your line, `self.vertices[start].add(start)`. ??? That's saying for a given a vertex `self.vertices[start]`, add an edge that connects to vertex `start`. Remember, the key of `self.vertices[start]` is the same as `start`. So, you having a vertex have an edge with itself. _Bruh_.

**Adjustments**

In `add_edge`

* Fixed method so that it doesn't end up creating cyclic islands of vertices.

<hr>

> All the vertexes are the same color.  They're supposed to be different colors if they're not connected, and right now none of them are.

The below adjustments do not directly address the issue, but it seems that the underlying cause of this problem is non-functioning methods in `graph.py`. Specifically, the non-functioning methods prevent classification of vertices into different components, so all the vertices end up being drawn the same color because they're all `self.components == 0`.

Therefore, addressing those methods ultimately addresses this issue.

**Adjustments**

In `dfs`

* The variable name confusion resulted in the totally wrong thing being returned. We are now returning `visited`, which returns all the vertices traversed starting from the `start` vertex.
* Added `- visited` to the argument passed to `stack.extend()`. This ensures we don't add vertices already visited into the stack.
* We also need to add visited vertices to the `visited` stack. Otherwise, we filter nothing when we go `self.vertices[current] - visited`, so we still visit the visited vertices again and again and again and again and again and again and again and again...

In `find_components`

* Changed `if vertex in visited:` to `if vertex not in visited:`. The point of this line is to ensure we don't consider vertices we've already visited. But if we had the line as it was formerly, *we'd never visit any vertex, even for the first time, because we have not visited any vertex*. 

<hr>

> Sometimes I do something and when I run `python graph_demo.py` it just takes forever, even though my `draw.py` and `graph_demo.py` are totally just the same as from class.

I can't recreate the issue. Perhaps by fixing other problems, we have made this problem disappear? That'd be nice!

(*If I had to take a guess, it's probably the accidental infinite loop in `bfs`. That's been dealt with.*)

<hr>

> I wanted to let it find a target vertex, but even back when it did kinda run this part didn't really work.

Is it because it's just taking a `break`?

**Adjustments**

* Changed `if` condition in `while stack` loop in `dfs` to actually return the found match instead of just `break`ing.

<hr>

> My editor sure is complaining a lot about something called "lint."

"Lint" protects you from dumb mistakes like typos. It also helps your code conform to standards and conventions that help other people, like me, read your code better.

**Adjustments**

In `graph.py`

* Removed unused imports from `math`
* Put doc_strings under class declarations
* Not directly referenced by linter, but I guess `graph_rec` is an earlier abandoned implementation of a search method? Out it goes!

In `draw.py`

* Fixed spacing between method declarations `__init__` and `_setup_graph_renderer` in `BokehGraph`

<hr>

> I keep losing track of my variables, I guess I should name them better?

**Adjustments**

* In `dfs`, changed variable names to be more semantic. Specifically, changed names to be clear that:
  * We are using a stack to do our business
  * We are keeping track of the current vertex being considered
  * We are keeping track of visited vertices