Describe the fixes you made to the Graph implementation here.

App.js

line 125 - width of canvas should be canvasWidth not canvasHeight
line 6 & 7 - modified the x & y count to increase the size of the canvas.
line 64 - changed fillStyle to use the variable 'color'
line 160 - onClick fixed to call the onButton function

Graph.js

line 135 - commented out 'stack.shift' because pop should be used in a stack (LIFO). This is already declared on line 126.
