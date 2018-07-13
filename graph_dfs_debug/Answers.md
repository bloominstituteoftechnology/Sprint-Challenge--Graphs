Describe the fixes you made to the Graph implementation here.

*My randomize button is broken.*

- To fix the random button not functioning, in App.js on line 158 was not calling the right method on click so I fixed ```onClick={this.Button}``` to ```onClick={this.onButton}```

*All the vertexes are the same color. They're supposed to match the color of the edges for each connected component.*

- To fix, in App.js on line 62, I removed the static color and changed it to the dynamic color being passed in. ```ctx.fillStyle = '#77f';``` to ```ctx.fillStyle = color;```

*The graph draws crazily.*

- To fix, I commented out line 135, as we already popping out from the stack so it is unnecessary

*It looks like part of the graph is getting cut off.*

- To fix, in App.js the render method was setting the width of the canvas to the height so I changed that.