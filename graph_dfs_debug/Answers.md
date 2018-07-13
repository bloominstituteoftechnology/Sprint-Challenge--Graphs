Describe the fixes you made to the Graph implementation here.

# Axhon Ruiz

1.  The graph draws crazily.
    > Line 135 graph.js
    > There is an unnecessary shift
2.  All the vertexes are the same color. They're supposed to match the color of the edges for each connected component.
    > Line 64 App.js
    > You are not applying the parameter `color` into the draw function
3.  My randomize button is broken.
    > Line 159 App.js
    > The name of the handler is `onButton` not `Button`
4.  It looks like part of the graph is getting cut off.
    > Line 125 App.js
    > The canvas' `width` prop was receiving the `canvasHeight` value.
