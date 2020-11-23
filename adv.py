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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# Get exits for each room
# Add any room visited to queue
# Create a way to move in the opposite direction to go backwards
# Repeat till all 500 rooms visited

# traversal_path = ['n', 'n']
traversal_path = []
# this will loop until we have visited each node
visited = {}
# keep track of when player goes backwards
go_backwards = []
# create a compass of which way to go for each value
backwards_compass = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# where is the player
room_location = player.current_room.id
# room index starting point, add to visited
visited[room_location] = player.current_room.get_exits()

# Loop through rooms that have not been visited
while len(visited) < len(room_graph):
    # starting point, not visited rooms
    if player.current_room.id not in visited:
        # add to visited and get next direction
        visited[player.current_room.id] = player.current_room.get_exits()
        # after room is visited it needs to be removed for optimal travel
        last_path = go_backwards[-1]
        visited[player.current_room.id].remove(last_path)

    # when all rooms are visited stop the loop and continue finding unvisited nodes
    if len(visited[player.current_room.id]) == 0:
        # until you find a room not visited
        last_path = go_backwards[-1]
        # remove from last path
        go_backwards.pop()
        # add to the previous
        traversal_path.append(last_path)
        # move player to unvisited node
        player.travel(last_path)

    # any exit not taken
    else:
        cardinal = visited[player.current_room.id][-1]
        # take out of visited
        visited[player.current_room.id].pop()
        # add to traversal
        traversal_path.append(cardinal)
        # add backwards
        go_backwards.append(backwards_compass[cardinal])
        # move player to new room
        player.travel(cardinal)


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
