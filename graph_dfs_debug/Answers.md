Describe the fixes/improvements you made to the Graph implementation here.

Updated add_edge to add the end to the start and vice/verse.

updated dfs() to make variable names readable, swapped stack and current where needed, then added current to visited, now it removes visited to avoid any duplicates, then finally now we return the visited as our result. 

all I had to change in find components was the if statement to check if the vertex is NOT in visited. 

in graph_rec swapped append with add, made variables make a bit more sense, and finally called graph_rec on self to check visited.