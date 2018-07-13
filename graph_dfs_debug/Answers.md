Describe the fixes you made to the Graph implementation here.

1. The graph draws crazily.


2. All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.

3. My randomize button is broken.

To fix this issue, the function passed into the onClick was "this.Button" when the method is actually "this.onButton".

4. It looks like part of the graph is getting cut off.

To fix part of the graph getting cut off, I switched the canvasWidth to be "boxSize * yCount" instead of "boxSize * xCount" and the vice versa for canvasHeight.