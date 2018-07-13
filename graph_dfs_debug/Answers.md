Describe the fixes you made to the Graph implementation here.

1. The graph draws crazily.
- in graph.js, line 131 should be unshift instead of push

2. All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.
- in graph.js, commented out line 135 de-stack

3. My randomize button is broken.
- in app.js, line 158 correct `this.Button` to `this.onButton`

4. It looks like part of the graph is getting cut off.
- in app.js, line 8 increased boxSize