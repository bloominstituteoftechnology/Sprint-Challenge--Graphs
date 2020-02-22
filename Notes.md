
A) IMPORTS
1. Stack & Queue from Utils
2. Random

B) SETUP
1. Make Reverse Direction Dictionary

C) STEPS
1. Initialize Stack
2. Add Players current room to stack
3. Initialize Visited_rooms dictionary

4. WHILE loop w/ conditions 
- condition_1 = s.size() > 0

4.1. Get curr_room from Stack

4.2. Add curr_room to visited rooms
4.3 Get all available exit directions
4.4. Get all rooms in those available exit directions
4.5 Update the current room in the visited rooms dictionary w/ the apporpriate adjacent rooms

4.6 Pick random direction to move to
4.7 Update traversal path

4.8 Move player in that direction
4.9 Add new room to Stack





8. Get movement options
9. Pick random direction
10. Move in that direction
11. Add direction to Traversal Path 
12. Add room to stack


