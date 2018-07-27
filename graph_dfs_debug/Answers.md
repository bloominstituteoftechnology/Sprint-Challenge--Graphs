Describe the fixes/improvements you made to the Graph implementation here.

1. Added a conditional on line 20 to check if the vertex provided already exists in self.vertices. If it does, I added an exception to be raised on line 21. 

2. Added a conditional on line 22 to check if the edges provided exists as a subset of self.vertices. If it does, I added an exception to be raised on line 23. 

3. Added conditionals and exception statements from line 28 to line 31 to check if the start and end edges provided are in self.vertices. 
