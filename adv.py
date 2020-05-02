from room import Room
from player import Player
from world import World

import random
from random import randint
from util import Queue, Stack
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
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


# Use EXPLORED set to store rooms in map_graph that have NO REMAINING ? ROOMS
def traversal():
    map_graph = {}
    to_explore = []
    current_room = player.current_room.id

    while len(map_graph) < len(room_graph):
        prev_room = current_room

        current_room = player.current_room.id
        exits = player.current_room.get_exits()

        if current_room not in map_graph:
            map_graph[current_room] = {exit: '?' for exit in exits}
        to_explore = [
            exit for exit in map_graph[current_room] if map_graph[current_room][exit] == '?'
        ]
        # print(current_room)
        while len(to_explore) > 0:
            print(to_explore)
            to_travel = to_explore.pop(0)
            reverse = ''
            if to_travel == 'n':
                reverse = 's'
            if to_travel == 's':
                reverse = 'n'
            if to_travel == 'e':
                reverse = 'w'
            if to_travel == 'w':
                reverse = 'e'
            player.travel(to_travel)
            traversal_path.append(to_travel)
            map_graph[prev_room][to_travel] = current_room
            print(map_graph)


traversal()

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


# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
