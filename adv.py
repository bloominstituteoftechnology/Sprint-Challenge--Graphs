from room import Room
from player import Player
from world import World
from util import Stack, Queue

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
# keeps track of path

# print('current room', player.current_room.id)
 # first room
    # Room 0
    # (3, 5)
    # Exits: [n]
# print('current room exts', player.current_room.get_exits())

traversal_path = []
# when an end is reached, player needs to backtrack in the opposite direction
reverse_dir = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w'
}

def traverse_map(starting_room, visited=set()):
 
    path = []
    
    # get all possible exits in current_room
    for direction in player.current_room.get_exits():
        # player travel to room in direction of exit
        player.travel(direction)

        # check if new room has been visited
        if player.current_room.id not in visited:
            # room has not been visited
            # mark as visited
            visited.add(player.current_room.id)
            # add new direction to path
            path.append(direction)
            # recurse with new current_room and add to path
            path = path + traverse_map(player.current_room.id, visited)
            # backtrack and go to different room
            player.travel(reverse_dir[direction])
            # add backtrack to path to keep track of steps 
            path.append(reverse_dir[direction])

        else:
            # Room already visited so backtrack and go to different room
            player.travel(reverse_dir[direction])

    return path

traversal_path = traverse_map(player.current_room.id)

## 1000 steps


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



######
# UNCOMMENT TO WALK AROUND
######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# when a player can no longer go in a cardinal direction, the player either goes to an entirely different available exit or goes in the opposite direction to backtrack out of the room. Ex, head N reach a deadend, must head S to exit out of room