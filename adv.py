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

# Initialise vert stack
traversal_path = ['n', 'e', 's', 'w']
print(traversal_path)
visited_rooms = []

def add_to_maze(direction, maze):
    player.travel(direction)
    maze += [player.current_room.id]
    for exit in player.current_room.get_exits():
        if exit.id == maze[-2]:
            continue
        else:
            add_on = add_to_maze(exit.id, maze)
            if(len(maze + add_on) == 500):
                return maze + add_on

final_maze = add_to_maze(player.current_room, [])

def travel_directions():
    return player.current_room.id
if player.current_room.id == 0:
    visited_rooms.append(player.current_room.id)
    print('Visited Rooms: ', visited_rooms)

'''  
0) Get current room and add to stack
1) Create list adj rooms
2) Add unvisited rooms to top of stack
3) Grab top unvisited room mark it visited and add to visited
4) Get just visited rooms adj rooms
5) If no adj rooms unvisited move to prev room in stack and check for unvisited adj rooms
6) Repeat step 5 until unvisited adj room found
'''
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
