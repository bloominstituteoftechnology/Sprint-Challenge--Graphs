Describe the fixes/improvements you made to the Graph implementation here.

1. Nothing seems to connect, my edges aren't showing up.
Fixed add_edge method by having the start vertex add the end vertex, and the end vertex add the start vertex

2. All the vertexes are the same color. They're supposed to be different colors if they're not connected, and right now none of them are.
Fixed find_components method so it checks if the vertex is not in visited

3. Sometimes I do something and when I run python graph_demo.py it just takes forever, even though my draw.py and graph_demo.py are totally just the same as from class.
Fixed dfs method so nodes are taken from the stack and added to visited, otherwise the while stack loop will run forever

4. I wanted to let it find a target vertex, but even back when it did kinda run this part didn't really work.

5. My editor sure is complaining a lot about something called "lint."

6. I keep losing track of my variables, I guess I should name them better?
The variables in dfs and graph_rec methods were not descriptive so I changed the following variable names:
dfs:
x => stack
y => visited
z => current
graph_rec:
x => queue
v => vertex
