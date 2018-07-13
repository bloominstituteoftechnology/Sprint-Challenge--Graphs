Describe the fixes you made to the Graph implementation here.

The bug with the randomize button is that you named the the button function `onButton` but in render you called `this.Button`. You need to call it by the function name you gave it. 

The bug with the graph getting cut off and being drawn crazily is because in the line ` return <canvas ref="canvas" width={canvasHeight} height={canvasHeight}></canvas>;` you're calling `canvasHeight` for both the width and the height when you should be calling `canvasWidth` for width instead of `canvasHeight`. Changing the line to ` return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;` fixes the bug to where the canvas is the correct size and the graphs are being drawn properly. 

