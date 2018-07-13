Describe the fixes you made to the Graph implementation here.

3. The button element's `onClick` property was not calling the proper function. Line 158: `onClick={this.Button}` -> `onClick={this.onButton}`
4. The canvas element's `width` property was using `canvasHeight`. Line 122: `width={canvasHeight}` -> `width={canvasWidth}`