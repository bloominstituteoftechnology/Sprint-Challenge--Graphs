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

# <-- START CODE
visited = {}

oppostie_dir = {
    'n': 's', 's': 'n', 'e': 'w', 'w': 'e'
    }

backtrack_route = [None]

# while number of rooms visited is less than total number of rooms
while len(visited) < len(room_graph) - 1:
    # if the current room has not yet been visited
    if player.current_room.id not in visited:
        # get all the exits of the current room
        visited[player.current_room.id] = player.current_room.get_exits()
        # if we have come in from another room,
        if backtrack_route[-1]:
            # remove the direction we just came from the current room (in visited rooms)
            visited[player.current_room.id].remove(backtrack_route[-1])
        else:
            continue
    # while the current room you are in does not have any unvisted exits
    while len(visited[player.current_room.id]) == 0:
        # the previous path is equal to the last direction in the backtrack route
        previous_path = backtrack_route.pop()
        # add to the traversal path the previous path
        traversal_path.append(previous_path)
        # travel the previous path
        player.travel(previous_path)
    # next direction is equal to the most recently visited room
    next_direction = visited[player.current_room.id].pop()
    # add the next direction to the traversal path
    traversal_path.append(next_direction)
    # add to the backtracking route by adding the opposite direction to the next direction
    backtrack_route.append(oppostie_dir[next_direction])
    # go in the next direction!
    player.travel(next_direction)
# --> END CODE

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
