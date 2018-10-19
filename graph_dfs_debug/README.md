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
    
    graph_demo.py
    a. Created seperate functions for default and random graph creation. 
    b. While it was good that you were instantiating a graph object from your Graph class
    c. When calling graph creation, you just need to pass in your graph object to BokehGraph() and then call draw. 
    d. Keep your main function as a juncture where you direct the call of either default or random graphs.
    e. Use your __name__ == '__main__' to interpret your user's input when they call the program. Currently there is nothing equating inputs with functionality/appropriate variables to be called on the program. Adjusted to allow for style, nodes and edges to be defaulted, adjusted or randomized. This may not be perfect still, so will require you to do a little more work, but it is functional.  

    draw.py
    a. Don't seperate all the bokeh components into their own functions. You need to be able to call self.draw on the graph object you've created to apply the graph object to Bookeh's code. I condensed these accordingly. 
    b. Adjusted excessive class properties and params in __init__. 


2. All the vertexes are the same color.  They're supposed to be different colors
if they're not connected, and right now none of them are.
- 
3. Sometimes I do something and when I run `python graph_demo.py` it just takes
forever, even though my `draw.py` and `graph_demo.py` are totally just the same
as from class.
- 
4. I wanted to let it find a target vertex, but even back when it did kinda run
this part didn't really work.
- 
5. My editor sure is complaining a lot about something called "lint."
    a. You need to install linter and a linting software, like flake8. 
6. I keep losing track of my variables, I guess I should name them better?
    a. Yes, your variables should be named in the most straightforward fashion possible and kep consistent throughout the program. For example, you named your edges components in your Vertex class. Keep them as edges. 

7. I also tried to do it with recursion instead of a stack, in `graph_rec`, but I
got even more stuck. It was running forever so I tried adding a thing to keep
track of vertices, and now I just get an error message. Please try to fix this
too if you can, or at least give me some pointers on what I should be doing.
- 

I'm still trying to learn this stuff, so please don't just fix the code for me.
Let me know in the `Answers.md` file where my bugs are and what you did to fix
them, so I can have an easier time watching out for them next time. Oh and don't
forget to `pipenv install` and `pipenv shell`!

00. Stretch: 
If you get all this figured out, it'd be great if you could also help try to
improve the `randomize()` in `BokehGraph` so I can draw vertices that don't
overlap (*i.e. stretch goal*).

Thanks!
