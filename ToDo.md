# Sprint Challenge: Graphs

There are two parts to this sprint challenge:

 * `graph_dfs_debug`: Inside this directory, you'll find an implementation of the Graphs project we worked on this last week, but it's not functioning as it should. Your job is to fix the listed issues so that the code works properly. You'll also need to document your changes in the provided `Answers.md` file. 

    * [ ] 1. Nothing seems to connect, my edges aren't showing up.
    * [ ] 2. All the vertexes are the same color.  They're supposed to be different colors
    if they're not connected, and right now none of them are.
    * [ ] 3. Sometimes I do something and when I run `python graph_demo.py` it just takes
    forever, even though my `draw.py` and `graph_demo.py` are totally just the same
    as from class.
    * [ ] 4. I wanted to let it find a target vertex, but even back when it did kinda run
    this part didn't really work.
    * [ ] 5. My editor sure is complaining a lot about something called "lint."
    * [ ] 6. I keep losing track of my variables, I guess I should name them better?

 * `graph_shortest_path`: For this part, you'll be extending the functionality of the breadth-first-search traversal algorithm we worked on so that it's able to find the shortest path between two input graph nodes. You'll find further instructions in the README in the directory.

 ## Procedure

    * [ ] 1. Perform a BFS from the _ending vert_ (host). This will set up all the
      `parent` pointers across the graph.

    * [ ] 2. Output the route by following the parent pointers from the _starting_ vert
      printing the values as you go.


    ## Sample Run
    * [ ] $ python routing.py HostA HostD
          HostA --> HostB --> HostD
    * [ ] $ python routing.py HostA HostH
          HostA --> HostC --> HostF --> HostH
    * [ ] $ python routing.py HostA HostA
    HostA
    * [ ] $ python routing.py HostE HostB
          HostE --> HostF --> HostC --> HostA --> HostB
