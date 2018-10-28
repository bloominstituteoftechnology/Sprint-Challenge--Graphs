Describe the fixes/improvements you made to the Graph implementation here.

I understand the concepts but I dont know how to implement it yet. This week was a rough one for me. Bellow is my understating of "Breath First Search" and "Depth First Search" and "Graphs"

# Graphs

Graphs are basically a collection of nodes.Each node can point to other nodes, either a one way point or a two way point. A one way point would mean you can only get to a single node from one direction. So you could go from node "A" to "B" but yu couldnt go from node "B" to "A". Two way point is the opposite. This means you could get to any node from any other node (Two-way).

# Breath First Search

So breath first search is a traversal algorithm. Which is a FIFO(First in first out). Which basically means that it finds every vertex that is reachable from the vertex its on, and it finds the distance from whatever vertex its was on as well. When implementing this, you need a Queue as well as a way to show that a vertex has been visited.

# Depth First Search

So depth first search is a recursive algorithm. Its similar to Breath First Search, but instead of a Queue you use a Stack. This means you go down the node tree touching every node until you find the node your looking for. SO if your starting at node "A" and want to get to node "F" you would ave to touch each node and its children until you get to were your going.
