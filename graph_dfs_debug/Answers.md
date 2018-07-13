Describe the fixes you made to the Graph implementation here.

#App.js updates
1. On line 43 I changed Canvas fillStyle to `grey` from 'white' so I could see canvas in browser

2. On lines 12 & 13 I updated canvasWidth and canvasHeight by adding +1 to x and y count in order to fit the graph better

3. On line 62 I updated 'Draw the Verts on top' by changing the fillStyle from #77f to 'color' so verts would have different colors versus staying all the same.

4. On line 159 under 'Handle Button Press' I fixed the onClick command in order to make the Random button function properly. 'this.Button' needed to be 'this.onButton' so randomize button now works.

5. On line 122 under 'Render' I fixed width to equal {canvasWidth} within the brackets as it was marked incorrectly as canvasHeight. 

#Graph.js updates
1. Commented out line 135 for de-stack as it is not needed. This also fixed the issue of the graph drawing in a 'crazy' way.