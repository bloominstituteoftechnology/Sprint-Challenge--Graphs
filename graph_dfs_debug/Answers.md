Describe the fixes/improvements you made to the Graph implementation here.

### Linting Issues
I've got Flake8 installed in my editor which checks that all Python files follow the PEP8 style guide. To get the code to comply I changed the following:

- Lines should only be up to 79 characters long. With that in mind I broke up several lines that were too long in `draw.py`:
  - The bokeh.models import
  - The Bokeh `figure` method call in the `BokehGraph` class constructor
  - The `edge_renderer` data source setup

- Classes are required to have two blank lines before and after (if it's the last thing in a file you just one blank line at the end). I added two lines before the `Vertex` class in `graph.py` and one line after.
- In `draw.py` I removed imports that were never used: math.ceil, math.floor, math.sqrt

### Fixed Variable Names
It was hard to keep track of certain variables in `graph.py` as they had generic names. I gave different names to the following variables:

- In the `dfs` method:
    - Renamed `x` to `stack` since that is the data structure a depth first search utilizes
    - Renames `z` to `current` since this represents the current vertex that you are visiting
    - As you are searching you'll want to keep track of which vertexes you've already visited. I'm assuming that is where you were going with `y`. I renamed that `visited` 

### Fixed Edges
The edges were not showing up because they were not being setup correctly in the `add_edge` method. An edge connects one vertex to the other so it has a start vertex and an end vertex. While `add_edge` was accepting a start and end, it was assigning the start and end to the same vertex. Instead of doing `self.vertices[start].add(start)` which is like saying _start the edge at my start vertex and end it at my start vertex_ it should be `self.vertices[start].add(end)` which says _start the edge at my start vertex and end it at my end vertex_. The bidirectional condition had the same issue. It was starting and ending at the same point.

### Fixed Colored Components and Fixed Infinite Loop in DFS
To identify the components and perform a depth first search, you have to properly keep track of which vertexes you've already visited otherwise you'll get unintended side effects.

In `find_components` a search for connected components was only triggered if the current vertex was in the visited list. At that point visited is an empty set so none of the logic was ever triggered. You also want to visit a vertex only if it has _not_ been visited. The fix here was changing the condition to say if vertex is not in the visited set: `if vertex not in visited:`

That change triggered the `dfs` method which also sent the script into an infinite loop because nothing was keeping track of which vertexes had already been visited. Earlier I changed the `y` variable to `visited` but nothing was being done with it. I changed the initialization to be an empty set as at that point we haven't visited anything yet. Popping a vertex off of the stack is the same as visiting that vertex so it is after that point that we want to add it to the list of visited vertexes. You'll then want to update your stack by removing any vertexes that now sit in the visited list. To do that I added `visited.add(current)` inside the loop and modified the stack update to `stack.extend(self.vertices[current] - visited)`. Finally the point of a depth first search is to traverse the graph so we'll want the list of vertexes it visited back. The visited list is what should be returned not the stack which will be empty at the end of our search.

### Fixed Finding A Target Vertex
The `dfs` method was looking for the target by comparing the stack to the target. It instead needed to compare the current vertex to the target.
