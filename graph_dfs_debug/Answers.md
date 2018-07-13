Describe the fixes you made to the Graph implementation here.

graph.js - line 135
Comment out stack.shift() in dfs(), as DFS uses stack which are LIFO and thus use push and pop.

app.js - line 66
Change ctx.fillStyle = '#77f' to ctx.fillStyle = color, so that color will match vertex color from updateCanvasConnectedComponents()

app.js - line 162
Change onClick={this.Button} to onClick={this.onButton} to utilize provided onButton() function.

app.js - line 127
Change width={canvasHeight} to width={canvasWidth}.  Width was set to given height rather than width.