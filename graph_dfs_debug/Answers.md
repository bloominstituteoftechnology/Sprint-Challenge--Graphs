Describe the fixes/improvements you made to the Graph implementation here.

i renamed variables for their function, because seemingly you had them confused. in the search you were returning the queue after you emptied it.

you also were only edged from one vert to itself so a quick change in your add_edge function got that fixed up for you.
