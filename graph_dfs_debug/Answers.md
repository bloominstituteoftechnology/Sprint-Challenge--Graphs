Describe the fixes you made to the Graph implementation here.
1. Connected components weren't color coded correctly. It was an issue with depth-first-search implementation. Call to .shift() as well as a call to .pop(). Fixed by removing extra shift call on line 135 in graph.js --   stack.shift(); // de-stack -- 

2. Was hard-coded on line 62, so changed the assignment to '' color '' , rather than the hard coded color that was in the code. 

3. Randomize button was broken because of typo. Fixed by changing line 158 as follows:
//        <button onClick= () => {this.Button()}>Random</button>

4. Canvas cut off. Changed line 122 in App.js to width-{canvasWidth}
