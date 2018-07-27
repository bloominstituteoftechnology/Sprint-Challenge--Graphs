Describe the fixes/improvements you made to the Graph implementation here.

### `graph_demo.py`

1. Add `component=num` to num in range loop of `graph_demo.py` for Vertex creation
2. Added an edges set to check for duplicate edges in edge creation loop in `

### `graph.py`

1. Remove `__repr__` "Vertex" addition for readability
2. Correct start/start, end/end to start/end, end/start in `add_edges`
3. Rename variables in `dfs`
4. Remove `graph_rec` fn