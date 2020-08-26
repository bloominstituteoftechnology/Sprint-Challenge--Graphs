from room import Room
from player import Player
from world import World

from util import Queue, Stack

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
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
reverse = {"n": "s", "s": "n", "e": "w", "w": "e"}

# ? first pass (no queue or stack)
def find_the_cheese(visited_rooms=[]):
    store_directions = []
    # print(f"store = {store_directions}")

    # print(f"current room: {player.current_room.id}")
    # print(f"visited rooms: {visited_rooms}")

    # ? getting directions for current room from get_exits() in room.py
    for direction in player.current_room.get_exits():

        # ? using travel() from player.py to move player
        # print(f"dir: {direction}")
        player.travel(direction)

        # ? check if current room has been visited
        if player.current_room.id not in visited_rooms:
            # ? mark current room as visited, track direction
            # print(f"not visited: {player.current_room.id}")
            visited_rooms.append(player.current_room.id)
            store_directions.append(direction)

            # ? set store to current store + updated visited rooms
            # print(f"store before: {store_directions}")
            store_directions = store_directions + find_the_cheese(visited_rooms)
            # print(f"store after: {store_directions}")

            # ? use travel() from player.py to move player, track direction
            player.travel(reverse[direction])
            store_directions.append(reverse[direction])

        else:
            # ? use travel() from player.py to move player in opposite direction
            # print(f"already visited: {player.current_room.id}")
            player.travel(reverse[direction])

    # print(f"store = {store_directions}")
    return store_directions


# ? fill traversal_path list
traversal_path = find_the_cheese()
# print(f"traversal path: {traversal_path}")

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
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
