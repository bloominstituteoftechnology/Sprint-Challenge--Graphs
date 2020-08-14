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

'''  
0) Initialise stack
1) Get current room and add to stack
2) Create list adj rooms
3) Add unvisited rooms to top of stack
4) Grab top unvisited room mark it visited and add to visited
5) Get just visited rooms adj rooms
6) If no adj rooms unvisited move to prev room in stack and check for unvisited adj rooms
7) Repeat step 5 until unvisited adj room found
'''

traversal_path = ['n', 'n', 's', 'w']
print(traversal_path)
visited_rooms = []

def add_to_map(direction, map):
    player.travel(direction)
    map += [player.current_room.id]
    for e in player.current_room.get_exits():
        if e.id == map[-2]:
            continue
        else:
            addendum = add_to_map(e.id, map)
            if(len(map + addendum) == 500):
                return map + addendum

    final_map = add_to_map(player.current_room, [])

def travel_directions():
    return player.current_room.id
if player.current_room.id == 0:
    visited_rooms.append(player.current_room.id)
    print('Visited Rooms: ', visited_rooms)

travel_directions()



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
