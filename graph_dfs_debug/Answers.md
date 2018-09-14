Describe the fixes/improvements you made to the Graph implementation here.
1. Nothing seems to connect, my edges aren't showing up.
    - graph.py line 22 & 24: in add_edge()  
        from// self.vertices[start].add(start)  
        fix to// self.vertices[start].add(end)  
        from// self.vertices[end].add(end)  
        fix to// self.vertices[end].add(start)  

2. All the vertexes are the same color.  They're supposed to be different colors
    - graph_demo.py line 13 in def main()  
        //from def main(.. draw_components=True):  
        fix to// def main(.. draw_components=False):  

3. Sometimes I do something and when I run `python graph_demo.py` it just takes forever, even though my `draw.py` and `graph_demo.py` are totally just the same as from class.
    - could not duplicate.  Likely already fixed by re-factoring.  

4. I wanted to let it find a target vertex, but even back when it did kinda run this part didn't really work.
    - refactored dfs & graph_rec  

5. My editor sure is complaining a lot about something called "lint."
    - for vs code, add `"python.linting.pylintEnabled": false` to settings.  

6. I keep losing track of my variables, I guess I should name them better?
    - renamed:  
        in dfs_rec()  
            x --> stack  
            y --> visited  
            z --> current  

        graph_rec() --> dfs_rec()  
            x --> visited  
            v --> child_vert  









