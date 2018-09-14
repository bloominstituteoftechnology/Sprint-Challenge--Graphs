Describe the fixes/improvements you made to the Graph implementation here.


 ##graph.py
 * installed pylint
 * installed autopep8
 * if you continue to get linter errors, you should consider following the python style guidelines https://www.python.org/dev/peps/pep-0008/

 #Graph class fixes -

 #Add edge method updated
 * line 22/24 updated with correct start/end variables
 * added test edges (uni and bi) at bottom of file, returns correctly as example below:
   {4: {8, 6}, 6: set(), 8: {4}, 10: set()}

#dfs method updated
 * updated variable names
 * return current instead of break

 #graph_rec method updated
 * added visited list parameter to method to replace x variable
 * updated to return true if target found
 * added exception handling if values not supplied
 * updated with working recursive call on child nodes



 




 