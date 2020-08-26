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
traversal_path = []
# START HERE
# in case we mess up, we have to be able to back up
reverse_direction = {'n': 's','s': 'n','w': 'e', 'e': 'w'}
# create function, where we can pass in a starting room and a visited set -> make sure you have a place to place path (arr)
# loop through player.current_room.get_exits() to find all possible exits
    # player should be able to travel in the direction of exit
        #  if, visited already, reverse
        # else (room not yet visited)
            # add the id to visited set + add the new direction to the path
            # recurse with new current room and add it to the path
            # use reverse to go backwards again
            # add the backtrack steps (direction) to new_path in order to keep track of it
        # return the path
       
def map_traversal(starting_room, visited=set()):
 
    new_path = []

    for direction in player.current_room.get_exits():
        player.travel(direction)

        if player.current_room.id in visited:
            player.travel(reverse_direction[direction])
        else:
            # room has not been visited
            visited.add(player.current_room.id)
            new_path.append(direction)
            # new_path has direction add
            # direction + recurse to have current status
            new_path = new_path + map_traversal(player.current_room.id, visited)
            player.travel(reverse_direction[direction])
            new_path.append(reverse_direction[direction])
          
    return new_path

# no longer empty arr, passes in id to call func
traversal_path = map_traversal(player.current_room.id)




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
