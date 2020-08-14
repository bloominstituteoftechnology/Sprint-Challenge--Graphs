from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from collections import deque

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


def dir_entry(directions_list):
    new_dir = {
        "n": None,
        "e": None,
        "s": None,
        "w": None
    }

    for dir in directions_list:
        new_dir[dir] = dir

    return new_dir

# search of the visited set starting node


def bfs_nearest_open_node(visited, starting_node):

    q = deque()
    q.append([starting_node])

    q2 = deque()
    bfs_visited = set()

    while len(q) > 0:
        if len(q2) <= 0:
            path = []

        # records path
        else:
            path = q2.popleft()

        cur_node_path = q.popleft()
        current_node = cur_node_path[-1]

        bfs_visited.add(current_node.id)

        if len(current_node.get_exits()) > 0:
            for next_room in current_node.get_exits():
                next_node = current_node.get_room_in_direction(next_room)

                if next_node.id not in visited:
                    return [*path, next_room]

                elif next_node.id not in bfs_visited:
                    q2.append([*path, next_room])
                    q.append([*cur_node_path, next_node])

        else:
            return path


traversal_path = []

graph = dict()
visited = set()

while len(visited) < len(world.rooms):
    paths = player.current_room.get_exits()
    room_id = player.current_room.id

    if room_id not in visited:
        visited.add(room_id)

    if room_id not in graph:
        graph[room_id] = dir_entry(paths)

        for next_room in paths:
            graph[room_id][next_room] = player.current_room.get_room_in_direction(
                next_room).id

    unexplored_route = None

    for dir in graph[room_id]:
        if graph[room_id][dir] is not None and graph[room_id][dir] not in visited:
            unexplored_route = dir

    if unexplored_route is not None:
        traversal_path.append(unexplored_route)
        player.travel(unexplored_route)

    else:
        pathfinding = bfs_nearest_open_node(visited, player.current_room)

        if pathfinding is not None:
            for dir in pathfinding:
                traversal_path.append(dir)
                player.travel(dir)
                visited.add(player.current_room.id)


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

#
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
