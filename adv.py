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
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# need a way to track visited rooms.
# need a way to record our path to remove later remove rooms we've visited and paths we've explored.
# track where the player has been and a path to reverse player direction
visited_rooms = {}
path = []

# set the current room exits in the visited room dict
visited_rooms[player.current_room.id] = player.current_room.get_exits()


while len(visited_rooms) < len(room_graph):
    # if room has not been visited
    if player.current_room.id not in visited_rooms:
        pass
        # add to visited
        # update current move to path - 1 in order to
        # remove it from the available moves for that room
    # if no exists or all explored
    if len(visited_rooms[player.current_room.id]) == 0:
        pass
        # update current move to path - 1 in order to
        # remove the last move from the path
        # then add current move to traversal path
        # move player backwards to get out of rooms with no unexplored choices
    # else
    else:
        pass
        # choose unexplored exit
        # and remove it so we don't explore it again
        # move to next room
        # add movement to our path trcker
        # add movement to traversal path

    # TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
