Describe the fixes/improvements you made to the Graph implementation here.

– Added Queue and Stack classes to use them for algorithms

– Updates to Vertex class:
    – remove component, add edges 
    – change repr to return edges
    – added x, y plus logic for them

– Updates to Graph class:
    – deleted components
    – changed add_vertex to create new instance of Vertex passing label
    – fixed up add_edge to add the right vertices to edges
    – fixed dfs to iteratively run through vertices to find target, removed default assignment of None from target
    – fixed graph_rec to be a recursive dft, changed target to visited and added if statements.