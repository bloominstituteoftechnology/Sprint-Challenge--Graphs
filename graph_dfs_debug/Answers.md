Describe the fixes you made to the Graph implementation here.

The bug with the randomize button is that you named the the button function `onButton` but in render you called `this.Button`. You need to call it by the function name you gave it. 

