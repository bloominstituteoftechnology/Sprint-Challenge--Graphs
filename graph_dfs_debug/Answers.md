Describe the fixes/improvements you made to the Graph implementation here.

*To prevent the linting message from popping up, just disable linting from the prompt that appears in your code editor.

* For your edges to show up, you need to change the parameter in your add method in your add_edge function. You need to change start to end because if you are starting out with a value, you don't want to add another starting value since you already have one. You need to do the same for if your edge is bi-directional as well.

* I also implemented a conditional to check and see if the random vertices that were being called already existed.

* If you want to make your code faster, you may want to implement a stack and/or queue instead of recursion for your graph.