Describe the fixes you made to the Graph implementation here.

1. The `onClick` handler was referencing a method that doesn't exist. I set the method to the pre-defined `onButton` method.

2. The canvas width was set to `canvasHeight`. I changed this to set the width equal to `canvasWidth`.

3. The vertex fill color was constant. I set it equal to the color parameter.

4. Removed unnecessary `stack.shift()` from `dfs` method.