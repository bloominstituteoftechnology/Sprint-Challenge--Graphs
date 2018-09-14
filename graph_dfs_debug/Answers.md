Describe the fixes/improvements you made to the Graph implementation here.
The first pass of going through your class, going from top to bottom, here are some thoughts.

- When adding a vertex, make sure the vertex being added doesn't already exist.
- make sure the edges connect to vertices that do exist
