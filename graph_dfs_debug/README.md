#Help!

Hi Friend,

After learning about breadth-first-search, I decided to give depth-first-search a try. I'm pretty sure I've almost got it working, but I can't figure out the last few bugs. Can you help? I've got the following issues. I'm not sure if the order here matters, you might have to fix them in a different order than they are listed.

1.  The graph draws crazily.

In graph.js change `shift()` to `unshift()` in your dfs method

2.  All the vertexes are the same color. They're supposed to match the color of the edges for each connected component.

In App.js, set your fill color to `color` --- the output of the `randomHexColor()` function

3.  My randomize button is broken.

You have a typo in your return statement of App.js. It should be `onButton` not `Button`

4.  It looks like part of the graph is getting cut off.

Adjust `xCount`, `yCount`, `boxSize` and `radius` to get the desired result that doesn't cut off your graph.

I'm still trying to learn this stuff, so please don't just fix the code for me. Let me know where my bugs are and what you did to fix them, so I can have an easier time watching out for them next time!

Thanks!
