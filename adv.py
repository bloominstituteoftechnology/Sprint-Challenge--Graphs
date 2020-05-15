from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


def check_move(move, x, y):
    if move == "n":
        return world.room_grid[x][y+1]
    elif move == "s":
        return world.room_grid[x][y-1]
    elif move == "e":
        return world.room_grid[x+1][y]
    else:
        return world.room_grid[x-1][y]


def inverse_move(move):
    if move == "n":
        return "s"
    elif move == "s":
        return "n"
    elif move == "e":
        return "w"
    else:
        return "e"


def dfs(room, visited, path, t, path_builder=None):
    if path_builder is None:
        path_builder = []

    possible_paths = visited[room.id][1]
    x, y = visited[room.id][0]

    for move in possible_paths:
        # opposite = inverse_move(move)
        next_room = check_move(move, x, y)
        if possible_paths[move] == "?" and next_room.id not in t:
            path_builder = path_builder.copy()
            path_builder.append(move)
            possible_paths[move] = next_room.id
            # if next_room.id not in t:
            np = dfs(next_room, visited, path, t, path_builder)

            if np:
                return np

    return path_builder


def traverse_all_rooms(starting_room):
    visited = {}
    path = []
    t = set()
    # populate visited with unexplored rooms
    for i in range(len(world.rooms)):
        neighbors = {}
        exits = world.rooms[i].get_exits()
        x, y = world.rooms[i].get_coords()
        for move in exits:
            neighbors[move] = "?"
        visited[i] = [(x, y), neighbors]
    q = [starting_room]
    # print(visited)
    while len(q) > 0:
        curr = q.pop(0)
        possible_paths = visited[curr.id][1]
        x, y = visited[curr.id][0]
        print("----->", (x, y), possible_paths)
        for move in possible_paths:
            if possible_paths[move] == "?":
                print("hey", move)
                t.add(curr.id)
                # path.append(move)
                # next_room = check_move(move, x, y)
                # possible_paths[move] = next_room.id
                opposite = inverse_move(move)
                # if opposite in visited[next_room.id][1]:
                #     visited[next_room.id][1][opposite] = curr.id
                dfs_path = dfs(curr, visited, path, t)
                dfs_path += opposite
                path += dfs_path
                print("*&", dfs_path)
    print("SDLfjsdlfjlsdklsdf, path", path)
    for move in path:
        traversal_path.append(move)


traverse_all_rooms(player.current_room)

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
