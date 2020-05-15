from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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
traversal_path = ['n', 's']

# Set up a direction opposite directions
opposite_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

previous_room = [None]
room_queue = {}
visited = {}

def check_direction(roomId):
    directions = []
    if 'n' in room_graph[roomId][1].keys():
        directions.append('n')
    if 'e' in room_graph[roomId][1].keys():
        directions.append('e')
    if 's' in room_graph[roomId][1].keys():
        directions.append('s')
    if 'w' in room_graph[roomId][1].keys():
        directions.append('w')
    return directions

while len(visited) < len(room_graph):
    room_id = player.current_room.id
    if room_id not in room_queue:
        visited[room_id] = room_id
        room_queue[room_id] = check_direction(room_id)
        
    if len(room_queue[room_id]) < 1:
        previous_direction = previous_room.pop()
        traversal_path.append(previous_direction)
        player.travel(previous_direction)
        
    else:
        next_direction = room_queue[room_id].pop(0)
        traversal_path.append(next_direction)
        previous_room.append(opposite_directions[next_direction])
        player.travel(next_direction)


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
