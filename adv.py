from room import Room
from player import Player
from world import World
from collections import deque
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

visited = {}
reverse = []
opposite_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph) - 1:
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()
        previous_direction = reverse[-1]
        visited[player.current_room.id].remove(previous_direction)

    while len(visited[player.current_room.id]) < 1:
        reverse_direction = reverse.pop()
        traversal_path.append(reverse_direction)
        player.travel(reverse_direction)

    find_exit = visited[player.current_room.id].pop(0)
    traversal_path.append(find_exit)
    reverse.append(opposite_direction[find_exit])
    player.travel(find_exit)


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



# TO PLAY UN-COMMENT

# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
