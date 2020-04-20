from room import Room
from player import Player
from world import World
from graph import Graph, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = ['n', 'n']
traversal_path = []
visited = {}
breadcrumbs = []
opposite_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}


# Add the first room to the visited dictionary and get its exits
visited[player.current_room.id] = player.current_room.get_exits()

# num of visited rooms less than num of rooms in graph
while len(visited) < len(room_graph):
    # if we haven't been here yet
    if player.current_room.id not in visited:
        # add it to the visited dictionary and add its corresponding exits
        # get_exits returns a list
        visited[player.current_room.id] = player.current_room.get_exits()
        # access the direction just visited and remove it from the unexplored paths as we've just come from that direction
        last_move = breadcrumbs[-1]
        visited[player.current_room.id].remove(last_move)

    # no directional options left
    if len(visited[player.current_room.id]) == 0:
        # backtrack until there are directions to explore again, take items off as you go
        last_move = breadcrumbs[-1]
        breadcrumbs.pop()
        # add the previous direction to the traversal_path
        traversal_path.append(last_move)
        # move the player accordingly
        player.travel(last_move)

    # if we find a room with unexplored directions, get it ready to explore, and track it in the breadcrumbs
    else:
        next_move = visited[player.current_room.id][-1]
        visited[player.current_room.id].pop()
        traversal_path.append(next_move)
        breadcrumbs.append(opposite_directions[next_move])
        player.travel(next_move)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
