Describe the fixes you made to the Graph implementation here.

1. Every connected component was not correctly color-coded. This turned out to be an issue with the depth-first-search implementation. There was a call to `.shift()` as well as a call to `.pop()`, so vertexes were getting removed from the stack when they weren't supposed to be. Fixed this by removing the extra `.shift()` call (which shouldn't be in a stack anyway).

2. Remove the hard-coded color value and make sure we are using the passed-in random color. 

3. The randomize button was broken because of a typo.

4. In order to fix the canvas cutting off the graph, I noticed that the canvas always rendered as a square despite the fact that the xCount and yCount did not match ... I found the actual problem when I inspected the render method of GraphView. It turned out the width and height were both being set to canvasHeight, which explained why the canvas was always being rendered as a square. 