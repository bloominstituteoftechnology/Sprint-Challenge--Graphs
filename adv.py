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

# This is the visited rooms
# holds the vistied rooms
visited = {}
# create a list for path
my_path = []
# list of reverse commands to enable going backwards
reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# appending current room to 'visited;
visited[player.current_room.id] = player.current_room.get_exits()
# traverse if length of visited room is < than legnth of room
while len(visited) < len(room_graph) - 1:
    # see of room is in visted dictionary
    if player.current_room.id not in visited:
        # lets add current_room to the dictionary
        visited[player.current_room.id] = player.current_room.get_exits()
        # obtain the previous direction
        previous_direction = my_path[-1]
        # removing and avoid going previous directions
        visited[player.current_room.id].remove(previous_direction)
    # this changes the traversal through all rooms
    while len(visited[player.current_room.id]) == 0:
        # removes the previous exits with pop()
        previous_direction = my_path.pop()
        # adding last exits towards traversal path
        traversal_path.append(previous_direction)
        # review rooms visited
        player.travel(previous_direction)
    #looks into current_room and finds last room on the list
    next_move = visited[player.current_room.id].pop(0)
    # appends next_move in the right path
    traversal_path.append(next_move)
    # appends the specific record on next_move
    my_path.append(reverse_direction[next_move])
    # use the directions dictionary to go backwards through rooms
    player.travel(next_move)

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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
