from room import Room
from player import Player
from world import World

import random
from util import Graph, Queue, Stack
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
# reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# visited rooms = dict or set?
# holds the rooms that are visited, kv
visited_rooms = {}
# create an array? maybe a queue for the path
master_path = []
# commands that reverse the current direction in the traversal so we can go backwards
reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# takes current room, appends to dict for visited rooms,
# gets exits we can begin traversal
visited_rooms[player.current_room.id] = player.current_room.get_exits()
# begin traversal, if the length of visited rooms is less than length of room graph
while len(visited_rooms) < len(room_graph) - 1:
    # check if the current room is in the visited_rooms dict
    if player.current_room.id not in visited_rooms:
        # add the current room to the visited_rooms dict:;
        visited_rooms[player.current_room.id] = player.current_room.get_exits()
        # grab the previous direction
        prev_direc = master_path[-1]
        # remove the previous direction so we dont try to go through the same place again
        visited_rooms[player.current_room.id].remove(prev_direc)
        # change the traversal to not just look for the shortest path but all rooms
        # go backwards through the path, annd start checking the rest of the rooms
    while len(visited_rooms[player.current_room.id]) == 0:
        # remove lst set of exits
        prev_direc = master_path.pop()
        # add last set of exits to traversal path
        traversal_path.append(prev_direc)
        # use travel function on player to move around to previous room
        # check if these rooms are visited
        player.travel(prev_direc)
    # check current rooms exits, find the last room on list, go to room
    next_move = visited_rooms[player.current_room.id].pop(0)
    # append to the path because this is the direction we want to go
    traversal_path.append(next_move)
    # append it here so we have a record of going there
    master_path.append(reverse_direction[next_move])
    # use the directions dict we created to go backwards, then travel backward through rooms
    player.travel(next_move)

# ***********************************************************
# def get_all_rooms(self, starting_room):
#     # create a Queue to store the neighbor rooms
#     neighbor_rooms_to_visit = Queue()
#     # create a dictionary to store visited rooms
#     visited_rooms = {}
#     # add current room to the romms to visit queue
#     neighbor_rooms_to_visit.enqueue([starting_room])
#     # while the rooms to visit queue is greater than 0
#     while neighbor_rooms_to_visit.size() > 0:
#         # create var to store the current working path
#         current_path = neighbor_rooms_to_visit.dequeue()
#         # grab the last vertex on the oath
#         current_path_last_vertex = current_path[-1]
#         # if the last room is not in visited rooms
#         if current_path_last_vertex not in visited_rooms:
#             # add it to visited rooms as a new key
#             visited_rooms[current_path_last_vertex] = current_path
#             # take each option and ?
#             for neighbor in player.current_room.get_exits():
#                 return neighbor
# ***********************************************************

# ***********************************************************
# def master_path(visited_rooms=[]):
#     # create an empty array to store directions
#     room_directions = []
#     # get each possible exit in current room
#     for direction in player.current_room.get_exits():
#         # move to those directions with player.travel
#         player.travel(direction)
#         # if the cureent room is not in visited rooms
#         if player.current_room.id not in visited_rooms:
#             # add that room to the visited rooms
#             visited_rooms.append(player.current_room.id)
#             # add the direction of the room to the room directions array
#             room_directions.append(direction)
#             # reset room directions to be the master path
#             room_directions = room_directions + \
#                 master_path(visited_rooms)
#             # travel in the reverse directions to get rest of rooms
#             player.travel(reverse_direction[direction])
#         else:
#             # if current room in not in visited rooms, go backwards
#             player.travel(reverse_direction[direction])
#     return room_directions
# traversal_path = master_path()
# ***********************************************************


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
