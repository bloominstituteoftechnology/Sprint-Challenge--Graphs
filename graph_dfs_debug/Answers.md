
Describe the fixes/improvements you made to the Graph implementation here.

Whats going "Friend".  After taking a zip of my joe I noticed you didnt install "Bokeh" via pipenv so I ran a little quick "pip3 install bokeh" and boom, you are in business.  Graph now prints (and now to fix your bugs).

In "def _setup_labels" made the following changes.  in Line 8- I added " vertex, position in self.pos.items().  in line 81 changed append to "position [0]" and line 82 changed the append to "position [1]" line 83, I changed the .append to take a string of (str(vertex)) as Bokeh usually has issues with strings

Line 40 you had in self.vertex_list.  we need to have self.vertex_keys.  this affected line 36 (draw.py) as we has self.vertex_list and it needs to be "_keys" as we already had list set up here.  changed to "self.vertex_keys".

in  def_get_connected_component_colors (line 107): self.vertex_list needs to be self.vertex_keys

line 97 (draw.py) changed self.vertex_list to self.vertex_keys

Moving to fix your problems on graph.py:
in line 18 def add_vertex(self, vertex, edges=()):  you are not giving your graph the power to connect your vertices to edges. adding the following to do that on top of line 19 and added the following code: "if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')"
P.S no edges still but R-E-L-A-X, i got you.lets move now to the next function.

in your function "add_edge" on line 25, i am going to add the following code to add edges to your vertices should there be one.  will keep everything you have here except will add above line 26: if start not in self.vertices or end not in self.vertices:
            raise Exception('Connecting Vertices not in graph!')
lets stay here for a bit.  in line 28 and line 30 respectively.  in .add(start) needs to be (end) and in line 30 your .add(start) needs to be (end) as well. or else not bidirectional. with these fixes we now have EDGES.  lets continue down the line though.


lets look at your function def find_components (line 57) we will change "if vertex in visited" for "if vertex ""not"" in visited"(the change being "not").  fix prints and fixes the coloring too for vertices that are visited versus those that are not.

your depth first search function was missing two parameters.  added start on line 33 to "x" to represent "stack" and on line 41 added for "y" for your visited vertices to make the code more readable to the next developer (notes above code for a more robust explanation).

your function def graph_rec (recursive) on line 45-50 (graph.py) needs to be able to be read.  you are new so remember, try to make it so you can almost read it in english.  You also didnt define "v" in line 48.  lets just keep it simple and change it to "vertex".  Notice how now it looks very similar to your find_components function.  Line 50 was added to update the set thats being visited for this recursive function.

Presto!!!! we have fixed THEE!!!  Issues fixed.
