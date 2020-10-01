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

#to reverse directions 
opposites = {"n": "s", "s": "n", "e": "w", "w": "e"}

def traverse(starting_room, visited=set()):
    # track the path in a list
    path = []
    # loop through the get_exits to find all exits
    for direction in player.current_room.get_exits():
        player.travel(direction)
        
        if player.current_room in visited: 
            # if a player is in a room that is visited, then turn to another direction by using inverse_direct
            player.travel(opposites[direction]) 
        else: 
            # if the room has not been visited add the new path
            visited.add(player.current_room)
            path.append(direction)

            # update current status
            path = path + traverse(player.current_room, visited)
            player.travel(opposites[direction])
            path.append(opposites[direction])

    return path

#fills in the list with the traverse func
traversal_path = traverse(player.current_room)



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
