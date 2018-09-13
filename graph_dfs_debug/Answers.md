Describe the fixes/improvements you made to the Graph implementation here.


1. All the vertexes are the same color. They're supposed to be different colors if they're not connected, and right now none of them are.

- Fix: Add integer values when running the python test in gitbash where 0 is the third value passed. 
(e.g python graph_demo.py 10 10 0)

2. Nothing seems to connect, my edges aren't showing up.
    
    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)
    
    Fixed to:

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end) # changed value in add to end
        if bidirectional:
            self.vertices[end].add(start) # changed value in add to start


3. Sometimes I do something and when I run python graph_demo.py it just takes forever, even though my draw.py and graph_demo.py are totally just the same as from class.
- It is much faster now. 


4. I wanted to let it find a target vertex, but even back when it did kinda run this part didn't really work.
My editor sure is complaining a lot about something called "lint."
- Fix: To find a target vertex, do a dfs or depth first search. 


5. I keep losing track of my variables, I guess I should name them better?
- Fix: Changed names of variables into something easier to remember and descriptive of the values that they represent. For example, changing the variable x to the variable name stack. 