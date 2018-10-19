Describe the fixes/improvements you made to the Graph implementation here.
--------------------------------------------------------------------------------------------
graph.py
---------
in def graph_rec

1) changed x to [] (was set())
2) change recursion call to SELF.graph_rec(v) (was missing self.)


