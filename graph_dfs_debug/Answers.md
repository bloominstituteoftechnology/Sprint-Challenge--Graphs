`I changed the `add_edge` function so that the end vertex is now added to its starting key (the reverse for when vertices are bidirectional).`

`A `not` was missing from the `if` in the `for` loop of `find_components`, so no vertex ever made it to the `dfs` function.

In the `dfs` function, there were a few things wrong. The variables were too unspecific, so I renamed them to make the flow of the function easier to follow. I started `stack` off with the `start` vertex already appended. I changed `break` to `return True` so the function could double as a search (even though traversal and search should really be separate functions). Finally, I made sure checked vertices are added to the `visited` set and `visited` vertices are subtracted from `stack`.`

`For `graph_rec`, I first changed the names of the function and several variables to make their purposes clearer. Then I added `visited=None` as a default argument, with a value check at the start of the function so the recursed list can be passed through. I added a check for `target` even though (as I said before) traversal and search should really be separate functions. Finally, I then added a check for inclusion in `visited` before the recursive call.
