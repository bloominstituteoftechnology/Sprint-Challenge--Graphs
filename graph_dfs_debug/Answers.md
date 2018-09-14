Describe the fixes/improvements you made to the Graph implementation here.

 ##graph.py
 * added test graph at bottom of file 
 * installed pylint
 * installed autopep8

 #Graph class fixes -
 #Add vertex method updated
 * line 18 removed edges from method parameters
 * line 19 initialized set without edges
 * added test vertex example at bottom of file, returns correctly
   {4: set(), 6: set(), 8: set(), 10: set()}

 #Add edge method updated
 * line 22/24 updated with correct start/end variables
 * added test edges (uni and bi) at bottom of file, returns correctly as example below:
   {4: {8, 6}, 6: set(), 8: {4}, 10: set()}
 




 