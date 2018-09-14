Describe the fixes/improvements you made to the Graph implementation here.


Hi Friend!
I was able to review your graph_dfs files and I think I can help. Let's go over the Issues list that you provided and find out what's going on.

ISSUES LOG:
1. Nothing seems to connect, my edges aren't showing up.
	If you look at your graph.py / def_add_edges function, it seems that vertices begins at "start", but connects to "start". Also, your bidirectional if statement says "end" to "end".  I changed it to say the following:

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start) //change to self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start) // self.vertices[end].add(start)
********************************************************

2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.

I think the problem lies in the graph_demo.py / def_main_ function.  You have draw_components to "True", but if  you take a look at the draw.py / def_init_, it says that draw_components is set to False(zero).  So BokehGraph can't tell to run if it's not equal to each other.

  graph_demo.py
    def main(num_vertices=8, num_edges=8, draw_components=True):  //change to False to match BokehGraph/def_init

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)  // Its can't understand to draw
    bokeh_graph.show()

  draw.py
    class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=100, height=100,
                 show_axis=False, show_grid=False, circle_size=35,
                 draw_components=False): // draw components = False.

*********************************************************
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.

I'm not sure what's happening.  In terminal, when I run 'python3 graph_demo.py #edges #vertices' and it seems that I'm fine to draw a graph quickly.  Maybe adding too many #vertices(100)/#edges(100) may make it run forever?

*********************************************************
4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.

In graph.py / def dfs, since dfs are like stacks it was easier to change 'x' to be named 'stack' since we're doing a depth-first search, renamed 'y' to be 'visited', which are vertices that been checked during the search, and renamed 'z' to be 'current_vertex' which temporarily holds the vertex(nodes) that we pop from the stack for because its searching.  The reason why I was chose to rename it that it helped me understand whats happening in dfs code (since its a stack the renaming could help understand who are the players) and potentially help again in future state if we need to go back and review the code again.

Next, I checked out the while loop. It's might be easier to have it populate the vertices into a queue that "start", then appending to an empty queue.

def dfs(self, start, target=None):
        stack = [start]
        visited = set()

        while stack:  //easier to understand that the when the searching for target.
            current_vertex = stack.pop()  //take current vertex in queue and check it
            if current_vertex == target:  // if its the target then stop
                break
            visited.add(current) //if not the target, then mark and put in back in queue
            stack.extend(self.vertices[current_vertex] - visited) // go through the queue and repeat
        return visited


        # x = []  //renamed "x" to "stack" and mark it to "start" instead of empty queue
        # x.append(start) //renamed "y" to "visited"
        # y = set(x)

        # while x:
        #     z = x.pop()
        #     if x == target:
        #         break
        #     x.extend(self.vertices[z])

        # return x
 *************************************************************
 5. My editor sure is complaining a lot about something called "lint."

 I'm not sure how to really give a good answer.  I have pylint in my editor and it works fine.  Maybe you can check the linter and see what's having with the linting behavior and then modify its setting?

 *************************************************************

6. I keep losing track of my variables, I guess I should name them better? I also tried to do it with recursion instead of a stack, in `graph_rec`, but I got even more stuck. It was running forever so I tried adding a thing to keep track of vertices, and now I just get an error message.

In graph.py / def graph_rec,  I renamed 'x' to be 'visited' and set to "start". like I did for #4.   I think graph_rec should be self.graph_rec(v).  It needs to remember itself.

    def graph_rec(self, start, target=None):
        visited = set(start) // renamed "x" to visited
        for v in self.vertices[start]:
            self.graph_rec(v)  //added "self"
        return visited

    # def graph_rec(self, start, target=None):
    #     x = set()
    #     x.append(start)
    #     for v in self.vertices[start]:
    #         graph_rec(v)
    #     return x













