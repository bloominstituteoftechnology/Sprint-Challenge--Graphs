Describe the fixes/improvements you made to the Graph implementation here.
1. The edges were being connected to itself and not the other vertex!
2. The find_components method was checking if the vertex was in visited, when it was supposed to checking if it was not in visited.
The dfs method was appending forever, creating an infinite loop. Had to add z(current) to y(visited) and subtract that from x(stack)
to return the correct values.