Describe the fixes you made to the Graph implementation here.

1. Adjusted graph canvas size.
    Line#6-7: modified xCount and yCount to increase size of canvas.
2. Fixed canvas width.    
    Line#122: updated width to equal 'canvasWidth' instead of 'canvasHeight'
3. All vertexes are the same color & not corresponding the the edge component.
    Line#62: Changed fillStyle to variable color.
4. Random click button does not work.
    Line#159: button onClick was set to 'this.Button', while the actual function is called onButton. Changed onClick to call 'this.onButton' to resolve issue.
5. Graph is not color coding appropriately
    Line#131: removed stack.shift. The Stack is LIFO, so pop would be used, which it
    already implemented