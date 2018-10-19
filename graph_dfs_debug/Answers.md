Describe the fixes/improvements you made to the Graph implementation here.

- I changed the add_edge function to add the end vertex to the start vertex, and if bidirectional then also add the start vertex to the end vertex

- I changed "if bidirectional" to "if bidirectional is True"

- Changed dfs while loop to "while len(x) > 0" from "while x" and added "return True" to if statement, changing x to z

- In the line with x.extend I updated it to add the z.edges, added a line to update y using union, returned y instead of x.

- Added add function to vertex class, added edges property to vertex class
