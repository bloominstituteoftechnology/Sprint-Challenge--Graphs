Describe the fixes/improvements you made to the Graph implementation here.

Hey there :)

I've only found a couple of things I'm sure you would've found yourself eventually!
For example in the *add_edge* method we were adding the index as an edge to itself. 
I think this is the reason no edges showed up! 

Also in your find_components method we are looking for vertices that aren't yet in our visited set! 
You had a slight mishap in your if-statement so that it would never fire and thus not color your components! 

For the recursive DFS we needed to add our base cases (do not recurse over any vertex twice & stop when we found our target)

For the DFS method that was utilizing a stack I've only changed the way it adds and takes off the stack. Take a look at it, I'm sure you'll spot the differences at once.

I've also taken the liberty to assign meaningful names for the variables you used throughout your solution, it's important for us to keep our code reabable.
Think of it as more of a curtesy for you, when maintaining the program as well as the next developer who will be working on this.