Describe the fixes/improvements you made to the Graph implementation here.
## Steps taken
1. Run graph_demo
2. Notice that there are no edges in this graph. 
3. Put error messages in, found that we're not passing some key variables 
to the functions in `graph_demo`.
4. Add some error messages to the `add_vertex` function in `graph` file so
we know for sure that we're adding the right thing.
5. Mod `add_edge` function - add end to start and vice versa.
6. Run `graph_demo`, still getting errors.
7. Replaced search functions with working code from lecture - bfs/dfs
returns `visited`, which our `find_components` function is looking for. 
8. Add more error messages and print statements to `main` function of
`graph_demo` - apparently we're not passing 4 args. Our primary variables are
 not defined. 
 9. 