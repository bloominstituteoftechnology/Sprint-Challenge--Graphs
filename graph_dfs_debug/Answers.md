Describe the fixes/improvements you made to the Graph implementation here.

1. When adding an edge the end and start inputs were just adding to themselves, when they should have been swapped.

2. The visited nodes were not being added to the set which is returned for the components method

3. This has to do with the either the recusion method not knowing when to quit/break or not having had logic to stop in a cycle for the dfs.

4. This was implemented, when the target node is found the function prints it to the console. When setting the current node we just needed to check to see if it was our node we were looking for.

5. Fixed Python standard pep stuff

6. I renamed the variable mainly in th esearches to more meaningful names.

The recursive functio works. We had to add the current node to a set and add logic to check if the current node had been visited yet. When all the component nodes were added we knew to return.
