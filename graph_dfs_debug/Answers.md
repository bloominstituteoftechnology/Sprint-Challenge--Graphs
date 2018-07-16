Describe the fixes you made to the Graph implementation here.

When the randomize button is clicked this.onButton should be called like this: () => this.onButton()

Made the weights be randomized by making a randomized number from 1-10 be passed into the new edges inside of the randomize function

Made the canvas the correct width by making the canvas width equal to canvasWidth instead of canvasHeight in the render for GraphView

<!-- (actually this didn't fix it) Made the getConnectedComponents function work by making every vertex color white using a forloop -->
