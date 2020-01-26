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


def check_for_unex_in_path(path):
    explored = []
    if len(gr.get_unexplored_dir(player.current_room)):
        return explored
    for d in path:
        player.travel(d)
        explored.append(d)
        unex_dirs_in_d = gr.get_unexplored_dir(player.current_room)
        if len(unex_dirs_in_d):
            return explored
    return explored


def go_back_to_unexplored_room(path, base_path):
    reverse_path = [reverse_dirs[d] for d in path]
    reverse_path.reverse()
    path_to_unex = check_for_unex_in_path(reverse_path)
    base_path += path_to_unex


s = Stack()
s.push(player.current_room)
world_map = {}
while s.size:
    curr_room = s.pop()
    if curr_room not in world_map:
        world_map[curr_room] = {}
        for direction in curr_room.get_exits():
            room_in_dir = curr_room.get_room_in_direction(direction)
            world_map[curr_room][direction] = room_in_dir
            s.push(room_in_dir)

gr = Graph()
for room, directions in world_map.items():
    gr.add_vertex(room)
    for direction in directions:
        gr.add_vertex(room.get_room_in_direction(direction))


def traverse(base_path):
    s = Stack()
    for direction in gr.get_unexplored_dir(player.current_room):
        s.push(direction)
    while s.size:
        if not any('?' in d.values() for d in gr.rooms.values()):
            break
        unexplored_dir = s.pop()
        linear_dir = gr.go_in_direction_until_dead_end(
            player.current_room, unexplored_dir)
        get_current_room(linear_dir)
        base_path += linear_dir
        print('after dead end', player.current_room.id)
        dirs_in_current_room = gr.get_unexplored_dir(player.current_room)
        if len(dirs_in_current_room):
            for d in dirs_in_current_room:
                s.push(d)
        else:
            go_back_to_unexplored_room(base_path, base_path)
            print('after go back', player.current_room.id)
            for d in gr.get_unexplored_dir(player.current_room):
                s.push(d)


traverse(traversal_path)

print('last room:', player.current_room.id)

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
