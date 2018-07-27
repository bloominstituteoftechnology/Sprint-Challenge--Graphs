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