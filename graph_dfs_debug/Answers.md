Describe the fixes you made to the Graph implementation here.

1. Adjusted graph canvas size.
    Line#122: updated width to equal 'canvasWidth' instead of 'canvasHeight'
2. Edge of the vertexes are not matching in color
3. Random click button does not work
    Line#159: button onClick was set to 'this.Button', while the actual function is called onButton. Changed onClick to call 'this.onButton' to resolve issue.
4. 