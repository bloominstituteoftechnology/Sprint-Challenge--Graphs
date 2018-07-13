Describe the fixes you made to the Graph implementation here.

App.js - fault: canvas height in the GraohView render was set to canvasWidth
  correction: switched canvasWidth to canvasHeight

App.js - fault: button was calling this.Button method instead of this.onButton
  correction: changed name of onClick function inside button element

App.js - fault: ctx.fillStyle in the drawVerts method was set to '#77f' when it needed to be set to the 'color' parameter to change like the edges
  correction: changed ctx.fillStyle to 'color'

graph.js - fault: stack.shift() inside of your dfs method was removing vertexes from the stack in a way that prevented a full set of connected componenets from forming
  correction: removed stack.shift() from dfs