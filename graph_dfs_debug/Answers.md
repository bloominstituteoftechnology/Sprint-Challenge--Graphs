Describe the fixes you made to the Graph implementation here.

# App.js

Line 75: removed for loop and moved fillText inside the for loop initially used for 'Draw the verts on top'. It will now have same color for all connected verticies.

Line 127: canvas width was set to 'canvasHeight'. Fixed to 'canvasWidth'.

Line 158: onClick was linked to non-exisiting function. Fixed path to proper function. 'onButton()'

# graph.js

Line 128: reassigned u to stack[0], rather than return value of stack.pop


