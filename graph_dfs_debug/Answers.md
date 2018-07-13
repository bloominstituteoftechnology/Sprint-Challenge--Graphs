Describe the fixes you made to the Graph implementation here.

1. My randomize button is broken:
fix: Changed 'onButton' method was not called in render;

2. It looks like part of the graph is getting cut off.
fix: Render is graphView called both canvasHeight for width and hight;

3. All the vertexes are the same color. They're supposed to match the color of the edges for each connected component.
fix: Depth-first search was causing problem. Before check, instead of peeking the value, it was removing it.
Also, in app.js all vertexes were getting 'fixed' color instead of dinamic var named 'color';

4. The graph draws crazily.
fixed!