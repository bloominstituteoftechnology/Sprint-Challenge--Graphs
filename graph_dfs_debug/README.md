#Help!

Hi Friend,

After learning about breadth-first-search, I decided to give depth-first-search a try.  I'm pretty sure I've almost got it working, but I can't figure out the last few bugs.  Can you help?  I've got the following issues.  I'm not sure if the order here matters, you might have to fix them in a different order than they are listed.

1.  The graph draws crazily.
2.  All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.
3.  My randomize button is broken.
4.  It looks like part of the graph is getting cut off.

I'm still trying to learn this stuff, so please don't just fix the code for me.  Let me know where my bugs are and what you did to fix them, so I can have an easier time watching out for them next time!

Thanks!

## Solution
1. Problem in DFS implementation in `graph.js`. Line 131 should be `.unshift()` because stacks are FIFO. Line 139 is unneeded.
2. Line 62: The fill color is not set to the randomized color.
3. Line 158: The function to randomize is named `onButton`, but the button onClick fires `Button`.
4. Line 6-8: The size of the graph as defined in `App.js` ->  `xCount` and `yCount` is too small.