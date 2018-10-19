Describe the fixes/improvements you made to the Graph implementation here.

1. Your add_edges function was not adding the second points to the edges so they wouldn't actually connect. I changed the add_edges function to add ends to directional edges and starts to bidirectional edges.

2. The find_components function was looking for vertices that were list in visited list. I updated the find_components function to check for vertices NOT included in the visited list thereby changing the colors of the vertices not connected to each other.

3. 
4. 
5. 
6. Having proper names not only let you track them and their jobs easier, but it makes it so others reading your code can read them better too. I unpdated the variable names to be more relevant to what they are.
7. The graph_rec function was not checking for previously visited vertices. And with no target to look for the loop could potentially go on forever. So I changed the recursive function to keep track of visited vertices as well as giving it a check against a target to make sure the loop will eventually end.