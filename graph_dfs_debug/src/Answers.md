Hello Pal,

You erred in the following ways:

1. You didn't include a .gitignore for some reason.

2. You use the word `vertexes` instead of `vertices`

3. You used `ctx.fillStyle = '#77f';` instead of `ctx.fillStyle = color;` before drawing your vertices.
  * Also, your dfs had an extra `stack.shift();` in it, which I commented out.

4. You called for `this.Button` instead of `this.onButton` for the Random button's onClick.

5. Your current setup is designed for square grids, so xCount and yCount need to be the same for the graph to draw correctly.
