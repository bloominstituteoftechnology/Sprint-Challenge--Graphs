
A) IMPORTS
1. Stack & Queue from Utils
    - Stack = DFS
    - Queue = BFS (to get back to a room with unused exits)
2. Random
    - To pick a random direction out of available unused exits for DFS 

B) SETUP
1. Make Backtrack Dictionary
2. Initialize Visited_Rooms Dictionary

C) Helpers
1. ```unused_exits()``` => Find Valid Moves
    - Input: Current_Room, Visited_Rooms
    - Output:
        - all valid directional options (n / s / e / w) from the current room 
        - FALSE if none => triggers backtracing
2. ```random_direction``` => picks randomly from ```unused_exits```

D) STEPS
1. Initialize Stack
2. Add current room (starting room) to the stack

3. __Main__ WHILE loop
    - Goal: visit every room!
    - While loop translation: len(visited_rooms) < len(world.rooms)

    A1. Pop next room from stack
    A2. Add current_room to ```visited_rooms``` dict
    A3. Add all adjacent rooms connections to current_room in ```visited_rooms```

    B1. CALL: ```unused_exits()``` on current room
        - Output:
            - Filtered directional moved
            - False (if all adjacent rooms have already been visited)

    B1 != FALSE: ```CONTINUE DFS```
        A. CALL: ```random_direction()```
        B. Update ```traversal_path``` dict
        C. Move player in chosen_direction
        D. Add new current_room to stack


    B1 = FALSE: ```START BACKTRACKING```



    



4.6 Pick random direction to move to
4.7 Update traversal path

4.8 Move player in that direction
4.9 Add new room to Stack





8. Get movement options
9. Pick random direction
10. Move in that direction
11. Add direction to Traversal Path 
12. Add room to stack


