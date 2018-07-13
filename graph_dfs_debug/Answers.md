Describe the fixes you made to the Graph implementation here.

Known Issues:
1. The graph draws crazily.
Fix: Commented out line 135 of graph.js, call isn't needed and causes the lines to enter the circle when it's not needed

2. All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.
Fix:

3. My randomize button is broken.
Fix: this.Button needed this.onButton

4. It looks like part of the graph is getting cut off.
Fix: Canvas was rendering it's width with the value of cavasheight, changed to canvaswidth
