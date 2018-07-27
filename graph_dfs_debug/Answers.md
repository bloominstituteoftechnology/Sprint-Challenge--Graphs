Here are the fixes/improvements that I made to the Graph implementation:

---
## Depth-first Search
I began by changing the variable names in `dfs` to names that were more descriptive. (`stack` for the stack, `explored` for the set of explored vertices, `vertex` for the current vertex). 

As soon as I did that, it became obvious that all three of those variables were being "mixed up". `x` was used to represent the stack, and then later used to represent the vertex. `x` (the stack) was being returned at the end, when it should have returned the explored set. So I changed those around so that each variable was representing the right thing.

Next, I noticed that there was no check in place to make sure a vertex had not already been explored. I added line 33 `if vertex not in explored:` and indented the lines after it so that a vertex would be skipped over if it had already been explored.

After that condition, I also added the vertex to the explored set, so that it would not be explored again in the future (line 34).

I later noticed that explored was always only containing the start vertex. This was because explored was initialized with the start vertex. (line 29 `explored = set(stack)`). That made the condition on line 33 to be false, so the loop started a new iteration, but with an empty stack (because the only vertex was `pop`ed off in the first iteration and no new vertices were added). When the stack is empty, the loop terminates, and the explored set is returned. I changed line 29 to be an empty set instead. `explored = set()`

## Recursive Implementation
Again, I started by changing variable names so that it would be easier to keep track of the logic. I used the same names as I used in `dfs`.

I changed `x` to `explored` and I noticed that it was initialized as a set, but then `.append()` is called on it (line 42). The `.append` method is for lists; the equivalent for a set is `.add()`.

Then I noticed that the linter was "complaining" about the recursive call on line 47. It said "undefined variable 'graph_rec'." This is because `graph_rec` is a method of the Graph object. When it is called inside of the Graph, it needs to be called on `self`; i.e: `self.graph_rec()`

Next, I added a condition on line 46 to again check the explored set before doing anything with a vertex. Without this condition, the function will run forever if given a component that has a cycle.

I added a condition to check if the target has been reached. If that's the case, the function will return the explored set. I made sure to pass that same target in as an argument for the recursive call as well.

The last step was to pass in the explored set as an argument to the function so that it can be checked on each recursive call. I added a default for the explored argument `explored=None` so that on the first iteration, it can be initialized as an empty set. Each recursive call after that passes in the already initialized set as an argument.

## Add Edges
I noticed that the vertices each had edges to themselves. I looked over the `add_edge` method and noticed that the start vertex is added to itself `self.vertices[start].add(start)` (Same with end vertex). I changed this to `self.vertices[start].add(end)` and that fixed the problem.

## Color Components
The reason why the nodes were the same color was due to a bug in `find_components()`. The problem was with line 55. The condition said `if vertex in visited:` but it should have said `if vertex not in visited:`. As it was, the condition would evaluate to false on the first iteration because none of the vertices had been visited yet, so self.components would always just be 0.