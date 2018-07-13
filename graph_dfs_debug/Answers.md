Describe the fixes you made to the Graph implementation here.

#App.js

I slightly decreased the boxSixe radius. 

I formatted the stroke and fillStyle of the vertexes with color. 

I changed the vertex drawing functions to all be under 1 for loop. 

I corrected the canvas width to correctly render the width. 

I added the 'getConnectedComponents' as a state funciotn under the App constructor. 

I corrected the incorrectly rendered Button fucntion to correctly render the 'onClick' funciton. 

#graph.js

I centered the vertex text. 

I defined an empty state vertex array under the randomize function. 

I unstringified the x and y grid coordinates used in their defintiions under the randomize funciton. 

I removed the destack shift funciton. 

#routing.js
I added default states to the vertex constructor, setting searched to false, and parent to null. 

Implemented the findVertex function with a for loop and a nested if statement. 

Implemented BFS pushing to a queue array while going edge to edge through the levels of the vertexes stack. 

Implemented an output route funciotn to view the output values via console.log. 

#generally formatted all docs with some spacing adgustments. 