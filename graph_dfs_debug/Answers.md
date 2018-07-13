Describe the fixes you made to the Graph implementation here.
1. fixed an issue in graph.js that was removing a vertex from the back of the stack and then also removing a vertex from the front of the stack, which was causing the lines to render after some of the vertexes.

2. changed the vertex fillstyle property from a fixed value to the parameter 'color'.

3. the randomize buttons onClick method was referencing an undefined method. so i changed it to onButton().

4. the canvas width parameter on line had the canvasHeight variable passed in so i switched it to the canvasWidth.
