Describe the fixes/improvements you made to the Graph implementation here.

1. Lines 22 and 24 are wrong. The way its setup is that the vertices are connecting to themselves
2. Had to change the if statement in the find_components method because it was preventing the code after from running
3. Had to change line 36 to stack.extend(self.vertices[current] - visited) because
   it was causing the hang
4. Line 34 was pointless as it was just breaking from the loop. Changed to return x
5.
6. Renamed the variables in dfs to make it less confusing
