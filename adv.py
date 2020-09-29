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



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)


room_keys = {}
rev = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
cardinal = ['n', 'e', 's', 'w']
path = []
direction = {
    'n': ['w', 's', 'e'],
    'e': ['n', 'w', 's'],
    's': ['e', 'n', 'w'],
    'w': ['s', 'e', 'n']}

def set_doors():
    doors = {}
    for exit in player.current_room.get_exits():
        doors[exit] = '?'
    return doors

def travel(direct, prev):
    #MOVE to next room and set doors
    player.travel(direct)
    path.append(direct)
    if player.current_room.id not in room_keys:
        room_keys[player.current_room.id] = set_doors()
    visited_rooms.add(player.current_room.id)

    # SET room_keys
    room_keys[prev][direct] = player.current_room.id
    room_keys[player.current_room.id][rev[direct]] = prev
    prev = player.current_room.id

    return player.current_room.id

def backtrack(prev_direct):
    player.travel(rev[prev_direct])
    path.pop()

    return player.current_room.id

def journey():
    journey_map = []
    first_move = cardinal[1]
    #SET first room and doors
    visited_rooms.add(player.current_room.id)
    journey_map.append(player.current_room.id)
    room_keys[player.current_room.id] = set_doors()
    prev = player.current_room.id

    #MOVE to second room and set doors
    player.travel(first_move)
    path.append(first_move)
    room_keys[player.current_room.id] = set_doors()
    visited_rooms.add(player.current_room.id)
    journey_map.append(player.current_room.id)

    # SET room_keys
    room_keys[prev][first_move] = player.current_room.id
    room_keys[player.current_room.id][rev[first_move]] = prev
    prev = player.current_room.id
    prev_dir = first_move

    while len(visited_rooms) < len(room_graph):
        if player.current_room.id not in room_keys:
            room_keys[player.current_room.id] = set_doors()
        for i in direction[rev[prev_dir]]:
            if i in room_keys[player.current_room.id]:
                if room_keys[player.current_room.id][i] == '?':
                    journey_map.append(travel(i, prev))
                    prev = player.current_room.id
                    prev_dir = i
                    break
            else:
                continue
        else:
            journey_map.append(backtrack(prev_dir))
            prev = player.current_room.id
            if len(path) < 2:
                continue
            else:
                prev_dir = path[len(path) - 1]
    print(journey_map)
    return journey_map

traversal_path = journey()

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
