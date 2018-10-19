Describe the fixes/improvements you made to the Graph implementation here.

in add_edge the edges were beging added to the nodes themselves, not other nodes. added start to end and end to start (if bisirection)