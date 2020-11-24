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
go_back = {
    "n" : "s",
    "s" : "n",
    "e" : "w",
    "w" : "e"
}

def traverse_graph(current_room, visited=None):
    # Initialize path
    path = []
    # create a set of visited rooms if empty
    if visited == None:
        visited = set()

    # Traverse through each exit
    for possible_move in player.current_room.get_exits():
        # Travel to the next room
        player.travel(possible_move)

        # If current room is in visited
        if player.current_room in visited:
            # Use dictionary and current move to go back to previous room
            player.travel(go_back[possible_move])
        else:
            # Add current room to the visited set
            visited.add(player.current_room)
            # Append the move to the path
            path.append(possible_move)
            # Recursively call the method passing in the current room and visited set
            path = path + traverse_graph(player.current_room, visited)
            # Go back to previous room
            player.travel(go_back[possible_move])
            # Append move to path
            path.append(go_back[possible_move])

    # At end of loop, return the path
    return path

traversal_path = traverse_graph(player.current_room)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

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
