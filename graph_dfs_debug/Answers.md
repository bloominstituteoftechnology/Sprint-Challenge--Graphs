Describe the fixes you made to the Graph implementation here.

#App.js updates
1. Changed Canvas fillStyle to `grey` from 'white' so I could see canvas in browser

2. Updated canvasWidth and canvasHeight by adding +1 to x and y count in order to fit the graph better

3. Under 'Draw the Verts on top' I changed the fillStyle from #77f to 'color' so verts would have different colors versus staying all the same.

4. Under 'Handle Button Press' I fixed the onClick command in order to make the Random button function properly. 'this.Button' needed to be 'this.onButton' so randomize button now works.

5. Under 'Render' I fixed width to equal {canvasWidth} within the brackets as it was marked incorrectly as canvasHeight.  