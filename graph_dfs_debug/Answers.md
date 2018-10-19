Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seems to connect, my edges aren't showing up.

The bug is in the add_edge function of the Graph class. First we must check to see if we have a starting or ending node. If we already have the starting node, we don't need to add the start again, but the ending node instead. Likewise if the edge is Bidirectional, we would already then have the ending node, so we add the starting node to point the edge in the other direction as well.