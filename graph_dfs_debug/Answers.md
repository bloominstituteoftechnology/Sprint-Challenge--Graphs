Describe the fixes you made to the Graph implementation here.
2. The vert's fill style was being set statically. Line 62: `ctx.fillStyle = '#77f'` -> `ctx.fillStyle = color`
3. The button element's `onClick` property was not calling the proper function. Line 158: `onClick={this.Button}` -> `onClick={this.onButton}`
4. The canvas element's `width` property was using `canvasHeight`. Line 122: `width={canvasHeight}` -> `width={canvasWidth}`