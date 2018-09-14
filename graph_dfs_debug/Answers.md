Describe the fixes/improvements you made to the Graph implementation here.

1. In the add_edge method, I changed the vertex from adding to itself and instead to the end and I did vice verse if bidirectional. They now add to each other and connect the vertices.

2. In your find_components method you were checking if the vertex was already in visited and if it was it would repaint it. So every vertex was the same color. I changed the if statement so that if it wasn't in visited, therefore already colored, the loop would skip over it.

3. I added a base case to your graph_rec method so that it would stop running forever. I also fixed it even more by actually adding each visited node into the stack that you initialized and not just the start node.

4. On line 29, I removed the y variable being initialized as a set with the x list. This y set will be used to keep track of each element that has been checked and so x has not been checked yet.

On line 33, I changed the variable from x to z because we need to check if the current element(which is z) is our target index not the whole x list.

On line 35, I added an elif statement that checks to see if the current element(z) is not in the visited set (y) and if it is not it adds it to the set and adds to stack (x) the next vertex to check minus the ones already visited.

5. Ran through linter everything seems fine except for the recursive method needing to be invoked from self on line 48.

6. Changed the names of your variables for graph_rec() and dfs() so that they have a similar naming system to find_components().