Describe the fixes you made to the Graph implementation here.
1. Changed the onClick={this.Button} to {this.onButton} to fix the randomize.
2. The graph cutting off was to change canvas size change canvas width from canvasHeight to canvasWidth.
3. Switched the call to pop to shift in graph.js in the stacks as they are first in first out. 
4. Vertexes colors are the same as they match the colors of the edge for the connections.