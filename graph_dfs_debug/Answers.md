# Fixes

I've made the following changes to your files:

1. The connections were not showing up because the edges were pointing to themselves, so I've changed them to point to each other.

2. The connected colors were not showing up because the condition in the `find_components` needed to do it's thing when the vertex hasn't been visited (i.e., `not in`)

3. Your script may have been hanging on the dfs and other operations in the `graph.py`, so that could have impacted the performance of your script in spite of the other files being the same as those given in class. 

4. I replaced the break in your dfs so that you can return the target vertex when it is found.

5. The "lint" messages are coming up due to your code not conforming to style and structure conventions that make your code easier to read and less prone to errors. I would look up these errors to make your code more bulletproof and make collaboration with other developers easier.

6. I have changed values like `x` and `y` into more descriptive names so you do not lose track of variables.

7. I have added a generic recursive approach to dfs. One thing to note is that the recursive function has to receive `visited` as an argument so that it can keep track of what has been visited as it loops onto itself.