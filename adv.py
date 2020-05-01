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


def random_move():
    map_graph = {}
    explored = set()
    to_explore = Queue()
    exits = player.current_room.get_exits()
    current_room = player.current_room.id
    explored.add(current_room)
    map_graph[current_room] = {}
    for exit in exits:
        to_explore.enqueue(exit)
    while to_explore.size() > 0:
        direction = to_explore.dequeue()
        print(direction)
        player.travel(direction)
        traversal_path.append(direction)
        current_room = player.current_room.id
        if current_room not in explored:
            explored.add(current_room)
            exits = player.current_room.get_exits()
            for exit in exits:
                to_explore.enqueue(exit)


random_move()

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
