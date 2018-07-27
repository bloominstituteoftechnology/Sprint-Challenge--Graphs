Describe the fixes/improvements you made to the Graph implementation here.

RE: linting:
I used my formatter out of habit to make a first commit for my pull request, so I'll have to guess at what the errors are based on the difference between the original code and the saved code with the knowledge I have of flake8 errors.

1) My particular linter does not like when lines are overly long (I believe it caps it at 80, though I've set it to allow up to 120 for situations where my formatter cannot split a line properly), so the import from bokeh.models was too long and had a lot of unnecessary white space, which is a big no-no for linting.

2) I don't know if it's a linting preference or my formatter's preference, but in cases where there are multiple variables declared, the declarations were changed to be one per line to aid in readability.

3) Single quotes were changed to double quotes, though pep8 has no preference on the type of quotation used, Black does have a preference and it's good to be consistent.

4) Removed extra whitespace between functions.

5) Indentation added to distinguish indentation.

RE: Documentation:
1) I'm adding some documentation to your classes to indicate what attributes are inherent in a given class.

RE: Error handling:
1) I added some error handling so that a person can't add a vertex if it's not actually an instance of the Vertex class.

2) I added some error handling so that a person can't add a vertex if it already has been added.  It's good to enforce things so that duplicates aren't present in your dataset.

3) I added some error handling so that a person can't add an edge if the vertices involved aren't in the graph.  You don't want random lines anywhere, unconnected to anything.  

RE: Naming Variables
1) In your depth first search, since you're implementing a stack, it's best to choose variable names that communicate what you're doing.  I changed your `x` variable to `stack`, your `y` variable to `visited`, and your `z` variable to `current`.

RE: Corrections:
1) In your depth first search, probably due to your variable naming scheme, you ended up having an `if stack == target` rather than `if current == target`.  This has been corrected.

2) Also in your depth first search, you had the equivalent of `stack.extend(self.vertices[current])` - this adds all of the edges from the current vertex to the stack.  In order to avoid revisiting a vertex, it's important to subtract the visited vertexes from the current vertex's edges before adding them to the stack.  This has been changed to `stack.extend(self.vertices[current] - visited)`

3) You said in your notes that you wanted to let it find the target vertex, but didn't actually specify if you wanted to then return the target vertex, so I changed the `break` to `return target`.  Feel free to change this back if you really just wanted to use a `break` there.

4) That recursive function was a doozy.  I ended up adding a parameter to the method to keep track of the `visited` variable, which you originally had as `x`.  Also, your for loop needed to be changed to subtract visited.  That's the reason you kept geting errors, you were exceeding the maximum call stack (you were infinitely looping).  So your recursive call now passes the edge and the visited list (which I kept as a set).

5) In finding_components, you were checking to see if the vertex was in visited, so the method actually terminated abruptly (since visited starts as an empty set).  I changed it so that it now checks if the vertex is not in visited.