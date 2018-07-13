Describe the fixes you made to the Graph implementation here.

Dear Friend,

Below are my responses to your concerns and a list of changes I made. Please let me know if there's anything else I can help with.

1. The graph draws crazily.
    -I revised some of the variables so the width/height were pulled properly. See line 111 for example. Also, I commented out the stack shift line 136 on graph.js as it's unnecessary.

2. All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.
    - You needed to properly pass the color to the drawVertex function, which I updated.

3. My randomize button is broken.
    - You were calling a function `button` when u should have called `onButton`. 

4. It looks like part of the graph is getting cut off.
    - I revised the starting position of the graph in graph.js. You didn't have the position properly declared and i made the default -4 x -4 to give some extra padding.