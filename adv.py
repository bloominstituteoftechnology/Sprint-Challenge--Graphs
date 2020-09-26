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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

move_back = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}


def mazeTraversal(current_room, visited=None):
    # list for directions when moving rooms
    directions = []
# check if visited is none loop and create set to hold visited vertex
    if visited == None:
        visited = set()
# find all exits in current room
    for move in player.current_room.get_exits():
        player.travel(move)  # move in selected room

# if room is visited move_back to find the unvisited path
        if player.current_room in visited:
            player.travel(move_back[move])
# if room is unvisited.
        else:
            # add to visited
            visited.add(player.current_room)
# append the move to the directions
            directions.append(move)
#  use recursive call to repeat the loop and add directions to path
            directions = directions + \
                mazeTraversal(player.current_room, visited)
            # Move to previous room
            player.travel(move_back[move])
            # add move_back to the direction list
            directions.append(move_back[move])

    return directions


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = mazeTraversal(player.current_room)
print(mazeTraversal)


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
