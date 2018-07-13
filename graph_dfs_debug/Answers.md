Describe the fixes you made to the Graph implementation here.

App.js - fault: canvas height in the GraohView render was set to canvasWidth
  correction: switched canvasWidth to canvasHeight

App.js - fault: button was calling this.Button method instead of this.onButton
  correction: changed name of onClick function inside button element