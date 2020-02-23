
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
2. ```random_direction()``` => picks randomly from ```unused_exits```
3. ```backtrack()``` => BFS to get back to a room with ```unused_exits```

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


    B1 == FALSE: ```START BACKTRACKING```
        A. Initialize Queue for directional path generation
        B. Get all available moves from the current_room
        C. Enqueue all available moves
        D. __MAIN__ WHILE loop
            - Goal: generate all paths until room has ```unused_exits```
            - While loop translation: queue.size() > 0

            D1. Dequeue to get current Path
            D2. Travel to end of that path from current room
            D3. CALL: ```unused_exits()```
                D3 != FALSE
                    - return path

                D3 == FALSE
                    - For each possible move from current test room
                        - copy current path
                        - append filtered backtrack move
                        - enqueue the updated paths









<!-- OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD
OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD
OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD
OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD
OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD -->

        A. Initialize Queue
        B. Add current room (starting room) to the queue
        C. Initialize ```backtrack_traversal_path```
        D. __MAIN__ WHILE loop
            - Goal: Continue backtracking until the current_room has `unused_exits``` => then BREAK out of while loop and return path from backtrack
            - While loop translation: q.size() > 0

            D1. Dequeue next room from queue
            D2. CALL: ```get_exits()```
            D3. Add ```available_backtrack_directions``` to queue

            D4. Dequeue a direction => test_direction
            D5. CALL: ```unused_exits()``` on ```current_room.get_room_in_direction()```

            D5 != FALSE: ```STOP BACKTRACKING```

            D5 == FALSE: ```CONTINUE BACKTRACKING```





    



4.6 Pick random direction to move to
4.7 Update traversal path

4.8 Move player in that direction
4.9 Add new room to Stack





8. Get movement options
9. Pick random direction
10. Move in that direction
11. Add direction to Traversal Path 
12. Add room to stack


