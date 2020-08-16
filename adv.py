from room import Room
from player import Player
from world import World
from util import Stack, Graph


import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#directions/opposite for backtracking
backtrack_directions = {"n":"s", "s": "n", "e": "w", "w":"e"}

## Keep track of the directions to backtrack the node visited 
backtrack = []
rooms = {}
# Initialize dictionary and store current room and its exits
rooms[player.current_room.id] = player.current_room.get_exits()
print("Rooms: ", rooms)

first_room = player.current_room.id
exits = player.current_room.get_exits()

#keep track of previous rooms
previous_room = None

print("graph", room_graph)
print("exits:", exits)

#while the lenght of our rooms dictionary is less than the graph
while len(rooms) < len(room_graph):
        if player.current_room.id not in rooms:
            #add it and its exits
            rooms[player.current_room.id] = player.current_room.get_exits()
            # Grab the reversed of the last direction traveled so that
            # it can be removed from the exit options of the current room
            reverse_direction = backtrack[-1]
            rooms[player.current_room.id].remove(reverse_direction)
        #when a room has no exist, need to backtrack
        while len(rooms[player.current_room.id]) < 1:
            # Pop the last reverse direction traveled to remove it from our backtrack list and add it to the traversal path, then move the player in this reverse direction
            reverse_direction = backtrack.pop()
            #print("directions: ", reverse_direction)
            traversal_path.append(reverse_direction)
            player.travel(reverse_direction)
        # Pop the first available exit direction to remove it from possible exits and
        # add it to the traversal path, then add it to the end of the backtrack path list
        exit_direction = rooms[player.current_room.id].pop(0)
        traversal_path.append(exit_direction)
        backtrack.append(backtrack_directions[exit_direction])
        # print("Traversal path: ", traversal_path)
        # print("Bactrack list: ", backtrack)
        
        # Move in the direction of the first available exit
        player.travel(exit_direction)
        # If there's only one room left unvisited, store the last room and its exits
        # in the rooms dictionary to avoid an error due to using pop() on an empty list
        if len(room_graph) - len(rooms) == 1:
            rooms[player.current_room.id] = player.current_room.get_exits()
  

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
