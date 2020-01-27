from random import choice
from room import Room
from player import Player
from world import World
from util import Queue, Stack, Graph, reverse_dirs

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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []


def get_current_room(path):
    for d in path:
        player.travel(d)


def find_unexplored_room():
    q = Queue()
    for d in player.current_room.get_exits():
        q.enqueue([(player.current_room, d)])
    visited = set()
    while q.size:
        path = q.dequeue()
        curr_room = path[-1][0]
        if '?' in gr.rooms[curr_room].values():
            return [d for _, d in path][1:]
        elif curr_room not in visited:
            visited.add(curr_room)
            for direction in curr_room.get_exits():
                next_room = curr_room.get_room_in_direction(direction)
                q.enqueue(
                    path + [(next_room, direction)])
    return None


gr = Graph()
for room in world.rooms.values():
    gr.add_vertex(room)


while True:
    if not any('?' in d.values() for d in gr.rooms.values()):
        break
    linear_dir = gr.go_in_direction_until_dead_end(player.current_room)
    get_current_room(linear_dir)
    traversal_path += linear_dir
    path_to_unexplored_room = find_unexplored_room()
    if path_to_unexplored_room is not None:
        traversal_path += path_to_unexplored_room
        get_current_room(path_to_unexplored_room)

# TRAVERSAL TEST
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
