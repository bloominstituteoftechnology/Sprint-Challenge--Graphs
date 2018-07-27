Describe the fixes/improvements you made to the Graph implementation here.

This: https://help.github.com/articles/comparing-commits-across-time/

1. In the Graph.add_vertex fuction you are adding self connecting edges. You need to switch the add calls.
2. You needed to return the set of nodes you visited. Not the empty list of nodes the algorithm needed to visit.
3. If the graph is a cyclic graph, has a loop in it, you just follow that loop forever. You need to remove vertices you already visited with set differencing.
4. Here you are checking for equality against all the vertices you are planning to visit, not the current vertex. I changed to check against current_vertex (formerly z)
5. Its mostly a style thing, you're editor should tell you what to do about each one. Largely about spacing, but it can help you catch unused imports and unreferenced functions.
6. I renamed the one letter vars to things like to_visit, visited, current_vertex. Mostly consistent across functions and descriptive enough without being too verbose.
7. Firstly, you are calling a function that belongs to the graph class, this was hinted at by the linter. You have to change it to self.rec_graph. Also You don't append to sets, you update them. You still need to keep track of what you have visited. This could be done by splitting it into two functions. One to initialize the visited set, and the other a recursive function that takes in a visited set. But we don't need to split it into two functions. We can just have it be a default argument that is equal to None. If it is None, we initialize a visited set, then pass that in to the next call. The two if statements (check target, check is first call) on every call might not be terribly efficient. If that really mattered, python might not be the best language. Perhaps consider pypy or writing a python extenstion in another language.