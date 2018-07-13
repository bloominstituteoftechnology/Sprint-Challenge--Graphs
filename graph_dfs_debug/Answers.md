Describe the fixes you made to the Graph implementation here.

App.js
------
- Size of canvas: changed canvas width from  `canvasHeight` to `canvasWidth`
- Randomize button: changed click handler from `this.Button` to `this.onButton`
- Vertex colors: changed fillStyle from hardcoded value to `color`
- DFS stack: removed call to `stack.shift` in DFS, as `stack.pop` is also called