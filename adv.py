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

backtracking = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w'
}


def maze_traversal(current_room, visited=None):
    # list for directions while moving rooms
    directions = []
    # if visited is none (1st loop) create a set to hold all visited nodes
    if visited == None:
        visited = set()

    # Find all exits for current room
    for move in player.current_room.get_exits():
        # Move in selected direction
        # print(move)
        player.travel(move)

        # If room is in visited, backtrack to find an unvisited path
        if player.current_room in visited:
            player.travel(backtracking[move])
            # print(backtracking[move])
        # if we haven't visited this room:
        else:
            # Add to visited
            visited.add(player.current_room)
            # append the move to the directions list
            directions.append(move)
            # recursive call and repeat the above loop and add directions to path
            directions = directions + \
                maze_traversal(player.current_room, visited)
            # Move to previouss room
            player.travel(backtracking[move])
            # add backtracking to the directions list
            directions.append(backtracking[move])

    return directions




# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = maze_traversal(player.current_room)
print(maze_traversal)

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
