Describe the fixes/improvements you made to the Graph implementation here.
* Switch `start` and `end` argument for `add_edge` method in `graph.py`
* Change `dfs` method to:
```
x = []  
x.append(start)  
y = set()  
while x:  
    z = x.pop(0)  
    if z == target:  
        break  
    x.extend((i for i in self.vertices[z] if i not in y))  
    y.add(z)  
return y  
```
* In `find_component` method, change to `if vertex not in visited`