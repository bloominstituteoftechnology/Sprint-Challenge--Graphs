
Describe the fixes/improvements you made to the Graph implementation here.
Whats going Mr. Bug.  After taking a zip of my joe I noticed you didnt install "Bokeh" ran a little quick "pip3 install bokeh" and boom, you are in business.  Graph now prints. 
In "def _setup_labels" made the following changes.  in Line 8- I added " vertex, position in self.pos.items().  in line 81 changed append to "position [0]" and line 82 changed the append to "position [1]" line 83, I changed the .append to take a string of (str(vertex)) as Bokeh usually has issues with strings

Line 40 you had in self.vertex_list.  we need to have self.vertex_keys.  this affected line 36 (draw.py) as we has self.vertex_list and it needs to be "_keys" as we already had list set up here.  changed to "self.vertex_keys".

in  def_get_connected_component_colors (line 107): self.vertex_list needs to be self.vertex_keys

line 97 (draw.py) changed self.vertex_list to self.vertex_keys 