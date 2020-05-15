from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


traversal_path = []



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

#ADDING MY CODE UNDER HERE BECAUSE I NEED TO MAKE USE OF VISITED_ROOMS

#dictionary for steps forward
moving_forward = {
    'n': 'e',
    'e': 's',
    's': 'w',
    'w': None
}
#dictionary for steps backwards
back_it_up = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}
#create a path stack
path = ['n']
#while the length of the stack is greater than 0
while len(path) > 0:
    #assign a veriable to pop off the stack
    moving = path.pop()
    #now I want to call player.travel passing in the variable I just created 
    player.travel(moving)
    
    # now if player.current room has not been visited
    if player.current_room not in visited_rooms:
        #append to traversal_path the dictionary for the steps to go back with the variable we made above as the indicies
        traversal_path.append(back_it_up[moving])
        # also append it to our path stack
        path.append(back_it_up[moving])
        # and add the current room to our visited rooms
        visited_rooms.add(player.current_room)
    
    # for our new_direction in [n,s,e,w]
    for new_direction in ['n', 's', 'e', 'w']:
        #we want to go to a new room, by calling get_room_in_directions(new_direction)
        next_room = player.current_room.get_room_in_direction(new_direction)
        #if new room exists and is not in visited
        if next_room and next_room not in visited_rooms:
            #append our new direction to traversal_path
            traversal_path.append(new_direction)
            #and also append it to our path stack
            path.append(new_direction)
            #time to break ;)
            break

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
