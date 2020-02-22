from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# IMPORTS
from utils import Queue, Stack
import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt" 
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# -- START CODE -- #
# -- START CODE -- #

# -1- SETUP
# Initialize Reverse Distionary 
reverse_direction = {'n':'s', 'e':'w', 's':'n', 'w':'e'}

# Helper Functions
def check_for_question(graph):
    for key in graph:
        if '?' in graph[key].values():
            return True
    return False

# -2- STEPS
s = Stack()
s.push(player.current_room)

visited_rooms = {}

# while s.size() > 0:
while len(visited_rooms) < len(world.rooms):
    curr_room = s.pop()
    print(f'-*- CURRENT ROOM: {curr_room}')

    visited_rooms[curr_room.id] = {}

    available_exits = curr_room.get_exits()
    print(f'-*- AVAILABLE EXITS: {available_exits}')
    for direction in available_exits:
        next_room_option = curr_room.get_room_in_direction(direction)
        print(f'-*- NEXT ROOM OPTION: {next_room_option}')
        
        # visited_rooms[curr_room.id][direction] = '?'
        visited_rooms[curr_room.id][direction] = next_room_option.id
        
        if next_room_option.id not in visited_rooms:
            filtered_exit_options = []
            filtered_exit_options.append(direction)
            print(f'-*- FILTERED AVAILABLE EXITS: {filtered_exit_options}')
    
    print(f'-*- VISITED ROOMS: {visited_rooms}')

    # Pick Movement Direction
    chosen_direction = filtered_exit_options[
        random.randint(0, len(filtered_exit_options) -1 )
    ]
    print(f'-*- CHOSEN DIRECTOIN: {chosen_direction}')

    # Update Travesal Path
    traversal_path.append(chosen_direction)
    print(f'-*- TRAVERSAL PATH: {traversal_path}')

    # Move Player
    player.travel(chosen_direction)
    s.push(player.current_room)


    


# for avail_direction in player.current_room.get_exits():
#     visited_rooms[player.current_room.id][avail_direction] = '?'
# print(visited_rooms)


# while s.size() > 0:
#     # Get Current Node
#     current_node = s.pop()
#     print(f'CURRENT NODE: {current_node}')

#     # Add Current Node to Visited Dictionary
#     visited_rooms[current_node.id] = {}
#     print(f'VISITED ROOMS: {visited_rooms}')

#     # Get Exits for current node
#     available_exits = current_node.get_exits()
#     print(f'AVAILABLE EXITS: {available_exits}')

#     # Pick Random Direction
#     direction = available_exits[random.randint(0, len(available_exits) - 1)]
#     print(f'CHOSEN DIRECTION: {direction}')
#     traversal_path.append(direction)
#     print(f'TRAVERSAL PATH: {traversal_path}')

#     # Get room in that direction
#     test = current_node.get_room_in_direction(direction)
#     print(f'TESTING GET ROOM IN THAT DIRECTION: {test}')

#     # Update Visited Dictionary w/ available direction
#     visited_rooms[current_node.id][direction] = test.id
#     print(visited_rooms)

#     if test.id in visited_rooms:
#         print(f'ALREADY THERE')
#         exit()


#     # Move in that direction
#     player.travel(direction)

#     # Add new room to stack
#     s.push(player.current_room)








# -- END CODE -- #
# -- END CODE -- #


# TRAVERSAL TEST
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
