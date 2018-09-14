Describe the fixes/improvements you made to the Graph implementation here.
1. The edges were being connected to itself and not the other vertex!

2. The find_components method was checking if the vertex was in visited, when it was supposed to checking if it was not in visited.
The dfs method was appending forever, creating an infinite loop. Had to add z(current) to y(visited) and subtract that from x(stack)
to return the correct values.

3. ?

4. It was checking if the stack was equal to the target. Changed it to check if the current node is equal to the target.

5. One of the variables in the method graph_rec was trying to append to a set(), had to change that to add().
It also tried calling itself without the use of the 'self' keyword.

6. The dfs and graph_rec methods had variables like x, y and z which are quite vague. 
Changed the variable names to be a bit more appropriate for what they are doing.

Changed the 'visited' variable to be included in the params so we can pass the visited data with each recursive call.
Then add the 'start' variable to 'visited' in every call. It will repeat until self.vertices[start] is None and then
return the visited components  