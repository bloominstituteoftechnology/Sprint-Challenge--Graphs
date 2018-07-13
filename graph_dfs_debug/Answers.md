Describe the fixes you made to the Graph implementation here.

1. The graph draws crazily.
    Graph is not color coding appropriately
        Line#131: removed stack.shift. The Stack is LIFO, so pop would be used, which it already implemented

2. All the vertexes are the same color. They're supposed to match the color of the edges for each connected component.
    All vertexes are the same color & not corresponding the the edge component.
        Line#62: Changed fillStyle to variable color.

3. My randomize button is broken.
    Random click button does not work.
        Line#159: button onClick was set to 'this.Button', while the actual function is called onButton. Changed onClick to call 'this.onButton' to resolve issue.

4. It looks like part of the graph is getting cut off.
    Adjusted graph canvas size.
        Line#6-7: modified xCount and yCount to increase size of canvas.
    Fixed canvas width.    
        Line#122: updated width to equal 'canvasWidth' instead of 'canvasHeight'
