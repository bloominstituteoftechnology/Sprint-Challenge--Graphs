Describe the fixes/improvements you made to the Graph implementation here.

– Updates to Vertex class:
    – remove component, add edges 
    – change repr to return edges
    – added x, y plus logic for them

– Updates to Graph class:
    – deleted components
    – changed add_vertex to create new instance of Vertex passing label
    – fixed up add_edge to add the right vertices to edges
    – fixed dfs to iteratively run through vertices to find target