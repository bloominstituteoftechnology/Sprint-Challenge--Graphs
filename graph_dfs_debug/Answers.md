Describe the fixes you made to the Graph implementation here.

1. The graph draws crazily.
    In graph.js  stack.shift() was changed to unshift(); This one took me forever to find.

2. All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.
    They were the same color because fillStyle was not being randomized. It was set to a specific color.

3. My randomize button is broken.
    in App.js the <button onClick={this.onButton}>Random</button> was not calling the onButton() properly. It was calling {this.Button}.

4. It looks like part of the graph is getting cut off.
    In App.js this statement is incorrectly using canvasHeight twice: return <canvas ref="canvas" width={canvasHeight} height={canvasHeight}></canvas>;
