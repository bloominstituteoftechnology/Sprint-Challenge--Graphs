from room import Room
from player import Player
from world import World

from utils import Queue, Stack, Graph

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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# print(f'%%%  room_graph[0]  {room_graph[0]} ')
# print(f'\t  room_graph[0][-1]  {room_graph[0][-1]}   ')

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# create graph 
g = Graph()
g.build_graph(room_graph)
print(f' g rooms >>  {g.rooms}')
# g rooms >>  {0: {'n': '?'}, 1: {'s': '?', 'n': '?'}, 2: {'s': '?'}}


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


print(f' current info {player.current_room} ')
print(f' current info id  {player.current_room.id} ')
print(f' exits:  {player.current_room.get_exits()}')



for room in g.rooms:
    print(f'  room: {room} >>  {g.rooms[room]}  ')


# set of visited rooms 
visited = set()


# TEST starting room 0
# room:0   g_room_dir {'n': '?', 's': '?', 'e': '?', 'w': '?'}

# MOVE 'n'
# player.travel('n')
# room:1   g_room_dir {'s': '?', 'n': '?'}       list_room_dir ['?', '?'] 


while len(visited) < len(room_graph):
    
    # !!!!!   3
    g_room_dir = g.rooms[player.current_room.id]
    list_room_dir = list(g_room_dir.values())

    print(f' room:{player.current_room.id}   g_room_dir {g_room_dir}       list_room_dir {list_room_dir} ')
    

    if  '?'  in list_room_dir:
        print(f' Not Done')
        break









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
