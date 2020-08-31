from room import Room
from player import Player
from world import World

from utils import Stack

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

def prevPath(dir):
    if dir == 'n':
        return 's'
    elif dir == 's':
        return 'n'
    elif dir == 'e':
        return 'w'
    elif dir == 'w':
        return 'e'
    else:
        print('You enter an invaild response')

def roomTraversal(start):
    stack = Stack()
    visited = set()

    # see where the player is starting from
    start = player.current_room

    # loop through all exits until all rooms all visited
    while len(visited) < len(world.rooms):
        #create a path to record prev path traveled
        path = []

        for exit in player.current_room.get_exits():

            if exit is not None:
                if player.current_room.get_room_in_direction(exit) not in visited:

                    path.append(exit)
                    print('path', path)
        vivisited.add(player.current_room)

        if len(path) != 0:

            move = random.randint(0, len(path) - 1)
            stack.push(path[move])
            player.travel(path[move])

            traversal_path.append(path[move])
        else:

            last = stack.pop()

            player.travel(prevPath(last))
            traversal_path.append(prevPath(last))


                          



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
