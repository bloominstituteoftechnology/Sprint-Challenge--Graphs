Describe the fixes you made to the Graph implementation here.

In App.js

- To fix the random button not functioning line 158 was not calling the right method on click so I fixed ```onClick={this.Button}``` to ```onClick={this.onButton}```