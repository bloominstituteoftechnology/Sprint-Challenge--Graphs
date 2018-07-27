Describe the fixes/improvements you made to the Graph implementation here.

I have made comments to the changes I made in the source code so refer to that directly. After you understand and agree with the changes, please go ahead and remove them.  

In general try to explicitly name your variables to be what they stand for.

Here is the overall changes (only name changes shown here):

1.  function search: 
    variables changed:
        x -> stack
        y -> visited
        z -> current

2.  function graph_rec
    name of function changed:
        graph_rec -> dfs_recursion


3.  function find_components
