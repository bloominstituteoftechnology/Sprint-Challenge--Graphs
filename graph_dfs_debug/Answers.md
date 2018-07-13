Describe the fixes you made to the Graph implementation here.

### graph.js --> 

line 14:
change class Vertex constructor's parameter to value's default value  to be 'default'
instead of passing color as a parameter passed the position and {x:-1, y: -1} as default parameter

line 21: 
changed this.color --> this.pos = pos; 

line 154: 
added a for loop to add color white to all of the verts.


### app.js--> 

at line 43 --> changed the canvas color to be gray.
On line 62 -->  fillStyle removed hard-coded color form #77f  --> variable --> color
on line 84 --> commented out the unused function -->  updateCanvasEntireGraph();
On line 122 -->  width -->  {canvasWidth} 
at line 158 -->  changed the handler name to --> this.onButton