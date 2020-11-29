from room import Room
from player import Player
from world import World

import random
from collections import deque
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
traversal_path = ['n', 's', 'w', 'e']
opposite_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# Pick a random unexplored direction from current room, travel and log that direction, then loop. When reach dead end, walk back and find nearest room that is unexplored.

exits = player.current_room.get_exits()
currRoom = player.current_room.id

# Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.

# def bfs(self, starting_vertex = currRoom, destination_vertex = ?):
# visited_rooms = set()
# queue = deque()
# queue.append ([currRoom])

# while len(queue) > 0:
#     currPath = queue.popleft()
#     currNode = currPath[-1]

#     if currNode is ?:
#         return currPath

#     if currNode not in visited_rooms:
#         visited_rooms.add(currNode)
#         for neighbor in self.visited_rooms:
#             newPath = list(currPath)
#             newPath.append(neighbor)
#             queue.append(newPath)
# return []

def traverse_map(starting_room, visited=[]):
    #   Define a path with what you start with aka no rooms or possible directions
    path = []
#   Loop through the exits for the current room
    for direction in player.current_room.get_exits():
        # Have the player travel in the given directions
        player.travel(direction)
#       Check to see if the current room is already in the `visited` array
        if player.current_room.id in visited:
            # If it is, move the player in the opposite direction, that room has already been visited so we've already checked all possible directions
            player.travel(opposite_directions[direction])
#           If it is not
        else:
            # Add the current room to the `visited` array
            visited.append(player.current_room.id)
#           Add that direction to the path array
            path.append(direction)
#           Let the path equal the current path plus the path we just created
            path = path + traverse_map(player.current_room.id, visited)
#           Have the player travel in the opposite direction of the path
            player.travel(opposite_directions[direction])
#           Add the opposite directions to the path array
            path.append(opposite_directions[direction])

    # finally, return the path
    return path


traversal_path = traverse_map(player.current_room.id)

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
