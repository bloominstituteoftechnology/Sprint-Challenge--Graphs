# Help!

Hi Friend,

After learning about breadth-first-search, I decided to give depth-first-search
a try.  I'm pretty sure I've almost got it working, but I can't figure out the
last few bugs.  Can you help?  I've got the following issues.  I'm not sure if
the order here matters, you might have to fix them in a different order than
they are listed. I think these are all problems with `graph.py`.

1. Nothing seems to connect, my edges aren't showing up.
    
    graph.py
    a. In your add Graph class, you are attempting to create edges. You should be instantiating a vertex object using the Vertex class instead.
    b. Using start twice in your edge creation, instead of creating a start and end. 
    c. Missing set() creation for edges in Vertex class. 
    d. Removal of str() from Vertex class self.label maker. 
    e. Added catch for add_edge in case vertex does not exist. 
    f. Seperated directional and bi-directional edges into two functions for ease of calling and code clarity.  
    g. Adjusted parameters in functions accordingly with code changes. 
    h. You'll notice an x/y randomizer in the Vertex init class. This exists to give random locations to the Bokeh class for x/y coordinates to be created to represent the location of the nodes randomly. 
    i. I'm not clear on what you are attempting to do with your find_components function. If you are searching for edges, I'm not entirely sure why. I have commented this out in the meantime. 
    
    graph_demo.py
    a. Created seperate functions for default and random graph creation. 
    b. While it was good that you were instantiating a graph object from your Graph class
    c. When calling graph creation, you just need to pass in your graph object to BokehGraph() and then call draw. 
    d. Keep your main function as a juncture where you direct the call of either default or random graphs.
    e. Use your __name__ == '__main__' to interpret your user's input when they call the program. Currently there is nothing equating inputs with functionality/appropriate variables to be called on the program. Adjusted to allow for style, nodes and edges to be defaulted, adjusted or randomized. This may not be perfect still, so will require you to do a little more work, but it is functional.  
    f. I had to do quite a bit of restructuring here to make this portion functional, but I think you should be able to work through understanding most of it.
        - In broad strokes, in the function, createRandomGraph, I am first creating the same number of edges as necessary for the nodes, shuffling them and then picking a random number of them to generate random edges. Then I'm applying that edge set to the graph using the add_edge function.

    draw.py
    a. Don't seperate all the bokeh components into their own functions. You need to be able to call self.draw on the graph object you've created to apply the graph object to Bookeh's code. I condensed these accordingly. 
    b. Adjusted excessive class properties and params in __init__. 
    
2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.
    a. It's hard for me to discern exactly what you were attempting to do. I like the attempt to create multiple functions for different aspects of the graph, but you might be better off simply getting bokeh to function first and then building out from there. In this vein I refactored the code and included broad explanations. I also left your code in there, commented out at the bottom, so that you can compare.

3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
    a. This is likely due to your recursive attempt at dft. You need to make sure you always have a solid base case or your stack will overflow. 

4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.
    a. I am assuming you are talking about your dfs? Please be more specific with your references as I'm not sure what "it" is. 
    b. Assuming you are referencing your dfs funciton, I have commented yours out and replaced it with a functional version. You were on the right track, but a couple things:
        - Unless you are creating a path, I would stay away from using sets, and even then, you are better off with lists. 
        - 

5. My editor sure is complaining a lot about something called "lint."
    a. You need to install linter and a linting software, like flake8. 

6. I keep losing track of my variables, I guess I should name them better?
    a. Yes, your variables should be named in the most straightforward fashion possible and kep consistent throughout the program. For example, you named your edges components in your Vertex class. Keep them as edges. 

7. I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck. It was running forever so I tried adding a thing to keep
track of vertices, and now I just get an error message. Please try to fix this
too if you can, or at least give me some pointers on what I should be doing.
    a. You are not maintaining a reference to your visited nodes, so there is no way to create a base case to stop the recursion. This is likely why you are experiencing the endless cycle when trying to run it. 
    b. I have kept your version commented out to compare with the one I wrote. You'll notice that I am doing two main things: 
        - reseting the starting node to the child node each recursion
        - appending the starting node to the visited list each recursion j
    c. Also note that this is a dft. Recursions are very, very hard to do on bft and, therefore, are not approached in this manner. 




I'm still trying to learn this stuff, so please don't just fix the code for me.
Let me know in the `Answers.md` file where my bugs are and what you did to fix
them, so I can have an easier time watching out for them next time. Oh and don't
forget to `pipenv install` and `pipenv shell`!

00. Stretch: 
If you get all this figured out, it'd be great if you could also help try to
improve the `randomize()` in `BokehGraph` so I can draw vertices that don't
overlap (*i.e. stretch goal*).

Thanks!
