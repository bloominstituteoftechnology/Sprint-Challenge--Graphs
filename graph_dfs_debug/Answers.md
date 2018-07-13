Describe the fixes you made to the Graph implementation here.

1. In graph.js I removed a call to shift on the stack because it's not needed.
1. In app.js I fixed the naming for the onclick function
1. In app.js the canvas width was using height so I changed to to use the width