Describe the fixes you made to the Graph implementation here.

1. The graph draws crazily.


2. All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.



3. My randomize button is broken.

To fix this issue, the function passed into the onClick was "this.Button" when the method is actually "this.onButton".

4. It looks like part of the graph is getting cut off.

To fix this part of the graph, inside the render method the width was being set to 'canvasHeight' instead of 'canvasWidth'.