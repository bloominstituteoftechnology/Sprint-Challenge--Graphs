Describe the fixes/improvements you made to the Graph implementation here.

1.Formatted code to dispell linting errors, using a linter (I use Black), will fix this issue without this this can be time consuming.

2.your add_edges function was connecting its starts to itself and the ends to themselves so there were no connections showing up. I fixed this by changing `self.vertices[start].add(end)` and `self.vertices[end].add(start)` 

3.You had two variables described by the same letter x which was confusing I changed them to better represent what they were for, stack and checked.

4.THe reason your colors are the same although they are supposed to be differrent was because find_components if statement was checking if vertex in visited instead of if vertex not in visited