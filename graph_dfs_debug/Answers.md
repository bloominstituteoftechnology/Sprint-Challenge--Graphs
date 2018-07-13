Describe the fixes you made to the Graph implementation here.

Dear Friend,

Below are my responses to your concerns and a list of changes I made. Please let me know if there's anything else I can help with.

1. The graph draws crazily.

2. All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.
    - you were passing in a default color value to the `drawVerts` function, which i replaced with a random color generator to make it more consistent.
3. My randomize button is broken.
4. It looks like part of the graph is getting cut off.

Changes Made:
(1) In your App.js file, you were clearing the canvas in the same method which you were drawing your vertexes. I create a separate method called `updateCanvas` which handles updating the canvas