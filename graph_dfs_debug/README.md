##**THIS EXERCISE IS OPTIONAL FOR CS7**

##DO NOT BEGIN UNTIL YOU HAVE COMPLETED ROUTING.JS

#Help!

Hi Friend,

After learning about breadth-first-search, I decided to give depth-first-search a try.  I'm pretty sure I've almost got it working, but I can't figure out the last few bugs.  Can you help?  I've got the following issues.  I'm not sure if the order here matters, you might have to fix them in a different order than they are listed.

1.  The graph draws crazily.
2.  All the vertexes are the same color.  They're supposed to match the color of the edges for each connected component.
3.  My randomize button is broken.
4.  It looks like part of the graph is getting cut off.

I'm still trying to learn this stuff, so please don't just fix the code for me.  Let me know where my bugs are and what you did to fix them, so I can have an easier time watching out for them next time!

Thanks!

----

Going in order of stated problems...

1. There was an extra array `shift` employed in the `dfs` method, probably a carry-over from the breadth-first search. As we're using a stack, rather than a queue, _and_ we're already popping out the item in the stack we need, there's no reason to also remove the first element from the stack.
2. The vertex colors were not receiving the `color` argument in the `drawVerts` method. This was originally set to `ctx.fillStyle = '#77f'` which will always lead to a static color choice. Changing this to `ctx.fillStyle = color` allows it to receive the random color argument being passed in.
3. This was a simple typo, the button was originally set to call `this.Button` which is not an available method. There is, however, an `onButton()` method available, so setting this to call `this.onButton()` will allow random graph generation. Alternatively, the method itself could be renamed to `button()` if preferred.
4. This is because the graph generation is expecting a square of equal height and width. The original dimensions were set to a width of 4 and a height of 3, which is why the right side gets cut off. This can be solved by either providing equal dimensions for the graph, or refactoring to allow for graphs of any width or height.

Additionally, in the future, including a `.gitignore` file is a good practice in order to avoid the possibility of pushing thousands of node packages to a repo. You can check the one added here for an example.