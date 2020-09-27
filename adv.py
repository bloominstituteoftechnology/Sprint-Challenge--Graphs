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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def opposite_path(chosen_path):
    if chosen_path == 'n':
        return 's'
    elif chosen_path == 'e':
        return 'w'
    elif chosen_path == 's':
        return 'n'
    elif chosen_path == 'w':
        return 'e'
    else:
        return None

traversal_path = []
rooms = [None] * len(room_graph)
my_graph = {}
visited_rooms = set()
paths_taken = {}

for i in range(len(room_graph)):
    rooms[i] = room_graph[i][1]

cur_room = 0
while len(visited_rooms) < len(rooms):
    visited_rooms.add(cur_room)
    if cur_room not in my_graph:
        my_graph[cur_room] = {'n': '?', 'e': '?', 's': '?', 'w': '?'}
    print(cur_room, end=" ")
    
    if 'n' not in rooms[cur_room].keys():
        my_graph[cur_room]['n'] = None
    if 'e' not in rooms[cur_room].keys():
        my_graph[cur_room]['e'] = None
    if 's' not in rooms[cur_room].keys():
        my_graph[cur_room]['s'] = None
    if 'w' not in rooms[cur_room].keys():
        my_graph[cur_room]['w'] = None

    paths = [k for k in my_graph[cur_room].keys() if my_graph[cur_room][k] is not None]
    new_paths = [p for p in paths if my_graph[cur_room][p] == '?']
    

    if len(new_paths) > 0:
        chosen_path = random.choice(new_paths)
    else:
        chosen_path = random.choice(paths)
    
    print(chosen_path, end=" ")
    traversal_path.append(chosen_path)
    next_room = rooms[cur_room][chosen_path]
    my_graph[cur_room][chosen_path] = next_room
    if next_room not in my_graph:
        my_graph[next_room] = {'n': '?', 'e': '?', 's': '?', 'w': '?'}
    my_graph[next_room][opposite_path(chosen_path)] = cur_room

    cur_room = next_room

    


# while len(visited_rooms) < 500:
# for _ in range(5):
#     all_exits = player.current_room.get_exits()
#     used_exits = [
#         e for e in visited_rooms[player.current_room.id] if e is not None]
#     unused_exits = [e for e in all_exits if e not in used_exits]
#     choice = random.choice(unused_exits)
#     print(f'all: {all_exits}')
#     print(f'used: {used_exits}')
#     print(f'unused: {unused_exits}')
#     print(f'choice: {choice}')
#     player.travel(choice)


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
