Describe the fixes you made to the Graph implementation here.

When the randomize button is clicked this.onButton should be called like this: () => this.onButton()

Made the weights be randomized by making a randomized number from 1-10 be passed into the new edges inside of the randomize function

Made the canvas the correct width by making the canvas width equal to canvasWidth instead of canvasHeight in the render for GraphView

I imported my bfs from the week project to make the colors work right, because I couldn't figure out how to fix dfs to make sure that connected vertexes had the same color

I made the radius boxSize divided by 12 instead of 8 so that circles wouldn't sometimes get cut off on the edge of the canvas.
