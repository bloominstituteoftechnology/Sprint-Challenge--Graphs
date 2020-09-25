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
# map_file = "maps/main_maze.txt"

map_file = "/Users/lambdacatalina/Desktop/LAMBDA-SCHOOL/COMPUTER SCIENCE/Unit 6 - Graphs/Sprint-Challenge--Graphs/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#setup opposite directions
opposite_directions = {'n': 's', 's' : 'n', 'e' : 'w', 'w' :'e'}

reversed_transversal = [None]
visitedSoFar = {}

while len(visitedSoFar) < len(room_graph) - 1:

    if player.current_room.id not in visitedSoFar:
        visitedSoFar[player.current_room.id] = player.current_room.get_exits()

        if reversed_transversal[-1]:
            visitedSoFar[player.current_room.id].remove(reversed_transversal[-1])

        else:
            continue
    
    while len(visitedSoFar[player.current_room.id]) == 0:
        previous_path = reversed_transversal.pop()
        traversal_path.append(previous_path)
        player.travel(previous_path)
    
    next_direction = visitedSoFar[player.current_room.id].pop()
    traversal_path.append(next_direction)
    reversed_transversal.append(opposite_directions[next_direction])
    player.travel(next_direction)

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
