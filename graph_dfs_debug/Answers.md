Describe the fixes/improvements you made to the Graph implementation here.

1) Lines 22 & 25: changed the start vertices to point to the end and the end to point to the start. Otherwise, there is no way to create a proper edge between the two vertices.

2) Line 28-37: changed variable names to convey to another dev what you were intending to do here. X and Y were vague and easy to misconstrue. Also helped to ensure that the DFS would work as intended.

3) Line 39: Changed to visited to ensure that the stack would work as intended by not returning to a node that had been visited and including it in its path.

4) Line 41: Changed the method name to better convey what the intent of the method was for another dev that may come and look at the code.

5) Line 45: Added self in order to be able to properly call recursive without lint yelling at you, otheriwise it wouldn't work and the graph would not display properly.