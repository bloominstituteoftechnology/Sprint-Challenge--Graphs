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

# First pass solution: 
# Record the room in visited
# Get all the exits with the room.
# Move in one direction, add this to the traversal path and pop it off the directions associated with the room
# Work out the opposite direction and add this to a reverse path so that backtracking is possible and remove the opposite direction from the unexplored paths
# Get exits for the new room and keep note of this (in visited)
# Move in a random direction again and add to the traversal path and pop it off the possible directions
# Keep moving until you reach a dead end
# When there are no more unexplored exits - backtrack along the last direction on the backtracked path and remove it from the backtracked path and add it to the traversal path
# Check that room for unexplored directions and repeat the process again
# This keeps going until the number of rooms visited reaches the length of the rooms graph


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# Add a visited dictionary
visited = {}
# Add somewhere to store the reverse path for backtracking
reverse_path = []
# add opposite directions for backtracking
opposite_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}


# Add the first room to the visited dictionary and get its exits
visited[player.current_room.id] = player.current_room.get_exits()

# While the visited list is less than the length of rooms in the graph
while len(visited) < len(room_graph):
    # if not visited
    if player.current_room.id not in visited:
        # add it to visited and get the rooms
        visited[player.current_room.id] = player.current_room.get_exits()
        # access the direction just visited and remove it from the unexplored paths as we've just come from that direction
        previous_direction = reverse_path[-1]
        visited[player.current_room.id].remove(previous_direction)

    # if the length of the paths associated with the room is 0 (when all the paths have been explored)
    if len(visited[player.current_room.id]) == 0: 
        # backtrack to previous room until a room with unexplored paths is found
        # assign the last addition to the reverse_path as the previous direction and pop it from reverse_path
        previous_direction = reverse_path[-1]
        reverse_path.pop()
        # add the previous direction to the traversal_path
        traversal_path.append(previous_direction)
        # move the player in that direction
        player.travel(previous_direction)

    # if there is an unexplored direction
    # add the direction to the traversal_path
    # explore the new room
    else:
        # take the first available direction in the room, assign it to direction and pop it from the list
        direction = visited[player.current_room.id][-1]
        visited[player.current_room.id].pop()
        # add the direction to the traversal_path
        traversal_path.append(direction)
        # record the opposite direction to the move in the reverse_path
        reverse_path.append(opposite_direction[direction])
        # move the player in that direction
        player.travel(direction)           





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



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
