Describe the fixes you made to the Graph implementation here.

1. Removed stack.shift from the DFS.  DFS is LIFO, which is done with pop.
2. ctx.fillStyle before vertex for loop was set to #77f blue (line 63).  Changed to color.
3. button was calling "Button" instead of "onButton"
4. GraphView render had width={canvasHeight} changed to width={canvasWidth}.